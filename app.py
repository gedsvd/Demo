import streamlit as st
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
    if b1:
        imgur=st.file_uploader("Browse Image")
        if st.button("Predict"):
            st.success("Message")                        
        else:
            st.warning("Incorrect Image")  
    else:
        st.warning("Not Valid Data")
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
            
            
            
            
            
            