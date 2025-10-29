import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(page_title='이차함수 그래프 분석기', layout='wide')
st.title('이차함수의 그래프 기본형 ($y=ax^2$) 분석하기 🧐')
st.markdown("""
**$y=ax^2$** 그래프에서 **$a$ 값**의 변화에 따라 그래프가 어떻게 바뀌는지 직접 탐색해 보세요.
""")

st.markdown('---')

# a 값 입력을 위한 슬라이더 (0.0은 건너뛰도록 설정)
a_values = np.concatenate((np.arange(-5.0, 0.0, 0.1), np.arange(0.1, 5.1, 0.1)))
a_list = [round(val, 1) for val in a_values]

# 슬라이더 대신 selectbox를 사용해 0을 명확히 제외
a = st.selectbox(
    '**$a$ 값 선택하기** (a=0 제외)',
    options=a_list,
    index=a_list.index(1.0) # 기본 a 값
)

# x 값 범위 설정 및 계산
x = np.linspace(-5, 5, 100)
y = a * x**2

# Streamlit 차트 사용을 위한 Pandas DataFrame 생성
df = pd.DataFrame({
    'x': x,
    f'y = {a:.1f}x^2': y
})

# 그래프 영역 지정
st.subheader(f'이차함수 그래프: $y = {a:.1f}x^2$')

# Streamlit 기본 라인 차트 표시
# x축을 인덱스 대신 'x' 컬럼으로 명시
st.line_chart(df.set_index('x'))

st.markdown('---')

## 📊 그래프 분석 결과

st.header('📊 그래프 분석을 통한 귀납적 추론')

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 1. 그래프의 모양 (볼록성) 확인")
    st.markdown(f"""
    선택한 $a={a:.1f}$ 값에 따라 그래프의 모양을 확인합니다.
    * $a > 0$ (**양수**)일 때: 그래프는 **아래로 볼록** (최소값 존재)합니다. 
    * $a < 0$ (**음수**)일 때: 그래프는 **위로 볼록** (최대값 존재)합니다. 
    """)

with col2:
    st.markdown("### 2. 그래프의 폭 확인 ( $|a|$의 영향)")
    abs_a = abs(a)
    st.markdown(f"""
    $a$ 값의 **절댓값** $|a| = |{abs_a:.1f}|$의 크기에 따라 폭을 비교해 보세요.
    * $|a|$ 값이 **클수록** (예: 4.0, -4.0): 그래프의 폭이 **좁아집니다** (y축에 가깝습니다).
    * $|a|$ 값이 **작을수록** (예: 0.5, -0.5): 그래프의 폭이 **넓어집니다** (x축에 가깝습니다).
    """)
