# import streamlit as st
# from streamlit_webrtc import webrtc_streamer
# import cv2
# import av
# import face_recognition

# st.title("Face Detection")
# Find all the faces in the current frame of video




# def callback(frame):
#     img = frame.to_ndarray(format="bgr24")
#     st.write(img.shape)

#     # img = cv2.cvtColor(cv2.Canny(img, threshold1, threshold2), cv2.COLOR_GRAY2BGR)
#     # img = cv2.cvtColor(cv2.Canny(img, threshold1, threshold2))
#     # rgb_frame = frame[:, :, ::-1]
#     # Find all the faces in the current frame of video
#     face_locations = face_recognition.face_locations(frame)
#     for top, right, bottom, left in face_locations:
#         img = cv2(cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2))
#     return av.VideoFrame.from_ndarray(img, format="bgr24")
# def callback(frame):
#     img = frame.to_ndarray()

#     img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
#     st.image(frame)
#     # rgb_frame = frame[:, :, ::-1]
#     # face_locations = face_recognition.face_locations(rgb_frame)
    
#     # for top, right, bottom, left in face_locations:
#         # img = cv2(cv2.rectangle(rgb_frame, (left, top), (right, bottom), (0, 0, 255), 2))
    
#     # x = av.img.VideoFrame(1920, 1080, 'rgb24')
#     return av.VideoFrame.from_ndarray(img)

# webrtc_streamer(key="example", video_frame_callback=callback)

# import cv2
# import streamlit as st

# # ret, im = camera.read()

# st.title("Video stream")
# run = st.checkbox('start')
# FRAME_WINDOW = st.image([])
# camera = cv2.VideoCapture(0)

# while run:
#     _, frame = camera.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     FRAME_WINDOW.image(frame)
# else:
#     st.write('Stopped')



import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2 
import av


st.title("live stream")





def callback(frame):
    img = frame.to_ndarray(format="bgr24")

    img = cv2.cvtColor(cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")



webrtc_streamer(
    key="example",
    video_frame_callback=callback,
    rtc_configuration={  # Add this line
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)