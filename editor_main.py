import cv2
import streamlit as st
import numpy as np
import os

def main():
    st.title("LB EDITOR✨")
    
    #style header
    def fancy_header(text, font_size=20):
        res = f'<span style="color:#3030FF; font-size: {font_size}px;"><b>{text}</b></span>'
        st.markdown(res, unsafe_allow_html=True )
        
    #image uploader
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        processed_image = image.copy()   
        
        #display original image & create an empty container for edited image
        row1 = st.columns(2)
        row1[0].image(image, caption="Original Image")
        edited = row1[1].empty()
        
        #select filter
        fancy_header('Select filter')
        filter = st.selectbox('Filter',label_visibility='collapsed', options=['None', 'Gray'])
        if filter == 'Gray':
            processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            
        # Display adjust options
        fancy_header('Adjust')
        row = st.columns(4)
        blur_option = row[0].checkbox("Blur")
        contrast_option = row[1].checkbox("Contrast")
        brightness_option = row[2].checkbox("Brightness")
        sharpen_option = row[3].checkbox('Sharpen')
        
        #blur image if blur is selected
        if blur_option:
            blur_radius = st.slider(f'Adjust Blur', min_value=1, max_value=27, value=5, step=2)
            processed_image = cv2.GaussianBlur(processed_image, (blur_radius, blur_radius), 0)
            edited.image(processed_image)
        else:
            edited.image(image)
            
        # adjust contrast if selected
        if contrast_option:
            contrast = st.slider("Contrast", -100, 100, 0)
            processed_image = cv2.convertScaleAbs(processed_image, beta=0-contrast)
            edited.image(processed_image)
            
        # adjust brightness image if selected
        if brightness_option:
            brightness = st.slider("Brightness", -100, 100, 0)
            processed_image = cv2.convertScaleAbs(processed_image, alpha=((brightness+95) / 100.0))
            edited.image(processed_image)
            
        # adjust sharpeness if selected
        if  sharpen_option:
            sharpen = st.slider("Sharpen", 0.1, 10.0, 1.0,0.1)
            kernel_sharpen = np.array([[ 0, -1, 0 ],
                                [ -1, 5, -1],
                                [ 0, -1, 0 ]])*sharpen
            processed_image = cv2.filter2D(processed_image, -1, kernel_sharpen)
            edited.image(processed_image)
            
        # Cropping and rotation
        fancy_header("Crop & Rotate")
        row = st.columns(2)
        x = row[0].slider("X-coordinate", 0, processed_image.shape[1], 0)
        y = row[1].slider("Y-coordinate", 0, processed_image.shape[0], 0)
        width = row[0].slider("Width", 1, processed_image.shape[1], processed_image.shape[1])
        height = row[1].slider("Height", 1, processed_image.shape[0], processed_image.shape[0])
        
        rotation_angle = st.slider("Rotation Angle", -180, 180, 0)
        flip_option = st.checkbox("Flip Image")
        
        processed_image = processed_image[y:y+height, x:x+width]
                
        
        if rotation_angle != 0:
            rows, cols = processed_image.shape[:2]
            rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 0-rotation_angle, 1)
            processed_image = cv2.warpAffine(processed_image, rotation_matrix, (cols, rows))

        # Flip the image
        if flip_option:
            processed_image = cv2.flip(processed_image, 1)

        # Display the processed image
        edited.image(processed_image, caption="Processed Image", use_column_width=True)

        #select image format
        format_ = st.selectbox('select format', ['jpg', 'png', 'jpeg'])
        # Save the processed image
        if st.button("SAVE", type='primary'):
            cv2.imwrite(f"lb_editor_{uploaded_file.name}.{format_}", cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB))
            st.success("Processed image saved successfully!")
            st.write(uploaded_file.name)
    
if __name__ == "__main__":
    main()