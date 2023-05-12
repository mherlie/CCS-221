import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

st.title("Image Transformations")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
if uploaded_file is not None:
    img_ = Image.open(uploaded_file)
    img_ = np.array(img_)
    st.image(img_, caption="Uploaded Image", use_column_width=True)

    rows, cols, dims = img_.shape

    st.sidebar.title("Choose transformation")
    user_input = st.sidebar.selectbox("",
        (
            "Select...",
            "Translation",
            "Rotation",
            "Scale",
            "Reflect",
            "Flip",
            "Shear"
        ),
    )

    def translation(img_, rows, cols):
        img_translated = np.float32([[1, 0, 100], [0, 1, 50], [0, 0, 1]])
        img_translated = cv2.warpPerspective(img_, img_translated, (cols, rows))

        return img_translated

    def rotation(img_, rows, cols):
        angle = np.radians(10)
        img_rotated = cv2.getRotationMatrix2D((cols/2,rows/2,),90,1)
        img_rotated = cv2.warpAffine(img_,img_rotated,(cols,rows))

        return img_rotated

    def scaling(img_, rows, cols):
        img_scaled = np.float32(([1.5, 0, 0], [0, 1.8, 0], [0, 0, 1]))
        img_scaled = cv2.warpPerspective(img_, img_scaled, (cols*2, rows*2))

        return img_scaled

    def reflection(img_, rows, cols):
        img_reflected = np.float32([[-1, 0, cols], [0, 1, 0], [0, 0, 1]])
        img_reflected = cv2.warpPerspective(img_, img_reflected, (int(cols), int(rows)))

        return img_reflected

    def flip(img_, rows, cols):
        img_flipped = cv2.flip(img_, 0)

        return img_flipped

    def shear(img_, rows, cols):
        img_sheared = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])
        img_sheared = cv2.warpPerspective(img_, img_sheared, (int(cols*1.5), int(rows*1.5)))

        return img_sheared

    def user_choices(user_input, img_):
        if user_input == "Translation":
            img_transformed = translation(img_, rows, cols)

        elif user_input == "Rotation":
            img_transformed = rotation(img_, rows, cols)

        elif user_input == "Scale":
            img_transformed = scaling(img_, rows, cols)

        elif user_input == "Reflect":
            img_transformed = reflection(img_, rows, cols)

        elif user_input == "Flip":
            img_transformed = flip(img_, rows, cols)

        elif user_input == "Shear":
            img_transformed = shear(img_, rows, cols)

        return img_transformed

    if user_input != "Select...":
        imgs_transformed = user_choices(user_input, img_)

        st.image(imgs_transformed, caption="Transformed Image", use_column_width=True)
