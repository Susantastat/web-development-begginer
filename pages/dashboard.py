import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import image
import plotly.express as px
import os
import seaborn as sns



# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "Resources")

IMAGE_PATH = os.path.join(dir_of_interest, "image", "campusplacement.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Placementdata.csv")

st.title("Dashboard - campus recruitment")
st.write("##")
st.write(
    """
    This is the data of campus recruitment. 
    - there is 14 attributes 
    - i have considered hsc_p (12th class  percentage)
    - hsc_s (stream taken by student)
    - status (status (whether the student is plaed or not))
    - degree_p (degree percentage)
    - salary (salary provided by the comapny to the students whom they hire)

    i am basically considered the histogram, boxplot.
    """
)
    
img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Stream = st.selectbox("Select the Stream:", df['hsc_s'].unique())

col1, col2,col3 = st.columns(3)



fig_1 = px.histogram(df[df['hsc_s'] == Stream], x="hsc_p")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['hsc_s'] == Stream], y="hsc_p")
col2.plotly_chart(fig_2, use_container_width=True)

Status = st.selectbox("Select the Status:", df['status'].unique())

fig_3=px.box(df[df['status']==Status],y="salary")
col3.plotly_chart(fig_3,use_container_width=True)




 


