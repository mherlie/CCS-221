import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pages.Activity_1 as activity1

def main():
    st.title("Midterm Exam in CCS221")
    
    st.sidebar.header("Line Algorithm Parameters")
    _task1_x0, _task1_y0, _task1_x1, _task1_y1 = st.sidebar.slider('Starting X', 1, 1000), \
                     st.sidebar.slider('Starting Y', 1, 1000), \
                     st.sidebar.slider('Ending X', 1, 1000, 100), \
                     st.sidebar.slider('Ending Y', 1, 1000, 100)

    st.sidebar.header("Change Pixel Hue Parameters")
    _task2_x, _task2_y, _task2_hue = st.sidebar.slider('X coordinate', 0, 2, 0, 1), \
                                     st.sidebar.slider('Y coordinate', 0, 2, 0, 1), \
                                     st.sidebar.slider('Hue', 0, 100, 50)
                                    
    st.sidebar.header("Image transformations")
    _task3_filepath = st.sidebar.text_input('Enter file path: ', 'Exercises/images/img1.webp')
    _task3_transformations = st.sidebar.multiselect('Select tranformations to apply: ', \
                            ['translate', 'rotate', 'reflect', 'scale', 'shear'])

    if 'translate' in _task3_transformations:
        _task3_translationx = st.sidebar.slider('X Translation', 0, 1000)
        _task3_translationy = st.sidebar.slider('Y Translation', 0, 1000)
        
    if 'reflect' in _task3_transformations:
        _task3_reflectionx = st.sidebar.checkbox('Reflect along x axis')
        _task3_reflectiony = st.sidebar.checkbox('Reflect along y axis')
        
    if 'rotate' in _task3_transformations:
        _task3_rotation = st.sidebar.slider('Rotation', -360, 360, 0)
        
    if 'scale' in _task3_transformations:
        _task3_scale = st.sidebar.slider('Scale', 0, 5, 1)
        
    if 'shear' in _task3_transformations:
        _task3_shearx = st.sidebar.slider('X Shear', 0, 5, 1)
        _task3_sheary = st.sidebar.slider('Y Shear', 0, 5, 1)
                
    st.header("Task 1")
    st.subheader("DDA Line Algorithm")
    st.pyplot(task1.DDALine(_task1_x0, _task1_y0, _task1_x1, _task1_y1, 'ro'))
    st.subheader("Bresenham's Line Algorithm")
    st.pyplot(task1.Bres(_task1_x0, _task1_y0, _task1_x1, _task1_y1, 'ro'))
    st.subheader("Midpoint Line Algorithm")
    st.pyplot(task1.midpoint(_task1_x0, _task1_y0, _task1_x1, _task1_y1, 'ro'))
    
    
