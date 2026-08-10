import streamlit as st
import cv2
import numpy as np
from tensorflow import keras
from PIL import Image
import os

# ----------------------
# Sidebar Menu
# ----------------------
menu1 = ["Home", "Login", "Signup"]
choice1 = st.sidebar.selectbox("Menu", menu1)

st.title("DeepFake Classification")

# ----------------------
# Home Section
# ----------------------
if choice1 == "Home":
    testp = """
    The rapid growth of artificial intelligence has led to the creation of
    DeepFake images that can manipulate human faces realistically. Such fake
    images are widely misused in social media, misinformation, and cybercrime.

    This study proposes a deep learning-based approach to detect face DeepFake
    images accurately. The system uses convolutional neural networks (CNN) to
    learn complex facial features such as texture inconsistencies, unnatural
    edges, and abnormal facial patterns.

    A dataset containing real and fake face images is used for training and
    testing the model. Preprocessing techniques like normalization and resizing
    improve detection accuracy. Experimental results show that the deep learning
    model effectively distinguishes DeepFake images from genuine ones.

    This research helps in preventing digital fraud, protecting personal
    identity, and maintaining trust in online content. The proposed system can
    be used by social media platforms, law enforcement agencies, and
    cybersecurity organizations.
    """

    st.markdown(testp)

# ----------------------
# ----------------------
# ----------------------
# Login Section
# ----------------------
elif choice1 == "Login":
    st.subheader("Login Section")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):

        # Simple login validation
        if email == "admin@gmail.com" and password == "1234":
            st.success("Login Successful")

            # ----------------------
            # Detection Page
            # ----------------------
            st.markdown("---")
            st.header("DeepFake Image Detection")
            st.write("Upload an image to predict whether it is Real or Fake.")

            # Download model if not exists
            if not os.path.exists("Deep_model.keras"):
                import gdown

                gdown.download(
                    id="1MvQFRlMsv6BJh94y_7vpNMnJ_YJqI_PK",
                    output="Deep_model.keras",
                    quiet=False
                )

            # Load model
            model = keras.models.load_model("Deep_model.keras")

            # Upload image
            uploaded_file = st.file_uploader(
                "Choose an image",
                type=["jpg", "jpeg", "png"]
            )

            if uploaded_file is not None:
                # Open image
                image = Image.open(uploaded_file).convert("RGB")

                # Show image
                st.image(
                    image,
                    caption="Uploaded Image",
                    use_container_width=True
                )

                # Convert for OpenCV
                file_bytes = np.frombuffer(
                    uploaded_file.getvalue(),
                    dtype=np.uint8
                )

                img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

                if img is not None:
                    # Resize and normalize
                    img = cv2.resize(img, (64, 64))
                    img = img.astype("float32") / 255.0

                    # Predict
                    prd = np.argmax(
                        model.predict(img.reshape(1, 64, 64, 3)),
                        axis=1
                    )[0]

                    classes = ["Real", "Fake"]

                    # Result
                    st.success(f"Prediction: {classes[prd]}")
                    
                else:
                    st.error("Invalid image file")

        else:
            st.error("Invalid Email or Password")
# ----------------------
# Signup Section
# ----------------------
else:
    st.subheader("Signup Section")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    mobile = st.text_input("Contact No")
    email = st.text_input("Email")
    new_password = st.text_input("Password", type="password")
    cpassword = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if new_password == cpassword and first_name and email:
            st.success("Signup Successful!")
        else:
            st.warning("Invalid data or passwords do not match.")
