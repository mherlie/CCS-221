import streamlit as st
import matplotlib.pyplot as plt


#DDA_LINE algorithm
st.subheader("DDA-LINE")
st.sidebar.subheader("DDA-LINE values")
x1_DDALINE, x2_DDALINE, y1_DDALINE, y2_DDALINE = st.sidebar.slider('x1 for DDALINE', 0, 15, 1),\
                                                st.sidebar.slider('x2 for DDALINE', 0, 15, 3),\
                                                st.sidebar.slider('y1 for DDALINE', 0, 15, 7),\
                                                st.sidebar.slider('y2 for DDALINE', 0, 15, 9)

fig3 = plt.figure()
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
        plt.plot(int(x1), int(y1), color)
        plt.plot(int(xMidDDA), int(yMidDDA), 'b.')
    return fig3

fig3 = DDALine (x1_DDALINE, x2_DDALINE, y1_DDALINE, y2_DDALINE, 'ro')
st.pyplot(fig3)
