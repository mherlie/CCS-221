import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Boundary Fill Algorithm")

# Initial 2D array
two_d_arr = np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]])

# Define boundary fill function
def boundary_fill(x, y, fill_color, boundary_color):
    if two_d_arr[x][y] != boundary_color and two_d_arr[x][y] != fill_color:
        two_d_arr[x][y] = fill_color
        if x > 0:
            boundary_fill(x-1, y, fill_color, boundary_color)
        if y > 0:
            boundary_fill(x, y-1, fill_color, boundary_color)
        if x < len(two_d_arr)-1:
            boundary_fill(x+1, y, fill_color, boundary_color)
        if y < len(two_d_arr)-1:
            boundary_fill(x, y+1, fill_color, boundary_color)

# Streamlit UI
x_boundary, y_boundary = st.slider("Select starting point for boundary fill", 0, 2, (1, 1))
fill_color = st.slider("Select fill color", 0, 1, 1)
boundary_color = st.slider("Select boundary color", 0, 1, 0)

# Run boundary fill function on click
if st.button("Apply Boundary Fill"):
    boundary_fill(x_boundary, y_boundary, fill_color, boundary_color)
    fig = plt.imshow(two_d_arr, interpolation='none', cmap='plasma')
    fig.set_clim([0, 1])
    plt.colorbar()
    st.pyplot()
