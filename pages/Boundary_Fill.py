import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def flood_fill(matrix, start_pos, target_color, replacement_color):
    rows, cols = matrix.shape
    stack = [start_pos]
    visited = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in visited or matrix[x, y] != target_color:
            continue

        matrix[x, y] = replacement_color
        visited.add((x, y))

        # Check top
        if x > 0:
            stack.append((x - 1, y))
        # Check left
        if y > 0:
            stack.append((x, y - 1))
        # Check right
        if y < cols - 1:
            stack.append((x, y + 1))
        # Check bottom
        if x < rows - 1:
            stack.append((x + 1, y))

    return matrix

# Streamlit app
def main():
    st.title("Boundary-fill / Flood-fill Algorithm")

    # Create a default example matrix
    default_matrix = np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    # Display the original matrix
    st.subheader("Original Matrix")
    fig, ax = plt.subplots()
    ax.imshow(default_matrix, interpolation='none', cmap='plasma')
    st.pyplot(fig)

    # Get user inputs
    start_pos = st.text_input("Enter the starting position (format: row, column)", "0, 0")
    target_color = st.number_input("Enter the target color", value=1)
    replacement_color = st.number_input("Enter the replacement color", value=2)

    # Process user inputs
    try:
        row, col = map(int, start_pos.strip().split(","))
        filled_matrix = flood_fill(default_matrix.copy(), (row, col), target_color, replacement_color)

        # Display the filled matrix
        st.subheader("Filled Matrix")
        fig, ax = plt.subplots()
        ax.imshow(filled_matrix, interpolation='none', cmap='plasma')
        st.pyplot(fig)
    except ValueError:
        st.error("Invalid input for starting position. Please enter row and column as integers separated by a comma.")

if __name__ == "__main__":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()
