import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Flood Fill")

st.header("Flood Fill Algorithm")

# Initial image
img = np.array([[1,0,1], 
                [0,1,0],
                [1,0,1]])

# Function to perform the flood fill
def flood_fill(x, y, target_color, replacement_color):
    if img[x][y] == target_color:
        img[x][y] = replacement_color
        if x > 0:
            flood_fill(x-1, y, target_color, replacement_color)  # Check the pixel to the left
        if x < len(img)-1:
            flood_fill(x+1, y, target_color, replacement_color)  # Check the pixel to the right
        if y > 0:
            flood_fill(x, y-1, target_color, replacement_color)  # Check the pixel above
        if y < len(img[x])-1:
            flood_fill(x, y+1, target_color, replacement_color)  # Check the pixel below

# Get the user input
x, y, target_color, replacement_color = st.beta_columns(4)
x = x.slider("X coordinate (0-2)", 0, 2, 0)
y = y.slider("Y coordinate (0-2)", 0, 2, 0)
target_color = target_color.selectbox("Target color", [0, 1])
replacement_color = replacement_color.selectbox("Replacement color", [0, 1])

# Perform the flood fill
flood_fill(x, y, target_color, replacement_color)

# Display the updated image
fig, ax = plt.subplots()
ax.imshow(img, interpolation="none", cmap="plasma")
ax.set_title("Updated Image")
ax.set_xticks(np.arange(len(img[0])))
ax.set_yticks(np.arange(len(img)))
ax.set_xticklabels(np.arange(len(img[0])))
ax.set_yticklabels(np.arange(len(img)))
plt.grid()
st.pyplot(fig)
