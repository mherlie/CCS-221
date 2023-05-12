import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
from PIL import Image

tf.compat.v1.disable_eager_execution()

st.title("3D Object Transformation")

def _plt_basic_object_(points):
    tri = Delaunay(points).convex_hull
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],
                        triangles=tri,
                        shade=True, cmap=cm.rainbow, lw=0.5)

    ax.set_xlim3d(-5,5) 
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5) 
    
    return fig

def rotate_obj(points, angle):
    rotation_matrix = tf.stack([
                                [tf.cos(angle), tf.sin(angle), 0],
                                [-tf.sin(angle), tf.cos(angle), 0],
                                [0, 0, 1]
                                ])
    rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))

    return rotate_object

#Cube
def _cube_(bottom_lower=(0, 0, 0), side_length=5):
    bottom_lower = np.array(bottom_lower)

    points = np.stack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0 , side_length],
        bottom_lower
    ])

    return points

init_cube_ = _cube_(side_length=3)
points = tf.constant(init_cube_, dtype=tf.float32)

cube_fig = _plt_basic_object_(init_cube_)
st.pyplot(cube_fig)

def translate_obj(points, amount):
    return tf.add (points, amount)

translation_amount =tf.constant([1, 2, 2], dtype=tf.float32) 
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
    translated_cube_ = session.run(translated_object)

translated_cube_fig = _plt_basic_object_(translated_cube_)
st.pyplot(translated_cube_fig)

# Add angle input to sidebar
angle = st.sidebar.number_input("Angle (degrees):", value=75, step=1)
angle_rad = np.deg2rad(angle)

with tf.compat.v1.Session() as session:
    rotated_object = session.run(rotate_obj(init_cube_, angle_rad))

rotated_cube_fig = _plt_basic_object_(rotated_object)
st.pyplot(rotated_cube_fig)

