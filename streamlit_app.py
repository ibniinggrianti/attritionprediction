import streamlit as st
import pandas as pd

st.title('Attrition Prediction')

st.info("Is your job worth keeping? Should you stay? Or just leave? Let's try!")

df = pd.read.csv('https://raw.githubusercontent.com/ibniinggrianti/attritionprediction/refs/heads/master/IBM-HR-Analytics-Employee-Attrition-and-Performance-Revised.csv')
df
