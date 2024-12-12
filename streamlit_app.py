import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Attrition Prediction')

st.write("Is your job worth keeping? Should you stay? Or just leave? Let's try!")

#with st.expander('Data'):
  #df = pd.read_csv('https://raw.githubusercontent.com/ibniinggrianti/attritionprediction/refs/heads/master/IBM-HR-Analytics-Employee-Attrition-and-Performance-Revised.csv')
  #df

# Load dataset (Ensure the CSV file is in the correct location)
data = pd.read_csv("https://raw.githubusercontent.com/ibniinggrianti/attritionprediction/refs/heads/master/IBM-HR-Analytics-Employee-Attrition-and-Performance-Revised.csv")  # Replace with your actual CSV file name

# Employee Attrition Counts Visualization
if "Attrition" in data.columns:
        attrition_rate = data["Attrition"].value_counts()

        # Creating two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Bar Plot in the first column
        with col1:
            st.info("### Employee Attrition Counts")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.barplot(x=attrition_rate.index, y=attrition_rate.values, palette=["#1d7874", "#8B0000"], ax=ax)
            #ax.set_title("Employee Attrition Counts", fontweight="black", size=20, pad=20)

            # Adding value annotations to the bars
            for i, v in enumerate(attrition_rate.values):
                ax.text(i, v, v, ha="center", fontweight='black', fontsize=18)

            st.pyplot(fig)

        # Pie Chart in the second column
        with col2:
            st.info("### Employee Attrition Rate")
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.pie(
                attrition_rate, 
                labels=["No", "Yes"], 
                autopct="%.2f%%", 
                textprops={"fontweight": "black", "size": 18},
                colors=["#1d7874", "#AC1F29"],
                explode=[0, 0.1], 
                startangle=90
            )
            center_circle = plt.Circle((0, 0), 0.3, fc='white')
            fig.gca().add_artist(center_circle)
            #ax.set_title("Employee Attrition Rate", fontweight="black", size=20, pad=10)

            st.pyplot(fig)

else:
    st.info("Please upload a CSV file to start the analysis.")
