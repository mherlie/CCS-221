import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header("Boundary Fill Algorithm")

# Define the 2D array with dimensions 10x10
two_d_arr = np.zeros((10, 10))

# Define the boundary coordinates
boundary_coords = [(3, 3), (3, 4), (4, 4), (4, 5), (5, 5), (5, 4), (6, 4), (6, 3), (5, 3), (5, 2), (4, 2), (4, 3)]

# Define the fill color
fill_color = 1

# Define the boundary color
boundary_color = 2

# Function to perform the boundary fill algorithm
def boundary_fill(x, y, fill_color, boundary_color):
    if x < 0 or y < 0 or x >= 10 or y >= 10:
        return
    if two_d_arr[x][y] == boundary_color or two_d_arr[x][y] == fill_color:
        return
    two_d_arr[x][y] = fill_color
    boundary_fill(x+1, y, fill_color, boundary_color)
    boundary_fill(x-1, y, fill_color, boundary_color)
    boundary_fill(x, y+1, fill_color, boundary_color)
    boundary_fill(x, y-1, fill_color, boundary_color)

# Perform the boundary fill algorithm for each boundary coordinate
for coord in boundary_coords:
    boundary_fill(coord[0], coord[1], fill_color, boundary_color)

# Plot the final 2D array
fig, ax = plt.subplots()
ax.imshow(two_d_arr, cmap='binary', interpolation='nearest')
ax.set_xticks(np.arange(-0.5, 10, 1))
ax.set_yticks(np.arange(-0.5, 10, 1))
ax.grid(color='black', linestyle='-', linewidth=1)
plt.show()

# Display the plot in Streamlit
st.pyplot(fig)
