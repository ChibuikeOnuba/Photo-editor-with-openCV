import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import cv2

from glob import glob
st.title('PHOTO EDITOR APP📷')

image = plt.imread('winner.jpg')

row = st.columns(6)
row2 = st.columns(2)
row3 = st.columns(1)
row4 = st.columns(2)

#edit functions
row[4].button('Resize') 
row[2].button('Reshape')
row[0].button('Brightness')
row[3].button('Blur')
row[1].button('Sharpeness')


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

st.write(f'{no2,2895-no1}')
st.write(image.shape)
