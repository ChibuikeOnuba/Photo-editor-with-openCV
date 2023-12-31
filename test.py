import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2

image = st.file_uploader('upload image', type=['jpg', 'png', 'jepg'])
if image:
    pi = Image.open(image)


ig = cv2.imread('winner.jpg')
ig = cv2.cvtColor(ig, cv2.COLOR_RGB2BGR)
ig.shape[0]

img = plt.imread('winner.jpg')
img.shape


if image:
    st.image(image)
    image.size

test_slider = st.slider('test', min_value=-25, max_value=-1, value=-10)
 
kernel_bright = np.ones((3,3), np.float32)/(0-test_slider)    
show = cv2.filter2D(ig, -1, kernel_bright)


   
st.image(show)