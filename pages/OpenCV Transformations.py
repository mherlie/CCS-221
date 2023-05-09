import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

def translation(img_, rows, cols):
    img_translated = np.float32([[1, 0, 100],
                                [0, 1, 50],
                                [0, 0, 1]])
    img_translated = cv2.warpPerspective(img_, img_translated, (cols, rows))
    return img_translated

def rotation(img_, rows, cols):
    angle = np.radians(10)
    img_rotated = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                            [np.sin(angle), np.cos(angle), 0],
                            [0, 0, 1]])
    img_rotated = cv2.warpPerspective(img_, img_rotated, (cols, rows))
    return img_rotated

def scaling(img_, rows, cols):
    img_scaled = np.float32(([1.5, 0, 0],
                             [0, 1.8, 0],
                             [0, 0, 1]))
    img_scaled = cv2.warpPerspective(img_, img_scaled, (int(cols*2), int(rows*2)))
    return img_scaled

def reflection(img_, rows, cols):
    img_reflected = np.float32([[-1, 0, cols],
                                [0, 1, 0],
                                [0, 0, 1]])
    img_reflected = cv2.warpPerspective(img_, img_reflected, (cols, rows))
    return img_reflected

def shear(img_, rows, cols):
    img_sheared = np.float32([[1, 0.5, 0],
                              [0, 1, 0],
                              [0, 0, 1]])
    img_sheared = cv2.warpPerspective(img_, img_sheared, (int(cols*1.5), int(rows*1.5)))
    return img_sheared

def apply_transform(img_, transform_fn):
    rows, cols, dims = img_.shape
    img_transformed = transform_fn(img_, rows, cols)
    return img_transformed

def process_image(file_name, transform_fn):
    img_test = cv2.imread(file_name)
    img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
    img_transformed = apply_transform(img_test, transform_fn)
    return img_transformed

def main():
    st.title("Image Transformation")

    file_name = st.text_input("Input File Name:")
    transform_type = st.selectbox("Select Transformation", ["Translation", "Rotation", "Scale", "Reflect", "Shear"])
    transform_fn = None

    if transform_type == "Translation":
        transform_fn = translation
    elif transform_type == "Rotation":
        transform_fn = rotation
    elif transform_type == "Scale":
        transform_fn = scaling
    elif transform_type == "Reflect":
        transform_fn = reflection
    elif transform_type == "Shear":
        transform_fn = shear

    if file_name and transform_fn:
        img_transformed = process_image(file_name, transform_fn)

        st.image(img_transformed, use_column_width=True)
    else:
        st.warning("Please enter a file name and select a transformation type.")

if __name__ == "__main__":
    main()
