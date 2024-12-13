import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

st.title('Attrition Prediction')

st.subheader("Is your job worth keeping? Should you stay? Or just leave? Let's try!")
st.write("You can see below for more information")

#with st.expander('Data'):
  #df = pd.read_csv('https://raw.githubusercontent.com/ibniinggrianti/attritionprediction/refs/heads/master/IBM-HR-Analytics-Employee-Attrition-and-Performance-Revised.csv')
  #df

# Load dataset (Ensure the CSV file is in the correct location)
data = pd.read_csv("https://raw.githubusercontent.com/ibniinggrianti/attritionprediction/refs/heads/master/IBM-HR-Analytics-Employee-Attrition-and-Performance-Revised.csv")  # Replace with your actual CSV file name
#df = pd.read_csv('https://raw.githubusercontent.com/ibniinggrianti/attritionprediction/refs/heads/master/IBM-HR-Analytics-Employee-Attrition-and-Performance-Revised.csv')
  #df

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
      
    if "Education" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employees by Education (Bar Plot)
        with col1:
            st.info("### Employees Distribution by Education")
            value_1 = data["Education"].value_counts()
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_1.index, 
                y=value_1.values, 
                order=value_1.index, 
                palette=["#FFA07A", "#D4A1E7", "#FFC0CB", "#87CEFA"], 
                ax=ax
            )
            #ax.set_title("Employees Distribution by Education", fontweight="black", size=20, pad=15)
            # Add value annotations on the bars
            for index, value in enumerate(value_1.values):
                ax.text(index, value, value, ha="center", va="bottom", fontweight="black", size=10)
            st.pyplot(fig)

        # Visualization for Employee Attrition by Education (Bar Plot)
        with col2:
            st.info("### Employee Attrition by Education")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["Education"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_2.index, 
                y=value_2.values, 
                order=value_2.index, 
                palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"], 
                ax=ax
            )
            #ax.set_title("Employee Attrition by Education", fontweight="black", size=18, pad=15)
            # Add value and percentage annotations on the bars
            for index, value in enumerate(value_2.values):
                ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", 
                        ha="center", va="bottom", fontweight="black", size=10)
            st.pyplot(fig)
    else:
        st.info("Please upload a CSV file to start the analysis.")
    if "EducationField" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employees by Education Field (Bar Plot)
        with col1:
            st.info("### Employees by Education Field")
            value_1 = data["EducationField"].value_counts()
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_1.index, 
                y=value_1.values, 
                order=value_1.index, 
                palette=["#FFA07A", "#D4A1E7", "#FFC0CB", "#87CEFA"], 
                ax=ax
            )
            #ax.set_title("Employees by Education Field", fontweight="black", size=20, pad=15)
            # Add value annotations on the bars
            for index, value in enumerate(value_1.values):
                ax.text(index, value, value, ha="center", va="bottom", fontweight="black", size=10)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            st.pyplot(fig)

        # Visualization for Employee Attrition by Education Field (Bar Plot)
        with col2:
            st.info("### Employee Attrition by Education Field")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["EducationField"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_2.index, 
                y=value_2.values, 
                order=value_2.index, 
                palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7"], 
                ax=ax
            )
            #ax.set_title("Employee Attrition by Education Field", fontweight="black", size=18, pad=15)
            # Add value and percentage annotations on the bars
            for index, value in enumerate(value_2.values):
                ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", 
                        ha="center", va="bottom", fontweight="black", size=10)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            st.pyplot(fig)
    else:
        st.info("Please upload a CSV file to start the analysis.")
      
