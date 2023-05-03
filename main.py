import cv2
import streamlit as st

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Define a function to detect faces
def detect_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return img

# Initialize camera capture
cap = cv2.VideoCapture(0)

# Set output dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create a Streamlit window to display the output
st.title("Face Detection App")
output = st.empty()


T = st.checkbox('Stop video')

# Main loop to detect and display faces
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = detect_faces(frame)
    output.image(frame, channels="BGR")
    if T==True:
        break


