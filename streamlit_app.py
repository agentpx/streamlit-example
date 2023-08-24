import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from Seaborn
@st.cache
def load_data():
    iris = sns.load_dataset("iris")
    return iris

iris_data = load_data()

# Streamlit App
st.title("Iris Dataset Scatter Plot")

# Sidebar
st.sidebar.header("Select Sepal and Petal Characteristics")
x_axis = st.sidebar.selectbox("X-axis", options=iris_data.columns[:-1])
y_axis = st.sidebar.selectbox("Y-axis", options=iris_data.columns[:-1])

# Scatter Plot
fig, ax = plt.subplots()
sns.scatterplot(data=iris_data, x=x_axis, y=y_axis, hue='species', ax=ax)
st.pyplot(fig)

# Display Data Table
st.write("Iris Dataset (First 10 Rows)")
st.write(iris_data.head(10))
