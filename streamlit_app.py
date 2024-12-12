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

with st.expander('Overall Statistics'):        
    if "Attrition" in data.columns:
        attrition_rate = data["Attrition"].value_counts()
          
        # Creating two columns for side-by-side plots
        col1, col2 = st.columns(2)
          
        # Bar Plot in the first column
        with col1:
            st.info("### Employee Attrition Counts")
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.barplot(x=attrition_rate.index, y=attrition_rate.values, palette=["#1d7874", "#8B0000"], ax=ax)
            #ax.set_title("Employee Attrition Counts", fontweight="black", size=20, pad=20)
          
            # Adding value annotations to the bars
            for i, v in enumerate(attrition_rate.values):
                ax.text(i, v, v, ha="center", fontweight='black', fontsize=10)
          
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

with st.expander('Statistics by Personal Data'):
    if "Gender" in data.columns and "Attrition" in data.columns:
        gender_attrition = data["Gender"].value_counts()

        # Creating two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Pie chart for gender distribution in the first column
        with col1:
            st.info("### Employees Distribution by Gender")
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.pie(
                gender_attrition, 
                autopct="%.0f%%", 
                labels=gender_attrition.index, 
                textprops={"fontweight": "black", "size": 20},
                explode=[0, 0.1], 
                startangle=90,
                colors=["#ffb563", "#FFC0CB"]
            )
            st.pyplot(fig)

        # Bar plot for attrition rate by gender in the second column
        with col2:
            st.info("### Employee Attrition Rate by Gender")
            new_df = data[data["Attrition"] == "Yes"]
            value_1 = data["Gender"].value_counts()
            value_2 = new_df["Gender"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            
            fig, ax = plt.subplots(figsize=(4, 4))
            sns.barplot(x=value_2.index, y=value_2.values, palette=["#D4A1E7", "#E7A1A1"], ax=ax)
            for index, value in enumerate(value_2):
                ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", 
                        size=10, fontweight="black")
            st.pyplot(fig)
          
    else:
        st.info("Please upload a CSV file to start the analysis.")
    if "Age" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employee Distribution by Age
        with col1:
            st.info("### Employee Distribution by Age")
            fig, ax = plt.subplots(figsize=(6, 6))
            sns.histplot(x="Age", hue="Attrition", data=data, kde=True, palette=["#11264e", "#6faea4"], ax=ax)
            #ax.set_title("Employee Distribution by Age", fontweight="black", size=20, pad=10)
            st.pyplot(fig)

        # Visualization for Employee Distribution by Age & Attrition
        with col2:
            st.info("### Employee Distribution by Age & Attrition")
            fig, ax = plt.subplots(figsize=(8, 8))
            sns.boxplot(x="Attrition", y="Age", data=data, palette=["#D4A1E7", "#6faea4"], ax=ax)
            #ax.set_title("Employee Distribution by Age & Attrition", fontweight="black", size=20, pad=10)
            st.pyplot(fig)
    
    else:
        st.info("Please upload a CSV file to start the analysis.")
    if "MaritalStatus" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employees by Marital Status (Pie chart)
        with col1:
            st.info("### Employees by Marital Status")
            fig, ax = plt.subplots(figsize=(6, 6))
            value_1 = data["MaritalStatus"].value_counts()
            ax.pie(
                value_1.values,
                labels=value_1.index,
                autopct="%.1f%%",
                pctdistance=0.75,
                startangle=90,
                colors=['#E84040', '#E96060', '#E88181', '#E7A1A1'],
                textprops={"fontweight": "black", "size": 15}
            )
            # Add a white circle at the center to make it a donut chart
            center_circle = plt.Circle((0, 0), 0.4, fc='white')
            fig.gca().add_artist(center_circle)
            #ax.set_title("Employees by Marital Status", fontweight="black", size=20, pad=20)
            st.pyplot(fig)

        # Visualization for Attrition Rate by Marital Status (Bar plot)
        with col2:
            st.info("### Attrition Rate by Marital Status")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["MaritalStatus"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.barplot(x=value_2.index, y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"], ax=ax)
            #ax.set_title("Attrition Rate by Marital Status", fontweight="black", size=20, pad=20)

            # Add text annotations for each bar
            for index, value in enumerate(value_2):
                ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=10, fontweight="black")
            st.pyplot(fig)

    else:
        st.info("Please upload a CSV file to start the analysis.")
      
with st.expander('Statistics by Job'):
  if "RelationshipSatisfaction" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employees by Relationship Satisfaction (Pie chart)
        with col1:
            st.info("### Employees by Relationship Satisfaction")
            fig, ax = plt.subplots(figsize=(6, 6))
            value_1 = data["RelationshipSatisfaction"].value_counts()
            ax.pie(
                value_1.values,
                labels=value_1.index,
                autopct="%.1f%%",
                pctdistance=0.75,
                startangle=90,
                colors=['#6495ED', '#87CEEB', '#00BFFF', '#1E90FF'],
                textprops={"fontweight": "black", "size": 15}
            )
            # Add a white circle at the center to make it a donut chart
            center_circle = plt.Circle((0, 0), 0.4, fc='white')
            fig.gca().add_artist(center_circle)
            #ax.set_title("Employees by Relationship Satisfaction", fontweight="black", size=20, pad=20)
            st.pyplot(fig)

        # Visualization for Attrition Rate by Relationship Satisfaction (Bar plot)
        with col2:
            st.info("### Attrition Rate by Relationship Satisfaction")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["RelationshipSatisfaction"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"], ax=ax)
            #ax.set_title("Attrition Rate by Relationship Satisfaction", fontweight="black", size=20, pad=20)

            # Add text annotations for each bar
            for index, value in enumerate(value_2):
                ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
            st.pyplot(fig)

  else:
      st.info("Please upload a CSV file to start the analysis.")

