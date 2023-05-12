import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

tf.compat.v1.disable_eager_execution()


def main():
    st.title("3D Object Visualization")
    
    object_type = st.selectbox("Select the 3D object", ("Cube", "Rectangle", "Right Triangle", "Triangle Prism"))

    side_length = st.slider("Side length", 1, 10, 5)
    angle = st.slider("Rotation angle", 0, 360, 0)
    translation = st.slider("Translation amount", 0, 10, 1)

    if object_type == "Cube":
        points = _cube_(side_length=side_length)
    elif object_type == "Rectangle":
        points = rectangle_obj(side_length=side_length)
    elif object_type == "Right Triangle":
        points = right_triangle_obj(side_length=side_length)
    else:
        points = triangle_prism_obj(side_length=side_length)

    points = tf.constant(points, dtype=tf.float32)

    rotated_points = rotate_obj(points, angle)
    translated_points = translate_obj(points, tf.constant([translation, translation, translation], dtype=tf.float32))

    with tf.compat.v1.Session() as session:
        rotated_points = session.run(rotated_points)
        translated_points = session.run(translated_points)

    st.subheader("Original object")
    _plt_basic_object_(points)
    st.pyplot(plt)

    st.subheader("Rotated object")
    _plt_basic_object_(rotated_points)
    st.pyplot(plt)

    st.subheader("Translated object")
    _plt_basic_object_(translated_points)
    st.pyplot(plt)


if __name__ == "__main__":
    main()
