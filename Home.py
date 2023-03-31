import streamlit as st
import pandas as pd
import base64

st.set_page_config(layout="wide")


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('images/b7.jpg')
st.title("Akhil Singh Rana")

col1, col2 = st.columns(2)
with st.container():
    with col1:
        st.image('images/photo.png')
        st.title(f"[LinkedIn]({'https://www.linkedin.com/in/akhilsinghrana729/'})")
    with col2:
        content = """
        Hi there! I am Akhil Singh Rana, a software engineer with experience in data engineering and web application development. I am currently pursuing Software Engineering Technology at Centennial College in Toronto.
    
    Previously, I completed my Bachelor's in Computer Science and Engineering from SRM Institute of Science and Technology in Chennai, India. During my academic journey, I gained a strong foundation in Python programming, data analysis, and SQL proficiency.
    
    SKILLS:
    
    Python (Pandas, NumPy, Matplotlib, Scikit-learn)
    .NET framework(C#)
    ReactJS( MVC , graphql, RESTFull API)
    PowerBI, Azure (Data lakes, Data Factory, Azure SQL Database, Cosmos DB)
    Microsoft Excel (Macros, V-Lookup, Power Query)
    SQL proficiency, database management, SQL queries
    Git, GitHub (cloning, merging, collaboration, Git actions)
    Web scraping and API integration with Python
    Data cleaning, wrangling, and visualization
    Machine learning (analysis, prediction)
    Docker (containerization, build image, deployment)
    Communication, presentation, and time management
    
    I am passionate about using my technical skills to solve complex problems and improve overall project efficiency and effectiveness. I am always eager to learn and grow, and I am excited about new opportunities in the field of software engineering.
        """
        st.info(content)

content2 = """
Below you can find some of the projects I have built. Feel free to contact me!
"""

st.write(content2)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        # st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        # st.write(f"[Source Code]({row['url']})")
