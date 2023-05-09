import streamlit as st
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def translation(img, x, y):
    rows, cols, _ = img.shape
    M = np.float32([[1, 0, x], [0, 1, y]])
    translated = cv2.warpAffine(img, M, (cols, rows))
    return translated


def rotation(img, angle):
    rows, cols, _ = img.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotated = cv2.warpAffine(img, M, (cols, rows))
    return rotated


def scaling(img, fx, fy):
    rows, cols, _ = img.shape
    M = np.float32([[fx, 0, 0], [0, fy, 0], [0, 0, 1]])
    scaled = cv2.warpPerspective(img, M, (cols, rows))
    return scaled


def reflection(img, axis):
    rows, cols, _ = img.shape
    if axis == 0:
        M = np.float32([[-1, 0, cols], [0, 1, 0], [0, 0, 1]])
    elif axis == 1:
        M = np.float32([[1, 0, 0], [0, -1, rows], [0, 0, 1]])
    reflected = cv2.warpPerspective(img, M, (cols, rows))
    return reflected


def flip(img, axis):
    flipped = cv2.flip(img, axis)
    return flipped


def shear(img, factor):
    rows, cols, _ = img.shape
    M = np.float32([[1, factor, 0], [0, 1, 0], [0, 0, 1]])
    sheared = cv2.warpPerspective(img, M, (int(cols+factor*rows), rows))
    return sheared


def apply_transform(img, transform, params):
    if transform == 'Translation':
        x, y = params
        transformed = translation(img, x, y)
    elif transform == 'Rotation':
        angle = params
        transformed = rotation(img, angle)
    elif transform == 'Scaling':
        fx, fy = params
        transformed = scaling(img, fx, fy)
    elif transform == 'Reflection':
        axis = params
        transformed = reflection(img, axis)
    elif transform == 'Flip':
        axis = params
        transformed = flip(img, axis)
    elif transform == 'Shear':
        factor = params
        transformed = shear(img, factor)
    return transformed


def main():
    st.title("Image Transformations")
    img_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if img_file is not None:
        img = np.array(Image.open(img_file))
        st.image(img, caption="Original Image", use_column_width=True)

        transform = st.selectbox("Select a transformation", ["Translation", "Rotation", "Scaling", "Reflection", "Flip", "Shear"])

        if transform == 'Translation':
            x = st.slider("x", -img.shape[1], img.shape[1], 
