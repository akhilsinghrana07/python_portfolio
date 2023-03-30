import streamlit as st
import base64
import io

st.set_page_config(layout="wide")
# Set the title of the app


# Open the PDF file
with open("images/Akhil_Singh_Rana_Resume.pdf", "rb") as f:
    pdf_bytes = f.read()

# Create a column layout
col1, col2 = st.columns([1, 0.1])

# Display the title in the first column
with col1:
    st.title("Resume")

# Display the download button in the second column
with col2:
    download_button = st.download_button(
        label="Download PDF", data=pdf_bytes, file_name="Akhil_Singh_Rana_Resume.pdf"
    )

# Show the resume file
st.image('images/Akhil_Singh_Rana_Resume.jpg')