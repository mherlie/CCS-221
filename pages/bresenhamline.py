import streamlit as st
import matplotlib.pyplot as plt

# Bresenham's Line Algorithm
st.subheader("Bresenham's Line")
st.sidebar.subheader("Bresenham's Line Values")
x1, x2, y1, y2 = st.sidebar.slider('x1', 0, 15, 1),\
                 st.sidebar.slider('x2', 0, 15, 3),\
                 st.sidebar.slider('y1', 0, 15, 7),\
                 st.sidebar.slider('y2', 0, 15, 9)

fig, ax = plt.subplots()
def bresenham_line(x1, y1, x2, y2, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1 < x2:
        sx = 1
    else:
        sx = -1
    if y1 < y2:
        sy = 1
    else:
        sy = -1
    err = dx - dy

    while True:
        ax.plot(x1, y1, color)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err = err - dy
            x1 = x1 + sx
        if e2 < dx:
            err = err + dx
            y1 = y1 + sy
    return fig

fig = bresenham_line(x1, y1, x2, y2, 'ro')
st.pyplot(fig)
