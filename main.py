import streamlit as st

st.set_page_config(
    page_title="急性眩晕患者卒中预警算法研究",
    page_icon="🏥",
    layout="wide"
)

# 创建侧边栏
with st.sidebar:
    # 背景知识下拉菜单
    with st.expander("背景", expanded=True):
        st.page_link("pages/background.py", label="急诊中的眩晕情况")
        st.page_link("pages/HINTS_STANDING.py", label="HINTS & STANDING")
        st.page_link("pages/nystagmus.py", label="眼震检查")
        st.page_link("pages/hit.py", label="头脉冲检查")
        st.page_link("pages/test_of_skew.py", label="眼位偏斜检查")
    
    # 目前进展下拉菜单
    with st.expander("目前进展", expanded=True):
        st.page_link("pages/progress.py", label="研究进展")



