import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

st.title('Welcome to my Streamlit App')
st.write('Hi! I am Dibyasha, a junior double majoring in Computer Science and Economics at Knox. I am passionate towards using technology as a means to solve human-centered problems, and am interested in using technology to leverage scalable, and impactful solutions that contribute to broader problems that humans face!')
st.image("Dibyasha Picture.jpg")

user_input=st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('You entered:', user_input)

#Plotting a linear regression graph for fun
st.write('Now, We will Work with Our Cropyields Dataset to Perform Linear Regression and Create a Visualization:')
df=pd.read_csv("cropyields.csv")
country=st.selectbox("Select Country", df["LOCATION"].unique())
crop=st.selectbox("Select Crop", df["SUBJECT"].unique())
filtered=df[(df["LOCATION"]==country) & (df["SUBJECT"]==crop)]
X=filtered[["TIME"]]
y=filtered["Value"]

#Fit the model
model=LinearRegression()
model.fit(X,y)
filtered["Prediction"]=model.predict(X)
#Create visualization
st.line_chart(filtered.set_index("TIME")[["Value","Prediction"]])
st.write('I had so much fun doing this assignment!')
              
