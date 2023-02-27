

import streamlit as st
st.set_page_config(page_title= "Come to my world",page_icon=":tada:",layout="wide")
st.subheader("Hi i am susanta :wave:")
st.title("An aspiring data analyst from pondicherry university")
st.write("It is my first experience about the streamlit and way exiciting to build a page that will help me and you to connect")

st.write("[lets connect by just click  :innocent: > ]( https://www.linkedin.com/in/susanta-dhurua-749875139)")
st.write("[just check are u there >](https://www.instagram.com/t_susanta_sd/?next=%2F)")


#---- WHAT I DO ------
with st.container():
    st.write("----")
    left_column, right_column=st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("##")
        st.write(
            """
              i am a student of msc statistics final year and looking for a data analyst role:
            - i have enhanced knowledge on mysql, powerbi, python, ms office, r 
            - actively looking for data scientist role.
            - ready to serve in a reputed organization where i can input my experience and stragies to maximize the exponential growth of a company.

            If this sounds intresting to you, consider my resume and give a feedback thank you for your valuable time.
            """
        )
        st.write("[here is my resume >](https://drive.google.com/drive/folders/1h1PvqrMDwgWtJeR0xu3BYPEpkKB2NQwe?usp=share_link)")