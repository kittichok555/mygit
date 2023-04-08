from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

#st.header("Kittichok555555555") 
st.image("./pic/banner.jpg")
#st.image("./pic/my.jpg")

html_8 = """
<div style="background-color:#7E7E7E;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4 style="color: #FF0000">การทำนายข้อมูลดอกไม้</h4></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

dt = pd.read_csv("./data/iris.csv")
st.markdown("<center>",unsafe_allow_html=True)
st.write(dt.head(10))
st.markdown("</center>",unsafe_allow_html=True)