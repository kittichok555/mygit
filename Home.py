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
st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])
