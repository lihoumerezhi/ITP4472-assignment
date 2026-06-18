import streamlit as st

st.set_page_config(page_title="Download File Page", page_icon="💾")
st.title("💾 Download Your Personal Introduction File")
st.divider()

if "user_info" not in st.session_state or st.session_state.user_info["name"] == "":
    st.error("You haven’t saved your personal information yet! Return to the main page to fill in details.")
else:
    info = st.session_state.user_info
    # 拼接文本内容
    file_text = f"""
==================== PERSONAL INTRODUCTION ====================
Name: {info["name"]}
Major: {info["major"]}
Age: {info["age"]}
Gender: {info["gender"]}
Hobbies: {", ".join(info["hobbies"]) if info["hobbies"] else "None"}

Self Description:
{info["self_desc"]}
===============================================================
Assignment: ITP4472 Streamlit Self Introduction
"""
    # 8. Download files 下载功能
    st.download_button(
        label="Download TXT Introduction File",
        data=file_text,
        file_name=f"{info['name']}_Self_Introduction.txt",
        mime="text/plain"
    )
    st.toast("File ready to download!", icon="📁")