with st.expander('Statistics by Employee Detail'):
  if "Department" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employees by Department (Bar Plot)
        with col1:
            st.info("### Employees by Department")
            value_1 = data["Department"].value_counts()
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_1.index, 
                y=value_1.values, 
                palette=["#FFA07A", "#D4A1E7", "#FFC0CB"], 
                ax=ax
            )
            #ax.set_title("Employees by Department", fontweight="black", size=20, pad=20)
            # Add value annotations on the bars
            for index, value in enumerate(value_1.values):
                ax.text(index, value, str(value), ha="center", va="bottom", fontweight="black", size=10)
            st.pyplot(fig)

        # Visualization for Employee Attrition Rate by Department (Bar Plot)
        with col2:
            st.info("### Attrition Rate by Department")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["Department"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_2.index, 
                y=value_2.values, 
                palette=["#11264e", "#6faea4", "#FEE08B"], 
                ax=ax
            )
            #ax.set_title("Attrition Rate by Department", fontweight="black", size=20, pad=20)
            # Add value and percentage annotations on the bars
            for index, value in enumerate(value_2):
                ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", 
                        fontweight="black", size=10)
            st.pyplot(fig)
  else:
       st.info("Please upload a CSV file to start the analysis.")
  if "JobRole" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employees by Job Role (Bar Plot)
        with col1:
            st.info("### Employees by Job Role")
            value_1 = data["JobRole"].value_counts()
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_1.index.tolist(), 
                y=value_1.values, 
                palette=["#FFA07A", "#D4A1E7", "#FFC0CB", "#87CEFA"],
                ax=ax
            )
            #ax.set_title("Employees by Job Role", fontweight="black", pad=15, size=18)
            ax.set_xticklabels(value_1.index, rotation=90)
            # Add value annotations on the bars
            for index, value in enumerate(value_1.values):
                ax.text(index, value, value, ha="center", va="bottom", fontweight="black", size=10)
            st.pyplot(fig)

        # Visualization for Attrition Rate by Job Role (Bar Plot)
        with col2:
            st.info("### Attrition Rate by Job Role")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["JobRole"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_2.index.tolist(), 
                y=value_2.values, 
                palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"], 
                ax=ax
            )
            #ax.set_title("Employee Attrition Rate by Job Role", fontweight="black", pad=15, size=18)
            ax.set_xticklabels(value_2.index, rotation=90)
            # Add value and percentage annotations on the bars
            for index, value in enumerate(value_2.values):
                ax.text(
                    index, value, f"{value} ({int(attrition_rate[index])}%)", 
                    ha="center", va="bottom", fontweight="black", size=10
                )
            st.pyplot(fig)
  else:
      st.info("Please upload a dataset with 'JobRole' and 'Attrition' columns to view visualizations.")
  if "JobLevel" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employees by Job Level (Pie Chart)
        with col1:
            st.info("### Employees by Job Level")
            value_1 = data["JobLevel"].value_counts()
            fig, ax = plt.subplots(figsize=(6, 6))
            wedges, texts, autotexts = ax.pie(
                value_1.values, 
                labels=value_1.index, 
                autopct="%.1f%%", 
                pctdistance=0.8, 
                startangle=90, 
                colors=['#FF6D8C', '#FF8C94', '#FFAC9B', '#FFCBA4', "#FFD8B1"], 
                textprops={"fontweight": "black", "size": 10}
            )
            center_circle = plt.Circle((0, 0), 0.4, fc='white')
            plt.gca().add_artist(center_circle)
            #ax.set_title("Employees by Job Level", fontweight="black", size=16, pad=15)
            st.pyplot(fig)

        # Visualization for Attrition Rate by Job Level (Bar Plot)
        with col2:
            st.info("### Attrition Rate by Job Level")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["JobLevel"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_2.index, 
                y=value_2.values, 
                palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"], 
                ax=ax
            )
            #ax.set_title("Attrition Rate by Job Level", fontweight="black", size=16, pad=15)
            # Add percentage annotations to bars
            for index, value in enumerate(value_2.values):
                ax.text(
                    index, value, 
                    f"{value} ({int(attrition_rate[index])}%)", 
                    ha="center", va="bottom", 
                    fontweight="black", size=10
                )
            st.pyplot(fig)

  else:
      st.info("Please upload a dataset containing 'JobLevel' and 'Attrition' columns to display visualizations.")
      
