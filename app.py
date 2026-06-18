import streamlit as st
import pandas as pd
from PIL import Image

# Global page configuration
st.set_page_config(page_title="Self Introduction", page_icon="👤", layout="wide")

# Global beautify CSS
st.markdown("""
<style>
html {font-size: 16px;}
.card-box {
    background-color: #f8fafc;
    padding: 20px 25px;
    border-radius: 12px;
    margin: 10px 0;
    border: 1px solid #d8e2f0;
}
.main-divider {
    height: 3px !important;
    background-color: #94a3b8 !important;
    margin: 25px 0 !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize session storage
if "user_info" not in st.session_state:
    st.session_state.user_info = {
        "name": "LIHOU Merezhi",
        "school": "Hong Kong Institute of Information Technology",
        "major": "Data Science and Artificial Intelligence",
        "hobbies": ["Badminton", "Singing", "Cycling"]
    }

# Left sidebar navigation
with st.sidebar:
    st.header("🧭 Page Navigation")
    st.info("ITP4472 Individual Streamlit Assignment")
    st.write("🏠 Homepage - Personal Info")
    st.write("📊 Page 2 - Hobby Chart")
    st.write("💾 Page 3 - Download Text File")
    st.divider()
    st.warning("📅 Submission Deadline: 18 June 2026")

# Page title
st.title("👋 Personal Self-Introduction")
st.header("📌 ITP4472 Streamlit Assignment")
st.markdown('<hr class="main-divider">', unsafe_allow_html=True)

# Module 1: Avatar + Self Introduction
st.markdown('<div class="card-box">', unsafe_allow_html=True)
img_col, text_col = st.columns([0.25, 0.75])
with img_col:
    try:
        # First try local absolute path for your computer
        avatar = Image.open(r"C:\MyAssignment\avatar.png")
        st.image(avatar, caption="My Profile Photo", width=170)
    except:
        try:
            # Fallback relative path for cloud deployment
            avatar = Image.open("avatar.png")
            st.image(avatar, caption="My Profile Photo", width=170)
        except FileNotFoundError:
            st.error("Missing avatar.png, please check the file storage path!")

with text_col:
    st.subheader("🙋 About Me")
    st.write("""
Hello everyone, my name is LIHOU Merezhi. I come from an ethnic minority region in Sichuan. I am outgoing and optimistic, and I am passionate about life. My undergraduate major is Data Science and Artificial Intelligence.
""")
    st.write("Python and artificial intelligence programming are the core of my current studies. This interactive web page is a practical assignment for the ITP4472 module.")
    st.info("My hobbies: Badminton, cycling and singing.")
st.markdown('</div>', unsafe_allow_html=True)

# Module 2: Expandable study content
with st.expander("📖 My Study Goals & Daily Life", expanded=False):
    st.write("1. Academic Goal: Master Python data analysis and basic AI model development.")
    st.write("2. Interest: Build interactive data visualization tools based on Streamlit.")
    st.write("3. Daily Life: Keep exercising and listen to music to release pressure.")

st.markdown('<hr class="main-divider">', unsafe_allow_html=True)

# Module 3: Personal information editing area
st.markdown('<div class="card-box">', unsafe_allow_html=True)
st.subheader("✏️ Edit Personal Information")
name = st.text_input("Full Name", value=st.session_state.user_info["name"], placeholder="Please enter your full name")
school = st.text_input("School", value=st.session_state.user_info["school"], placeholder="Your university name")
major = st.text_input("Major", value=st.session_state.user_info["major"], placeholder="Your academic major")
st.markdown('</div>', unsafe_allow_html=True)

# Module 4: Hobby selection + Save / Reset buttons
st.subheader("🎯 Select Your Hobbies")
hobby_area, save_area, reset_area = st.columns([0.72, 0.13, 0.13])
with hobby_area:
    c1 = st.checkbox("Badminton", value="Badminton" in st.session_state.user_info["hobbies"])
    c2 = st.checkbox("Singing", value="Singing" in st.session_state.user_info["hobbies"])
    c3 = st.checkbox("Reading")
    c4 = st.checkbox("Coding")
    c5 = st.checkbox("Cycling", value="Cycling" in st.session_state.user_info["hobbies"])

with save_area:
    save_btn = st.button("Save", use_container_width=True, type="primary")
with reset_area:
    reset_btn = st.button("Reset", use_container_width=True)

# Collect selected hobbies
hobby_list = []
if c1: hobby_list.append("Badminton")
if c2: hobby_list.append("Singing")
if c3: hobby_list.append("Reading")
if c4: hobby_list.append("Coding")
if c5: hobby_list.append("Cycling")

# Save logic
if save_btn:
    if name.strip() == "":
        st.error("Name cannot be empty! Please fill in your full name.")
    else:
        st.session_state.user_info["name"] = name
        st.session_state.user_info["school"] = school
        st.session_state.user_info["major"] = major
        st.session_state.user_info["hobbies"] = hobby_list
        st.toast("Data saved successfully!", icon="✅")
        st.balloons()

# Reset logic
if reset_btn:
    st.session_state.user_info = {
        "name": "LIHOU Merezhi",
        "school": "Hong Kong Institute of Information Technology",
        "major": "Data Science and Artificial Intelligence",
        "hobbies": ["Badminton", "Singing", "Cycling"]
    }
    st.toast("All data has been reset!", icon="🔄")

st.markdown('<hr class="main-divider">', unsafe_allow_html=True)

# Quick download on homepage
st.subheader("💡 Quick Download Introduction Text")
if st.session_state.user_info["name"].strip():
    info = st.session_state.user_info
    download_text = f"""
==================== PERSONAL SELF-INTRODUCTION ====================
Name: {info["name"]}
School: {info["school"]}
Major: {info["major"]}
Hobbies: {", ".join(info["hobbies"])}

Self Description:
Hello everyone, my name is LIHOU Merezhi. I come from an ethnic minority region in Sichuan. I am outgoing and optimistic, and I am passionate about life.
My undergraduate major covers Data Science and Artificial Intelligence. Python and AI programming form the core of my current learning content. This interactive web page serves as my coursework assignment for ITP4472.
My daily hobbies are badminton, cycling and singing.
================================================================
ITP4472 Streamlit Assignment
"""
    st.download_button(
        label="Download TXT File Directly",
        data=download_text,
        file_name=f"{info['name']}_SelfIntro.txt",
        mime="text/plain",
        type="primary"
    )
else:
    st.warning("Please fill in your name and save personal data before downloading!")

# Bottom prompt
st.divider()
if name.strip():
    st.success(f"Welcome, {name}!")
st.info("💡 Expand the left sidebar to view hobby chart and independent download page.")