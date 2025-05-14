import pandas as pd
import streamlit as st

st.title("📘 오늘의 SRS 카드")

# CSV 불러오기
url = "https://raw.githubusercontent.com/Pkms01/rop-srs-app/main/data/day01.csv"

try:
    df = pd.read_csv(url)

    for idx, row in df.iterrows():
        st.markdown(f"### Q{row['id']}. {row['question']}")
        with st.expander("정답 보기"):
            st.success(row['answer'])
        st.caption(f"태그: {row['tag']}")
        st.markdown("---")

except Exception as e:
    st.error("카드 불러오기에 실패했습니다. 인터넷 연결 또는 파일 경로를 확인해 주세요.")
    st.exception(e)
