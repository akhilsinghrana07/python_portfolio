import streamlit as st

st.set_page_config(layout="wide")
st.header('Work Experience')

col1, col2 = st.columns(2)

with col1:
    st.image('images/w1.gif')

with col2:
    st.title("doodleblue innovation")
    st.write(f"[Company's Website]({'https://www.doodleblue.com/'})")
    st.write(f"""
- Conducted thorough testing and debugging to ensure high-quality code, improving overall project efficiency and effectiveness.
- Collaborated with cross-functional teams to develop REST APIs and implement user-friendly, scalable React web applications.
- Utilized version control systems such as Git and GitHub to manage code, streamline workflows, and maintain project integrity.
- Employed agile methodologies to efficiently manage projects and prioritize tasks based on client needs and project timelines.
- Demonstrated excellent problem-solving skills, quickly identifying and resolving technical issues to ensure seamless project completion.""")
    st.write(f"[Document]({'https://drive.google.com/file/d/1zAGszHEN9I1--jEPkNx41Y0DYd6UtR5K/view?usp=sharing'})")
with col1:
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.image('images/w2.jpg', width=500)

with col2:
    st.title("ACIL Technologies")
    st.write(f"[Company's Website]({'https://www.acilindia.com/'})")
    st.write(f"""
- Developed and implemented data cleaning and data wrangling processes, resulting in more accurate and reliable data.
- Created and optimized SQL queries to extract, transform, and load (ETL) data from multiple sources, ensuring data integrity and consistency.
- Employed data visualization tools such as PowerBI to effectively communicate insights and findings to stakeholders.
- Utilized machine learning techniques to analyze and predict patterns in large datasets, improving overall data-driven decision-making.
- Demonstrated a strong understanding of cloud-based technologies such as AWS and Azure, to effectively manage data in the cloud.""")
    st.write(f"[Document]({'https://drive.google.com/file/d/1CHXuBIBhTMLoK05P64RVB-DCH1NnRlzg/view?usp=sharing'})")
