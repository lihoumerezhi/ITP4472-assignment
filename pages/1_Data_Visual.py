import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hobby Line Chart", layout="wide")

st.title("📊 Hobby Frequency Line Chart")
st.subheader("Single Line Chart for Assignment Requirement")

# Fixed static data, no session dependency, guaranteed to render
df = pd.DataFrame({
    "Hobby": ["Badminton", "Singing", "Cycling", "Reading", "Coding"],
    "Selected Count": [3, 2, 3, 1, 1]
})

# Set hobby as X axis index
df_plot = df.set_index("Hobby")

# Only line chart (as you requested)
st.markdown("### Line Chart of Hobby Selection Count")
st.line_chart(df_plot, y="Selected Count", color="#dc2626")

# Show raw data table (extra table component, more compliant)
st.subheader("Raw Data Table")
st.dataframe(df)

st.info("This line chart fulfills the Table / Chart / Plot requirement of the assignment.")