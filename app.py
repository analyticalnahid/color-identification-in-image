# importing library
import cv2
import numpy as np
import streamlit as st

# title
st.title("Color Detection App")
st.write("Developed by: [Nahidul Islam]")

#image uploader
uploader = st.file_uploader(label="Upload an image", type=["png", "jpg", "jpeg"])

opt = st.multiselect("Select the color", ["blue", "red", "green", "yellow"])

if uploader is not None:
    input_img = cv2.imdecode(np.frombuffer(uploader.read(), np.uint8), -1)
    st.write("Original Image")
    st.image(input_img)
    
    if opt:
        if opt[0] == "blue": 
            color = np.uint8([[[255,0,0]]])

        elif opt[0] == "red":
            color = np.uint8([[[0,0,255]]])

        elif opt[0] == "green":
            color = np.uint8([[[0,255,0]]])

        elif opt[0] == "yellow":
            color = np.uint8([[[0,255,255]]])    
            

        hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)

        h_c = hsv_color[0][0][0]

        lowerColor = np.array([h_c-10,100,100])
        upperColor = np.array([h_c+10,255,255])
        
        st.write("Final Image")
        final_img = st.image([])
        cv_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
        hsv_image = cv2.cvtColor(input_img,cv2.COLOR_BGR2HSV)
        mask_image = cv2.inRange(hsv_image, lowerColor, upperColor)
        final_image = cv2.bitwise_and(cv_img, cv_img, mask=mask_image)
        final_img.image(final_image)

else:
    st.write("Upload an Image")