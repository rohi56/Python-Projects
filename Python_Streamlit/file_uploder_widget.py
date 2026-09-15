import streamlit as st

uploaded_images = st.file_uploader("Upload images", accept_multiple_files=True)
uploaded_texts = st.file_uploader("Upload text files", accept_multiple_files=True)

for uploaded_image in uploaded_images:
    st.write(f"Uploaded image: {uploaded_image.name}")
    st.image(uploaded_image, caption=uploaded_image.name)

for uploaded_text in uploaded_texts:
    st.write(f"Uploaded text file: {uploaded_text.name}")
    text_content = uploaded_text.read().decode("utf-8")
    st.text_area("Text content", value=text_content, height=200)