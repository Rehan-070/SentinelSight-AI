import cv2
import numpy as np
import speech_recognition as sr
import threading
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import os

# ==============================
# EMAIL CONFIGURATION
# ==============================
EMAIL_SENDER = "rehan0rc0@gmail.com"   # <-- Replace with your Gmail
EMAIL_PASSWORD = "ngiy gqqr uvwp dhcw"    # <-- Use Gmail App Password
EMAIL_RECEIVER = "rehan0rc0@gmail.com"  # Receiver email

def send_email(image_path, audio_path, speech_text):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = "⚠️ Weapon & Threat Detected!"

        body = f"A weapon and threat were detected!\n\nSpeech: {speech_text}"
        msg.attach(MIMEText(body, 'plain'))

        # Attach image
        if os.path.exists(image_path):
            with open(image_path, "rb") as f:
                mime = MIMEBase('image', 'jpg', filename="attacker.jpg")
                mime.add_header('Content-Disposition', 'attachment', filename="attacker.jpg")
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)

        # Attach audio
        if os.path.exists(audio_path):
            with open(audio_path, "rb") as f:
                mime = MIMEBase('audio', 'wav', filename="threat_audio.wav")
                mime.add_header('Content-Disposition', 'attachment', filename="threat_audio.wav")
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", str(e))


# ==============================
# SPEECH RECOGNITION
# ==============================
speech_text_queue = []
audio_file_queue = []
threat_keywords = ["kill", "die", "murder", "shoot"]

def listen_microphone():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        try:  
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                print("🎤 Listening for 5 seconds...")
                audio = recognizer.listen(source, phrase_time_limit=5)

            # Save audio to file
            audio_path = "threat_audio.wav"
            with open(audio_path, "wb") as f:
                f.write(audio.get_wav_data())

            text = recognizer.recognize_google(audio).lower()
            print("🗣️ Recognized Speech:", text)
            speech_text_queue.append(text)
            audio_file_queue.append(audio_path)

        except sr.UnknownValueError:
            print("❌ Could not understand audio")
        except sr.RequestError as e:
            print("❌ Speech recognition error:", e)
        time.sleep(1)


# ==============================
# YOLO SETUP
# ==============================
weights_path = r"d:\PY\Wepons\yolov3.weights"
config_path = r"d:\PY\Wepons\yolov3.cfg"
names_path = r"d:\PY\Wepons\coco.names"

net = cv2.dnn.readNet(weights_path, config_path)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

weapon_classes = ["knife", "scissors", "gun"]  # YOLO COCO supports knife, scissors


# ==============================
# START AUDIO THREAD
# ==============================
threading.Thread(target=listen_microphone, daemon=True).start()


# ==============================
# OPEN CAMERA
# ==============================
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416),
                                 (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids, confidences, boxes = [], [], []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    weapon_detected = False
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            conf = int(confidences[i] * 100)

            if label in weapon_classes:
                color = (0, 0, 255)  # Red for weapon
                weapon_detected = True
            else:
                color = (0, 255, 0)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {conf}%", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # ==============================
    # CHECK CONDITION: WEAPON + THREAT
    # ==============================
    if weapon_detected and speech_text_queue:
        last_text = speech_text_queue[-1]
        last_audio = audio_file_queue[-1] if audio_file_queue else None
        if any(word in last_text for word in threat_keywords):
            print("⚠️ Weapon + Threat detected! Sending email...")
            cv2.imwrite("attacker.jpg", frame)
            send_email("attacker.jpg", last_audio, last_text)
            speech_text_queue.clear()
            audio_file_queue.clear()
            time.sleep(5)  # avoid spamming

    cv2.imshow("Weapon Detection + Threat Alert", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