with st.expander('Statistics by Job'):
    if "BusinessTravel" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employees by Business Travel (Pie Chart)
        with col1:
            st.info("### Employees by Business Travel")
            fig, ax = plt.subplots(figsize=(10, 10))
            value_1 = data["BusinessTravel"].value_counts()
            ax.pie(
                value_1.values,
                labels=value_1.index,
                autopct="%.1f%%",
                pctdistance=0.75,
                startangle=90,
                colors=['#E84040', '#E96060', '#E88181'],
                textprops={"fontweight": "black", "size": 15}
            )
            # Add a white circle at the center to make it a donut chart
            center_circle = plt.Circle((0, 0), 0.4, fc='white')
            fig.gca().add_artist(center_circle)
            #ax.set_title("Employees by Business Travel", fontweight="black", size=20, pad=20)
            st.pyplot(fig)

        # Visualization for Attrition Rate by Business Travel (Bar Plot)
        with col2:
            st.info("### Attrition Rate by Business Travel")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["BusinessTravel"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.barplot(
                x=value_2.index, 
                y=value_2.values, 
                palette=["#11264e", "#6faea4", "#FEE08B"], 
                ax=ax
            )
           # ax.set_title("Attrition Rate by Business Travel", fontweight="black", size=20, pad=20)

            # Add text annotations for each bar
            for index, value in enumerate(value_2):
                ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", 
                        size=10, fontweight="black")
            st.pyplot(fig)

    else:
        st.info("Please upload a CSV file to start the analysis.")
    if "EnvironmentSatisfaction" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        # Visualization for Employees by Environment Satisfaction (Pie Chart)
        with col1:
            st.info("### Employees by Environment Satisfaction")
            value_1 = data["EnvironmentSatisfaction"].value_counts()
            fig, ax = plt.subplots(figsize=(6, 5))
            ax.pie(
                value_1.values, 
                labels=value_1.index, 
                autopct="%.1f%%", 
                pctdistance=0.75,
                startangle=90,
                colors=['#E84040', '#E96060', '#E88181'],
                textprops={"fontweight": "black", "size": 10}
            )
            center_circle = plt.Circle((0, 0), 0.4, fc='white')  # To make the chart look like a donut
            fig.gca().add_artist(center_circle)
            #ax.set_title("Employees by Environment Satisfaction", fontweight="black", size=20, pad=20)
            st.pyplot(fig)

        # Visualization for Attrition Rate by Environment Satisfaction (Bar Plot)
        with col2:
            st.info("### Attrition Rate by Environment Satisfaction")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["EnvironmentSatisfaction"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(6, 5))
            sns.barplot(
                x=value_2.index, 
                y=value_2.values, 
                order=value_2.index, 
                palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"], 
                ax=ax
            )
            #ax.set_title("Attrition Rate by Environment Satisfaction", fontweight="black", size=20, pad=20)
            # Add value and percentage annotations on the bars
            for index, value in enumerate(value_2):
                ax.text(
                    index, value, f"{value} ({int(attrition_rate[index])}%)", 
                    ha="center", va="bottom", fontweight="black", size=10
                )
            st.pyplot(fig)
    else:
        st.info("Please upload a CSV file to start the analysis.")
    
    if "JobSatisfaction" in data.columns and "Attrition" in data.columns:
      # Create two columns for side-by-side plots
      col1, col2 = st.columns(2)
  
      # Visualization for Employees by Job Satisfaction (Pie chart)
      with col1:
          st.info("### Employees by Job Satisfaction")
          fig, ax = plt.subplots(figsize=(6, 6))
          value_1 = data["JobSatisfaction"].value_counts()
          ax.pie(
              value_1.values,
              labels=value_1.index,
              autopct="%.1f%%",
              pctdistance=0.8,
              startangle=90,
              colors=['#FFB300', '#FFC300', '#FFD700', '#FFFF00'],
              textprops={"fontweight": "black", "size": 15}
          )
          # Add a white circle at the center to make it a donut chart
          center_circle = plt.Circle((0, 0), 0.4, fc='white')
          fig.gca().add_artist(center_circle)
          st.pyplot(fig)
  
      # Visualization for Attrition Rate by Job Satisfaction (Bar plot)
      with col2:
          st.info("### Attrition Rate by Job Satisfaction")
          new_df = data[data["Attrition"] == "Yes"]
          value_2 = new_df["JobSatisfaction"].value_counts()
          attrition_rate = np.floor((value_2 / value_1) * 100).values
          fig, ax = plt.subplots(figsize=(5, 4))
          sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index, 
                      palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7"], ax=ax)
          
          # Add text annotations for each bar
          for index, value in enumerate(value_2):
              ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=10, fontweight="black")
          
          st.pyplot(fig)
  
    else:
        st.info("Please upload a CSV file to start the analysis.")

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
                    ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=10, fontweight="black")
                st.pyplot(fig)
    
    else:
        st.info("Please upload a CSV file to start the analysis.")
      
    if "OverTime" in data.columns and "Attrition" in data.columns:
            # Create two columns for side-by-side plots
            col1, col2 = st.columns(2)
        
            # Visualization for Employees by OverTime (Pie chart)
            with col1:
                st.info("### Employees by OverTime")
                fig, ax = plt.subplots(figsize=(3, 3))
                value_1 = data["OverTime"].value_counts()
                ax.pie(
                    value_1.values,
                    labels=value_1.index,
                    autopct="%.1f%%",
                    pctdistance=0.75,
                    startangle=90,
                    colors=["#ffb563", "#FFC0CB"],
                    textprops={"fontweight": "black", "size": 10}
                )
                # Add a white circle at the center to make it a donut chart
                center_circle = plt.Circle((0, 0), 0.4, fc='white')
                fig.gca().add_artist(center_circle)
                st.pyplot(fig)
        
            # Visualization for Attrition Rate by OverTime (Bar plot)
            with col2:
                st.info("### Attrition Rate by OverTime")
                new_df = data[data["Attrition"] == "Yes"]
                value_2 = new_df["OverTime"].value_counts()
                attrition_rate = np.floor((value_2 / value_1) * 100).values
                fig, ax = plt.subplots(figsize=(5, 4))
                sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#D4A1E7", "#E7A1A1"], ax=ax)
                
                # Add text annotations for each bar
                for index, value in enumerate(value_2):
                    ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=10, fontweight="black")
                
                st.pyplot(fig)

    else:
        st.info("Please upload a CSV file to start the analysis.")
    if "PerformanceRating" in data.columns and "Attrition" in data.columns:
            # Create two columns for side-by-side plots
            col1, col2 = st.columns(2)
        
            # Visualization for Employees by PerformanceRating (Pie chart)
            with col1:
                st.info("### Employees by PerformanceRating")
                fig, ax = plt.subplots(figsize=(4, 4))
                value_1 = data["PerformanceRating"].value_counts()
                ax.pie(
                    value_1.values,
                    labels=value_1.index,
                    autopct="%.1f%%",
                    pctdistance=0.75,
                    startangle=90,
                    colors=["#ffb563", "#FFC0CB"],
                    textprops={"fontweight": "black", "size": 10}
                )
                # Add a white circle at the center to make it a donut chart
                center_circle = plt.Circle((0, 0), 0.4, fc='white')
                fig.gca().add_artist(center_circle)
                st.pyplot(fig)
        
            # Visualization for Attrition Rate by PerformanceRating (Bar plot)
            with col2:
                st.info("### Attrition Rate by PerformanceRating")
                new_df = data[data["Attrition"] == "Yes"]
                value_2 = new_df["PerformanceRating"].value_counts()
                attrition_rate = np.floor((value_2 / value_1) * 100).values
                fig, ax = plt.subplots(figsize=(5, 4))
                sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#D4A1E7", "#E7A1A1"], ax=ax)
                
                # Add text annotations for each bar
                for index, value in enumerate(value_2):
                    ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=10, fontweight="black")
                
                st.pyplot(fig)

    else:
        st.info("Please upload a CSV file to start the analysis.")

    if "WorkLifeBalance" in data.columns and "Attrition" in data.columns:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)
    
        # Visualization for Employees by WorkLifeBalance (Pie chart)
        with col1:
            st.info("### Employees by WorkLifeBalance")
            fig, ax = plt.subplots(figsize=(6, 6))
            value_1 = data["WorkLifeBalance"].value_counts()
            ax.pie(
                value_1.values,
                labels=value_1.index,
                autopct="%.1f%%",
                pctdistance=0.75,
                startangle=90,
                colors=['#FF8000', '#FF9933', '#FFB366', '#FFCC99'],
                textprops={"fontweight": "black", "size": 15}
            )
            # Add a white circle at the center to make it a donut chart
            center_circle = plt.Circle((0, 0), 0.4, fc='white')
            fig.gca().add_artist(center_circle)
            st.pyplot(fig)
    
        # Visualization for Attrition Rate by WorkLifeBalance (Bar plot)
        with col2:
            st.info("### Attrition Rate by WorkLifeBalance")
            new_df = data[data["Attrition"] == "Yes"]
            value_2 = new_df["WorkLifeBalance"].value_counts()
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.barplot(x=value_2.index.tolist(), y=value_2.values, order=value_2.index, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"], ax=ax)
    
            # Add text annotations for each bar
            for index, value in enumerate(value_2.values):
                ax.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", fontweight="black", size=10)
            
            st.pyplot(fig)
    
    else:
        st.info("Please upload a CSV file to start the analysis.")
      
with st.sidebar:
  st.header('Input Features')
  Age = st.slider("Age", min_value=18, max_value=60, value=25)
  st.write(f"Your selected option: {Age}.")

  gender = st.selectbox("Gender", ["Male", "Female"])
  marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])

  Gender_options = ["Male", "Female"]
  selected_gender = st.pills("Gender", Gender_options, selection_mode="single")
  Gender = selected_gender[0] if selected_gender else None  # Handle empty selection
  st.markdown(f"Your selected Gender: {selected_gender}.")

  MaritalStatus_options = ["Single", "Married", "Divorced"]
  selected_marital_status = st.pills("Marital Status", MaritalStatus_options, selection_mode="single")
  MaritalStatus = selected_marital_status[0] if selected_marital_status else None  # Handle empty selection
  st.markdown(f"Your selected Marital Status: {selected_marital_status}.")

  #Gender = ["Male", "Female"]
  #selection = st.pills("Gender", Gender, selection_mode="single")
  #st.markdown(f"Your selected option: {selection}.")

  #MaritalStatus = ["Single", "Married", "Divorced"]
  #selection = st.pills("Marital Status", MaritalStatus, selection_mode="single")
  #st.markdown(f"Your selected option: {selection}.")
  
  options = ["Bachelor", "Master", "Doctor", "College", "Below College"]
  selection = st.pills("Education", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")

  options = ["Life Science", "Medical", "Marketing", "Technical Degree", "Other", "Human Resources"]
  selection = st.pills("Education FIeld", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")

  options = ["Research & Development", "Sales Department", "Human Resources"]
  selection = st.pills("Department", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")

  options = ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"]
  selection = st.pills("Job Role", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")

  options = ["Entry Level", "Junior Level", "Mid Level", "Senior Level", "Executive Level"]
  selection = st.pills("Job Level", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")
  
  options = ["Non-Travel", "Travel Rarely", "Travel Frequently"]
  selection = st.pills("Business Travel", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")
  
  options = ["Low", "Medium", "High", "Very High"]
  selection = st.pills("Job Satisfaction", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")
  
  options = ["Yes", "No"]
  selection = st.pills("Over Time", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")

  options = ["Excellent", "Outstanding"]
  selection = st.pills("Performance Rating", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")

  options = ["Good", "Best", "Better", "Bad"]
  selection = st.pills("Work Life Balance", options, selection_mode="single")
  st.markdown(f"Your selected option: {selection}.")
