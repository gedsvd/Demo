import streamlit as st
import cv2
import numpy as np
from tensorflow import keras
from PIL import Image
import os
menu1 = ["Home","Login", "Signup"]
choice1 = st.sidebar.selectbox("menu",menu1)
st.title("DeepFake Classification")
if choice1=="Home":
    #html
    testp="<p style='font-size: 17px;text-align:center;font-family:verdana;text-align: justify'>The rapid growth of artificial intelligence has led to the creation of DeepFake images that can manipulate human faces realistically. Such fake images are widely misused in social media, misinformation, and cybercrime. This study proposes a deep learning-based approach to detect face DeepFake images accurately. The system uses convolutional neural networks (CNN) to learn complex facial features such as texture inconsistencies, unnatural edges, and abnormal facial patterns. A dataset containing real and fake face images is used for training and testing the model. Preprocessing techniques like normalization and resizing improve detection accuracy. Experimental results show that the deep learning model effectively distinguishes DeepFake images from genuine ones. This research helps in preventing digital fraud, protecting personal identity, and maintaining trust in online content. The proposed system can be used by social media platforms, law enforcement agencies, and cybersecurity organizations.</p>"
    st.markdown(testp,unsafe_allow_html=True)
elif choice1=="Login":
    st.subheader("Login Section")
    Email=st.sidebar.text_input('Email')
    password=st.sidebar.text_input('Password',type='password')
    b1=st.sidebar.checkbox("login")
   # ----------------------
# Download model if not exists
# ----------------------
if not os.path.exists("Deep_model.keras"):
    import gdown

    gdown.download(  # noqa: E402
        id="1MvQFRlMsv6BJh94y_7vpNMnJ_YJqI_PK",
        output="Deep_model.keras",
        quiet=False
    )

# ----------------------
# Load the trained model
# ----------------------
model = keras.models.load_model("Deep_model.keras")

# ----------------------
# Streamlit App
# ----------------------
st.title("DeepFake Image Detection")
st.write("Upload an image to predict whether it is Real or Fake.")

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Open image with PIL
    image = Image.open(uploaded_file).convert("RGB")

    # Display image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Read image for OpenCV
    file_bytes = np.frombuffer(uploaded_file.getvalue(), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Check if image is loaded correctly
    if img is not None:
        # Resize image
        img = cv2.resize(img, (64, 64))
        img = img.astype("float32") / 255.0
        # Prediction
        prd = np.argmax(
            model.predict(img.reshape(1, 64, 64, 3)),
            axis=1
        )[0]

        # Class names
        classes = ["real", "fake"]

        # Show result
        st.success(classes[prd])
else:
    st.subheader("Signup Section")
    FirstName=st.text_input('First Name')
    LastName=st.text_input('Last Name')
    Mobile=st.text_input('Contact No')
    Email=st.text_input('Email')
    new_password=st.text_input('Password',type='password')
    Cpassword=st.text_input('Confirm Password',type='password')
    if st.button("Sign up"):
        st.success("Message")
    else:
        st.warning("Not Valid Data")
            
            
            
            
            
            
