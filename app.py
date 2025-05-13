import streamlit as st

st.set_page_config(page_title="SRS AI 데모", page_icon="📚")

st.title("📚 SRS AI 고정 배포 테스트")
st.write("이 앱은 Streamlit Cloud에 고정 URL로 배포 가능한 템플릿입니다.")

st.header("🔑 API Key 테스트")
api_key = st.secrets.get("GEMINI_API_KEY", "API 키가 설정되지 않았습니다.")
st.code(api_key)