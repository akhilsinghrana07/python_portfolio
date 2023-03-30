import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("Akhil Singh Rana")
    content = """
    Hi, I'm Akhil Singh Rana, a software engineer experienced in data engineering and web application development. I'm currently pursuing Software Engineering Technology at Centennial College in Toronto, and I hold a Bachelor's in Computer Science and Engineering from SRM Institute of Science and Technology in India.

I have experience as a Software Engineer and Data Engineer Intern, where I collaborated with cross-functional teams, utilized version control systems, and employed data visualization tools and machine learning techniques. My skills include Python programming, PowerBI and Azure, Microsoft Excel, database management, and Docker.

I'm passionate about problem-solving, project efficiency, and continuous learning. I'm excited about new opportunities in software engineering
    """
    st.info(content)

content2 = """
Below you can find some of the projects I have built. Feel free to contact me!
"""

st.write(content2)
col3, empty_col ,col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")