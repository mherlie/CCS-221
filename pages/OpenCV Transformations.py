import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

img_ = cv2.imread(".jpg")
img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
rows, cols, dims = img_.shape

def translation(img_, rows, cols):
    img_translated = np.float32([[1, 0, 100],
                                 [0, 1, 50],
                                 [0, 0, 1]])
    img_translated = cv2.warpPerspective(img_, img_translated, (cols, rows))
    return img_translated
  
def rotation(img_, rows, cols):
    angle = np.radians(10)
    img_rotated = cv2.getRotationMatrix2D((cols/2,rows/2,),90,1)
    img_rotated = cv2.warpAffine(img_,img_rotated,(cols,rows))
    return img_rotated

def scaling(img_, rows, cols):
    img_scaled = np.float32(([1.5, 0, 0],
                             [0, 1.8, 0],
                             [0, 0, 1]))
    img_scaled = cv2.warpPerspective(img_, img_scaled,(cols*2,rows*2))
    return img_scaled

def reflection(img_, rows, cols):
    img_reflected = np.float32(([1, 0, 0],
                                [0, -1, rows],
                                [0, 0, 1]))
    img_reflected = cv2.warpPerspective(img_, img_reflected, (int(cols), int(rows)))
    return img_reflected

def flip(img_, rows, cols):
    img_flipped = cv2.flip(img_, 0)
    return img_flipped

def shear(img_, rows, cols):
    img_sheared = np.float32([[1, 0, 0],
                              [0.5, 1, 0 ],
                              [0, 0, 1]])
    img_sheared = cv2.warpPerspective(img_, img_sheared, (int(cols*1.5), int(rows*1.5)))
    return img_sheared

user_input = st.sidebar.selectbox("Select an operation",
    ["Translation", "Rotation", "Scaling", "Reflection", "Flip", "Shear"])

if user_input == "Translation":
    img_translated = translation(img_, rows, cols)
    st.image(img_translated, caption="Translated Image", use_column_width=True)
  
if user_input == "Rotation":
    img_rotated = rotation(img_, rows, cols)
    st.image(img_rotated, caption="Rotated Image", use_column_width=True)

if user_input == "Scaling":
    img_scaled = scaling(img_, rows, cols)
    st.image(img_scaled, caption="Scaled Image", use_column_width=True)

if user_input == "Reflection":
    img_reflected = reflection(img_, rows, cols)
    st.image(img_reflected, caption="Reflected Image", use_column_width=True)

if user_input == "Flip":
    img_flipped = flip(img_, rows, cols)
    st.image(img_flipped, caption="Flipped Image", use_column_width=True)

if user_input == "Shear":
    img_sheared = shear(img_, rows, cols)
    st.image(img_sheared, caption="Sheared Image", use_column_width=True)
