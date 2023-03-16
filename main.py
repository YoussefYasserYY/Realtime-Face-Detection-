
# import streamlit as st
# from streamlit_webrtc import webrtc_streamer

# st.title("My first Streamlit app")
# st.write("Hello, world")

# webrtc_streamer(key="example")
# cap = cv2.VideoCapture(0)





# webrtc_streamer(key="example")


# while True:
#     # Grab a single frame of video
#     ret, frame = cap.read()
#     # Convert the image from BGR color (which OpenCV uses) to RGB   
#     # color (which face_recognition uses)
#     rgb_frame = frame[:, :, ::-1]
#     # Find all the faces in the current frame of video
#     face_locations = face_recognition.face_locations(rgb_frame)
#     for top, right, bottom, left in face_locations:
#         # Draw a box around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0,  
#         255), 2)
#     # Display the resulting image
#     # cv2.imshow('Video', frame)
#     st.video(frame)
    



# while True:
#     # Grab a single frame of video
#     ret, frame = cap.read()
#     # Convert the image from BGR color (which OpenCV uses) to RGB   
#     # color (which face_recognition uses)
#     rgb_frame = frame[:, :, ::-1]

#     # Display the resulting image
#     # cv2.imshow('Video', frame)
#     st.image(frame)   
    
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
# # video_file = open(, 'rb')
# # video_bytes = video_file.read()

# # st.video(video_bytes)
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import av
# import face_recognition

st.title("Face Detection")
# Find all the faces in the current frame of video

def callback(frame):
    img = frame.to_ndarray(format="bgr24")

    img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
    # face_locations = face_recognition.face_locations(img)
    # cv2.rectangle(frame, (left, top), (right, bottom), (0, 0,  
        # 255), 2)

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=callback)
#     rgb_frame = frame[:, :, ::-1]
#     # Find all the faces in the current frame of video
#     for top, right, bottom, left in face_locations:
#         # Draw a box around the face


