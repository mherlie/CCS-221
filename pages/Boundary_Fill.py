import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# initialize the 2D array
two_d_arr = np.zeros((10,10))

# function for boundary fill algorithm
def boundary_fill(x, y, fill_color, boundary_color):
    if two_d_arr[x][y] != boundary_color and two_d_arr[x][y] != fill_color:
        two_d_arr[x][y] = fill_color
        boundary_fill(x-1, y, fill_color, boundary_color)
        boundary_fill(x+1, y, fill_color, boundary_color)
        boundary_fill(x, y-1, fill_color, boundary_color)
        boundary_fill(x, y+1, fill_color, boundary_color)

# Streamlit UI
st.title("Boundary Fill Algorithm")
st.write("Click on any cell to fill with the selected color.")
fill_color = st.color_picker("Select fill color", "#f00")
boundary_color = st.color_picker("Select boundary color", "#000")

fig, ax = plt.subplots()

# plot the initial array
ax.imshow(two_d_arr, interpolation='none', cmap='gray_r')

# event handler for mouse click
def onclick(event):
    if event.inaxes:
        x, y = int(event.xdata), int(event.ydata)
        boundary_fill(x, y, fill_color, boundary_color)
        ax.imshow(two_d_arr, interpolation='none', cmap='gray_r')
        fig.canvas.draw_idle()

# attach the event handler to the plot
cid = fig.canvas.mpl_connect('button_press_event', onclick)

st.pyplot(fig)
