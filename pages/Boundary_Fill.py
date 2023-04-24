import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define the boundary fill algorithm
def boundary_fill(x, y, fill_color, boundary_color, img):
    if img[x][y] != boundary_color and img[x][y] != fill_color:
        img[x][y] = fill_color
        boundary_fill(x+1, y, fill_color, boundary_color, img)
        boundary_fill(x-1, y, fill_color, boundary_color, img)
        boundary_fill(x, y+1, fill_color, boundary_color, img)
        boundary_fill(x, y-1, fill_color, boundary_color, img)

# Define the main function
def main():
    # Define the initial image array
    img = np.array([[1, 0, 1],
                    [0, 0, 0],
                    [1, 0, 1]])

    # Define the default fill and boundary colors
    fill_color = 2
    boundary_color = 1

    # Get the user inputs for the row and column indices
    row = st.number_input("Row (0-2): ", 0, 2, 0)
    col = st.number_input("Column (0-2): ", 0, 2, 0)

    # Set the fill color for the selected pixel
    img_copy = np.copy(img)
    boundary_fill(row, col, fill_color, boundary_color, img_copy)

    # Plot the initial and modified images
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
    ax1.imshow(img, cmap='gray')
    ax1.set_title("Original Image")
    ax1.axis('off')
    ax2.imshow(img_copy, cmap='gray')
    ax2.set_title("Boundary Fill Image")
    ax2.axis('off')

    # Show the plot
    st.pyplot(fig)

if __name__ == '__main__':
    main()
