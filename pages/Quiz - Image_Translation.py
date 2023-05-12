import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.title("Image Translation")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
if uploaded_file is not None:
    img_ = Image.open(uploaded_file)
    img_ = np.array(img_)
    st.image(img_, caption="Uploaded Image", use_column_width=True)

    rows, cols, dims = img_.shape

    def translation(img_, rows, cols, Bx, By):
        img_translated = np.float32([[1, 0, Bx], [0, 1, By], [0, 0, 1]])
        img_translated = cv2.warpPerspective(img_, img_translated, (cols, rows))

        return img_translated

    num_img = st.sidebar.number_input("Enter number of images:", min_value=1, value=1, step=1)

    for num_test in range(num_img):
        st.sidebar.markdown(f"### Image {num_test+1}")

        Bx_old = st.sidebar.number_input(f"Bx_old (Image {num_test+1}):", value=0, step=1)
        By_old = st.sidebar.number_input(f"By_old (Image {num_test+1}):", value=0, step=1)

        Tx = st.sidebar.number_input(f"Tx (Image {num_test+1}):", value=0, step=1)
        Ty = st.sidebar.number_input(f"Ty (Image {num_test+1}):", value=0, step=1)

        Bx_new = Bx_old + Tx
        By_new = By_old + Ty

        old_img = translation(img_, rows, cols, Bx_old, By_old)
        new_img = translation(img_, rows, cols, Bx_new, By_new)

        col1, col2 = st.beta_columns(2)
        col1.image(old_img, caption=f"Original Image {num_test+1} (Bx_old={Bx_old}, By_old={By_old})", use_column_width=True)
        col2.image(new_img, caption=f"Translated Image {num_test+1} (Bx_new={Bx_new}, By_new={By_new})", use_column_width=True)
