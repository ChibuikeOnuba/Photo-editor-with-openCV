import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from PIL.ImageFilter import *
import matplotlib.pylab as plt
import cv2
from glob import glob


#BACKGROUND FORMAT
st.title('PHOTO EDITOR APP📷')


image = st.file_uploader('Upload your image', type=['jpg', 'png', 'jepg'])

if image:
    img = Image.open(image)
    #display image
    edited = st.empty()
      
    #specify row divisions
    row0 = st.columns(1) 
    row1 = st.columns(2)
    row2 = st.columns(2)

    #adjust display
    adjust = row1[0].selectbox(options=['None', 'Brightness', 'Blur', 'Sharpness', 'Contour'], label='Adjust')
    if adjust != 'None':
        row2[0].slider(adjust, min_value=100, max_value=200, value=10)
        
    #adjust filters
    filters = row1[1].selectbox(options=['None', 'BW', 'Vivid', 'Clone', 'Breeze'], label='filters')
    if filters != 'None':
        row2[1].slider(filters, min_value=100, max_value=200, value=10)

    st.markdown('Resize')
    width = st.slider('width', value=img.size[0], min_value=500, max_value=img.size[0])
    length = st.slider('length', value=img.size[1], min_value=500, max_value=img.size[1])
    degree = st.slider('Degree', step=10,max_value=180, min_value=-180, value=0)
    
    edited.image(img.resize((width, length)).rotate(degree))
    st.button('Reset', type='primary')

    
    
    
    #FUNCTIONLITY
    
    
    '''
    row2 = st.columns(2)
    row = st.columns(6)
    row3 = st.columns(1) 
    row4 = st.columns(2)

    #edit functions
    row[4].button('Resize') 
    row[2].button('Reshape')
    row[0].button('Brightness')
    row[3].button('Blur')
    row[1].button('Sharpeness')

    st.d
    
    row2[0].write('Original Image')
    row2[0].image(image)

    row2[1].write('Edited Image')
    value = row3[0].slider(min_value=-20, max_value=20, label='Brightness')
    kernel_bright = np.ones((3,3), np.float32)/(20-value)    
    img = cv2.filter2D(image, -1, kernel_bright)

    value2 = row3[0].slider(min_value=1, max_value=10, label='Sharpen')
    kernel_sharpen = np.array([[ 0, -1, 0 ],
                            [ -1, 5, -1],
                            [ 0, -1, 0 ]])*value2
    img = cv2.filter2D(img, -1, kernel_sharpen)
    col3 = row4[1].columns(2)
    no1 = col3[0].slider(min_value=90, max_value=image.shape[1], label='border-bottom')
    no2 = col3[1].slider(min_value=2, max_value=900, label='border-left')
    no3 = col3[0].slider(min_value=2, max_value=900, label='border-top')
    no4 = col3[1].slider(min_value=2, max_value=900, label='border-right')

    img = row2[1].image(img[no2:2895-no1,no3:2896-no4])
    '''

    
