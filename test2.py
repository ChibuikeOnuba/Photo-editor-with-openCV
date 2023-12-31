import cv2
import streamlit as st
import numpy as np

def main():
    st.title("Photo Cropper and Blur App")

    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        processed_image = image.copy()
        
        adjust_variables = ['None', 'Brightness', 'Blur', 'Sharpness', 'Contrast']
        adjust = st.selectbox(options=adjust_variables, label='Adjust')
        
        # Blur the image if the blur option is selected
        if adjust == 'Blur':
            blur_radius = st.slider(f'Adjust {adjust}', min_value=1, max_value=20, value=5, step=2)
            processed_image = cv2.GaussianBlur(processed_image, (blur_radius, blur_radius), 0)
            
        
        elif adjust == 'Brightness':
            brightness = st.slider("Brightness", -100, 100, 0)
            processed_image = cv2.convertScaleAbs(processed_image, beta=brightness)
            
        elif adjust == "Contrast":
            contrast = st.slider("Contrast", -100, 100, 0)
            processed_image = cv2.convertScaleAbs(processed_image, alpha=(contrast / 100.0))
        
        # Cropping and rotation
        st.subheader("Crop & Rotate")
        row = st.columns(2)
        x = row[0].slider("X-coordinate", 0, processed_image.shape[1], 0)
        y = row[1].slider("Y-coordinate", 0, processed_image.shape[0], 0)
        width = row[0].slider("Width", 1, processed_image.shape[1], processed_image.shape[1])
        height = row[1].slider("Height", 1, processed_image.shape[0], processed_image.shape[0])
        
        rotation_angle = st.slider("Rotation Angle", -180, 180, 0)
        flip_option = st.checkbox("Flip Image")
        
        cropped_image = processed_image[y:y+height, x:x+width]

                   
        # Flip the image
        if rotation_angle != 0:
            rows, cols = cropped_image.shape[:2]
            rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), rotation_angle, 1)
            cropped_image = cv2.warpAffine(cropped_image, rotation_matrix, (cols, rows))

        
        if flip_option:
            cropped_image = cv2.flip(cropped_image, 1)

        # Display the cropped and possibly blurred image
        st.image(processed_image, caption="Processed Image", use_column_width=True)

        # Save the processed image if requested
        if st.button("Save Processed Image"):
            cv2.imwrite("processed_image.jpg", cropped_image)
            st.success("Processed image saved successfully!")

if __name__ == "__main__":
    main()