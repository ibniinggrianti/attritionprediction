import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Attrition Prediction')

st.info("Is your job worth keeping? Should you stay? Or just leave? Let's try!")

#with st.expander('Data'):
  #df = pd.read_csv('https://raw.githubusercontent.com/ibniinggrianti/attritionprediction/refs/heads/master/IBM-HR-Analytics-Employee-Attrition-and-Performance-Revised.csv')
  #df
# Ignore warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

# Load dataset (Ensure the CSV file is in the correct location)
data = pd.read_csv("https://raw.githubusercontent.com/ibniinggrianti/attritionprediction/refs/heads/master/IBM-HR-Analytics-Employee-Attrition-and-Performance-Revised.csv")  # Replace with your actual CSV file name

 # Visualization: Total Employees by TotalWorkingYearsGroup
    if "TotalWorkingYearsGroup" in data.columns:
        st.write("### Employees by Total Working Years Group")
        value_1 = data["TotalWorkingYearsGroup"].value_counts()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.pie(
            value_1.values,
            labels=value_1.index,
            autopct="%.1f%%",
            pctdistance=0.75,
            startangle=90,
            colors=['#E84040', '#E96060', '#E88181', '#E7A1A1'],
            textprops={"fontweight": "black", "size": 15}
        )
        center_circle = plt.Circle((0, 0), 0.4, fc='white')
        fig.gca().add_artist(center_circle)
        plt.title("Employees by Total Working Years Group", fontweight="black", size=20, pad=20)
        st.pyplot(fig)
    else:
        st.warning("Column 'TotalWorkingYearsGroup' not found in the dataset.")

    # Visualization: Attrition Rate by TotalWorkingYearsGroup
    if "Attrition" in data.columns and "TotalWorkingYearsGroup" in data.columns:
        st.write("### Attrition Rate by Total Working Years Group")
        new_df = data[data["Attrition"] == "Yes"]
        value_2 = new_df["TotalWorkingYearsGroup"].value_counts()
        if not value_1.empty:
            attrition_rate = np.floor((value_2 / value_1) * 100).values
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(
                x=value_2.index.tolist(),
                y=value_2.values,
                palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"],
                ax=ax
            )
            ax.set_title("Attrition Rate by Total Working Years", fontweight="black", size=20, pad=20)
            for index, value in enumerate(value_2):
                ax.text(
                    index, value, f"{value} ({int(attrition_rate[index])}%)",
                    ha="center", va="bottom", size=15, fontweight="black"
                )
            st.pyplot(fig)
        else:
            st.warning("No data available for visualization.")
    else:
        st.warning("Required columns 'Attrition' or 'TotalWorkingYearsGroup' not found in the dataset.")
else:
    st.info("Please upload a CSV file to start the analysis.")

with st.expander('Data Visualization'):
  # Sidebar Filters for Interactivity
  st.sidebar.title("Filters")
  st.sidebar.subheader("Choose Filters to Explore Data")
  selected_group = st.sidebar.multiselect(
      "Select Total Working Years Groups:",
      options=data["TotalWorkingYearsGroup"].unique(),
      default=data["TotalWorkingYearsGroup"].unique()
  )
  
  # Filter Data Based on User Input
  filtered_data = data[data["TotalWorkingYearsGroup"].isin(selected_group)]
  
  # Title
  st.title("Employee Attrition Analysis")
  
  # Visualization: Total Employees by TotalWorkingYearsGroup
  st.subheader("Employees by Total Working Years Group")
  fig1, ax1 = plt.subplots(figsize=(7, 7))
  value_1 = filtered_data["TotalWorkingYearsGroup"].value_counts()
  ax1.pie(
      value_1.values, 
      labels=value_1.index, 
      autopct="%.1f%%", 
      pctdistance=0.75, 
      startangle=90,
      colors=['#E84040', '#E96060', '#E88181', '#E7A1A1'], 
      textprops={"fontweight": "bold", "fontsize": 12}
  )
  ax1.set_title("Employees by Total Working Years", fontweight="bold", fontsize=16)
  center_circle = plt.Circle((0, 0), 0.4, fc='white')
  fig1.gca().add_artist(center_circle)
  st.pyplot(fig1)
  
  # Visualization: Attrition Rate by TotalWorkingYearsGroup
  st.subheader("Attrition Rate by Total Working Years Group")
  fig2, ax2 = plt.subplots(figsize=(10, 6))
  new_df = filtered_data[filtered_data["Attrition"] == "Yes"]
  value_2 = new_df["TotalWorkingYearsGroup"].value_counts()
  attrition_rate = np.floor((value_2 / value_1) * 100).fillna(0).values
  sns.barplot(
      x=value_2.index.tolist(), 
      y=value_2.values, 
      palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"], 
      ax=ax2
  )
  ax2.set_title("Attrition Rate by Total Working Years", fontweight="bold", fontsize=16)
  ax2.set_xlabel("Total Working Years Group", fontweight="bold")
  ax2.set_ylabel("Number of Attritions", fontweight="bold")
  for index, value in enumerate(value_2):
      ax2.text(
          index, 
          value, 
          f"{value} ({int(attrition_rate[index])}%)", 
          ha="center", 
          va="bottom", 
          fontsize=12, 
          fontweight="bold"
      )
  st.pyplot(fig2)
