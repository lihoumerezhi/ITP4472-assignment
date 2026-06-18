import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Chart Page", page_icon="📊")
st.title("📊 Hobby Time Distribution Chart")
st.divider()

# 读取首页保存的用户数据
if "user_info" not in st.session_state:
    st.warning("Please fill your info on the home page first!")
else:
    hobby_data = st.session_state.user_info["hobbies"]
    if len(hobby_data) == 0:
        st.info("No hobbies selected, go back to home page to choose hobbies.")
    else:
        # 模拟每周投入时长数据
        data_list = []
        for hobby in hobby_data:
            data_list.append({"Hobby": hobby, "Weekly Hours": st.slider(f"{hobby} weekly hours", 1, 10, 3)})
        chart_df = pd.DataFrame(data_list)
        st.dataframe(chart_df, use_container_width=True)
        # 绘制柱状图 plot
        st.bar_chart(chart_df, x="Hobby", y="Weekly Hours", use_container_width=True)