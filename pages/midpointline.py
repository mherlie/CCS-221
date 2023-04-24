import streamlit as st
import matplotlib.pyplot as plt

st.title("Midpoint Line")

# Midpoint Line Algorithm
st.subheader("Midpoint Line Algorithm")
st.sidebar.subheader("Midpoint Line Algorithm values")
x1, x2, y1, y2 = st.sidebar.slider('x1', 0, 15, 1),\
                 st.sidebar.slider('x2', 0, 15, 3),\
                 st.sidebar.slider('y1', 0, 15, 7),\
                 st.sidebar.slider('y2', 0, 15, 9)

fig, ax = plt.subplots()
def midpoint_line(x1, y1, x2, y2, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            ax.plot(x, y, color)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            ax.plot(x, y, color)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    ax.plot(x, y, color)
    return fig

fig = midpoint_line(x1, y1, x2, y2, 'ro')
st.pyplot(fig)
