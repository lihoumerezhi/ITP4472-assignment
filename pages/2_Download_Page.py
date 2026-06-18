import streamlit as st

st.set_page_config(page_title="Independent Download Page", layout="wide")
st.title("📄 Independent Introduction Download Page")

user_data = st.session_state.user_info

full_text = f"""
==================== FULL PERSONAL INTRODUCTION ====================
Full Name: {user_data["name"]}
University: {user_data["school"]}
Major: {user_data["major"]}
Selected Hobbies: {", ".join(user_data["hobbies"])}

Self Introduction Content:
Hello everyone, my name is LIHOU Merezhi. I am an undergraduate student majoring in Data Science and Artificial Intelligence.
This multi-page Streamlit website is my complete submission for the ITP4472 course assignment.
My regular leisure activities include badminton, cycling and singing.
====================================================================
ITP4472 Streamlit Assignment Submission
"""

st.subheader("Text Preview Area")
st.text_area("Preview Content", full_text, height=350, disabled=True)

st.download_button(
    label="Download Complete Introduction TXT File",
    data=full_text,
    file_name=f"{user_data['name']}_Full_Intro.txt",
    mime="text/plain",
    type="primary"
)

st.warning("Return to homepage and click Save to synchronize updated personal information.")