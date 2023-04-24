import streamlit as st
import matplotlib.pyplot as plt

# DDALine algorithm
st.subheader("DDA Line")
st.sidebar.subheader("DDA Line Values")
x1_DDALine, x2_DDALine, y1_DDALine, y2_DDALine = st.sidebar.slider('x1 for DDALine', 0, 15, 1),\
                                                st.sidebar.slider('x2 for DDALine', 0, 15, 3),\
                                                st.sidebar.slider('y1 for DDALine', 0, 15, 7),\
                                                st.sidebar.slider('y2 for DDALine', 0, 15, 9)

fig3, ax = plt.subplots()
def DDALine (x1, y1, x2, y2, color):
   
    dx = x2 - x1
    dy = y2 - y1

    xMidDDA = (x1 + x2)/2
    yMidDDA = (y1 + y2)/2

    # calculate steps required for generating pixels
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # calculate increment in x and y for each step
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    for i in range(0, int(steps + 1)):
        #Draw pixels 
        x1 += Xinc
        y1 += Yinc
        ax.plot(int(x1), int(y1), color)
        ax.plot(int(xMidDDA), int(yMidDDA), 'b.')
    return fig3

fig3 = DDALine(x1_DDALine, y1_DDALine, x2_DDALine, y2_DDALine, 'ro')
st.pyplot(fig3)
