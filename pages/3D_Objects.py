import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

tf.compat.v1.disable_eager_execution()

@st.cache
def _plt_basic_object_(points):
    tri = Delaunay(points).convex_hull
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(
        points[:, 0], points[:, 1], points[:, 2],
        triangles=tri,
        shade=True, cmap=cm.rainbow, lw=0.5
    )
    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5)
    return fig

@st.cache
def rotate_obj(points, angle):
    rotation_matrix = tf.stack([
        [tf.cos(angle), tf.sin(angle), 0],
        [-tf.sin(angle), tf.cos(angle), 0],
        [0, 0, 1]
    ])
    rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
    with tf.compat.v1.Session() as session:
        rotated_object = session.run(rotate_object)
    return rotated_object

def translate_obj(points, amount):
    return tf.add(points, amount)

def main():
    st.title("3D Object Manipulation")

    object_type = st.selectbox("Select an object type", ("Cube", "Rectangle", "Right Triangle", "Triangle Prism"))

    if object_type == "Cube":
        init_cube = _cube_(side_length=3)
        points = tf.constant(init_cube, dtype=tf.float32)

    elif object_type == "Rectangle":
        init_rectangle = rectangle_obj(side_length=3)
        points = tf.constant(init_rectangle, dtype=tf.float32)

    elif object_type == "Right Triangle":
        init_right_triangle = right_triangle_obj(side_length=5)
        points = tf.constant(init_right_triangle, dtype=tf.float32)

    else:
        init_tri_prism = triangle_prism_obj(side_length=4)
        points = tf.constant(init_tri_prism, dtype=tf.float32)

    st.subheader("Original Object")
    fig = _plt_basic_object_(points)
    st.pyplot(fig)

    translate_amount = st.text_input("Enter translation amount (e.g., 1,2,2)")
    translate_amount = np.array([float(x) for x in translate_amount.split(",")])

    translated_object = translate_obj(points, tf.constant(translate_amount, dtype=tf.float32))
    with tf.compat.v1.Session() as session:
        translated_object = session.run(translated_object)

    st.subheader("Translated Object")
    fig = _plt_basic_object_(translated_object)
    st.pyplot(fig)

    rotate_angle = st.number_input("Enter rotation angle", value=75.0)
    rotated_object = rotate_obj(points, rotate_angle)

    st.subheader("Rotated Object")
    fig = _plt_basic_object_(rotated_object)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
