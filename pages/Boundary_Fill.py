import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define a 2D array as an image
image = np.array([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
])

# Define the boundary fill function
def boundary_fill(image, x, y, fill_color, boundary_color):
    if image[x][y] != boundary_color and image[x][y] != fill_color:
        image[x][y] = fill_color
        if x > 0:
            boundary_fill(image, x-1, y, fill_color, boundary_color)
        if x < len(image)-1:
            boundary_fill(image, x+1, y, fill_color, boundary_color)
        if y > 0:
            boundary_fill(image, x, y-1, fill_color, boundary_color)
        if y < len(image[0])-1:
            boundary_fill(image, x, y+1, fill_color, boundary_color)

# Define the main function to run the app
def main():
    # Create a sidebar for input values
    st.sidebar.title("Boundary Fill Algorithm")
    col, row = st.sidebar.slider("Select a pixel to fill:", 0, len(image)-1, (2, 2))
    fill_color = st.sidebar.slider("Fill color:", 0, 1, 1)
    boundary_color = st.sidebar.slider("Boundary color:", 0, 1, 0)

    # Call the boundary fill function with the input values
    boundary_fill(image, row, col, fill_color, boundary_color)

    # Display the image using matplotlib
    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray_r', interpolation='none')
    ax.set_xticks(np.arange(-.5, len(image[0]), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(image), 1), minor=True)
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
    plt.title("Boundary Fill Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Display the plot using streamlit
    st.pyplot(fig)

if __name__ == '__main__':
    main()
