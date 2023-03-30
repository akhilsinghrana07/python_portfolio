import streamlit as st

st.set_page_config(layout="wide")
st.header('Certifications')

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Udemy")
   st.image('images/uc.gif', use_column_width='always')
   st.image('images/c1.jpg', use_column_width='always')
with col2:
   st.header("HackerRank")
   st.image('images/hr.gif', use_column_width='always')
   st.image('images/c2.jpg', use_column_width='always')

with col3:
   st.header("Coursera")
   st.image('images/cc.gif', use_column_width='always')
   st.image('images/c3.jpeg', use_column_width='always')