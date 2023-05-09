import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to perform boundary fill
def boundary_fill(x, y, fill_color, boundary_color, img):
    if img[x][y] == boundary_color:
        return
    if img[x][y] != fill_color:
        img[x][y] = fill_color
        boundary_fill(x+1, y, fill_color, boundary_color, img)
        boundary_fill(x-1, y, fill_color, boundary_color, img)
        boundary_fill(x, y+1, fill_color, boundary_color, img)
        boundary_fill(x, y-1, fill_color, boundary_color, img)

# Create a 2D array as the initial image
two_d_arr = np.array([[1, 0, 1],
                      [0, 0, 0],
                      [1, 0, 1]])

# Set the default values for user inputs
column = st.sidebar.number_input("Column (0-2):", min_value=0, max_value=2, value=0)
row = st.sidebar.number_input("Row (0-2):", min_value=0, max_value=2, value=0)
fill_color = st.sidebar.number_input("Fill color:", min_value=0, max_value=1, value=1)

# Set the boundary color as the complement of the fill color
boundary_color = 1 if fill_color == 0 else 0

# Perform boundary fill
boundary_fill(row, column, fill_color, boundary_color, two_d_arr)

# Display the resulting image
fig, ax = plt.subplots()
ax.imshow(two_d_arr, interpolation='none', cmap='plasma')
ax.axis('off')
st.pyplot(fig)
