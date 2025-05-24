
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Dự án", layout="wide")

st.title("📊 Dashboard Dự án - Demo")

# Nhập dữ liệu
st.sidebar.header("📝 Nhập dữ liệu")
with st.sidebar.form("form_input"):
    bo_phan = st.selectbox("Bộ phận", ["Design", "Automation", "Customer", "QA", "Production"])
    tinh_trang = st.selectbox("Tình trạng", ["Done", "Doing", "Not yet", "No need"])
    thang = st.number_input("Tháng", min_value=1, max_value=12, value=5)
    nam = st.number_input("Năm", min_value=2020, max_value=2030, value=2025)
    submit = st.form_submit_button("Thêm")

# Lưu dữ liệu tạm thời trong session
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Bộ phận", "Tình trạng", "Tháng", "Năm"])

if submit:
    new_row = pd.DataFrame([[bo_phan, tinh_trang, thang, nam]], columns=st.session_state.data.columns)
    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)

# Hiển thị bảng dữ liệu
st.subheader("📋 Dữ liệu dự án đã nhập")
st.dataframe(st.session_state.data)

# Biểu đồ
if not st.session_state.data.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔍 Dự án theo bộ phận")
        fig, ax = plt.subplots()
        st.session_state.data["Bộ phận"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

    with col2:
        st.markdown("### ✅ Tình trạng dự án")
        fig2, ax2 = plt.subplots()
        st.session_state.data["Tình trạng"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax2)
        st.pyplot(fig2)
