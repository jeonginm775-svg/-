import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 제목 설정
st.set_page_config(page_title='이차함수 그래프 분석')
st.title('이차함수의 그래프 기본형 ($y=ax^2$) 분석하기 🧐')
st.markdown("""
**$y=ax^2$** 그래프에서 **$a$ 값**의 변화에 따라 그래프가 어떻게 바뀌는지 확인해 보세요.
""")

st.markdown('---')

# a 값 입력을 위한 슬라이더
# a=0인 경우는 이차함수가 아니므로 a=0을 제외한 범위로 설정합니다.
a = st.slider(
    '**$a$ 값 선택하기**', 
    min_value=-5.0, # 최소 a 값
    max_value=5.0,  # 최대 a 값
    value=1.0,      # 기본 a 값
    step=0.1        # a 값 변경 단위
)

# a가 0일 경우, 이차함수가 아님을 알림 및 대체
if abs(a) < 0.05: # 0에 아주 가까운 값도 0으로 간주
    st.warning("경고: $|a|$ 값이 0에 가까우면 $y=0$으로, 이는 이차함수가 아닌 **직선** 그래프에 가깝습니다.")
    # 그래프를 그리기 위해 0을 방지하는 아주 작은 값으로 대체
    a = 0.1 if a >= 0 else -0.1 

# x 값 범위 설정
x = np.linspace(-5, 5, 100)
# 이차함수 y = ax^2 계산
y = a * x**2

# Matplotlib 그래프 생성
fig, ax = plt.subplots(figsize=(8, 5))

# 그래프 그리기
ax.plot(x, y, label=f'$y = {a:.1f}x^2$', color='blue')

# 축 및 제목 설정
ax.set_title(f'이차함수 $y = {a:.1f}x^2$ 그래프')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# x, y 축 원점 표시
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)

# 그래프 범위 설정
ax.set_xlim([-5, 5])
ax.set_ylim([-10, 10])

ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# Streamlit에 그래프 표시
st.pyplot(fig)

st.markdown('---')

## 📊 그래프 분석 결과

st.header('📊 그래프 분석 결과')

st.markdown("### 1. 그래프의 모양 (볼록성) 확인")

st.markdown(f"""
선택한 $a={a:.1f}$ 값에 따른 그래프의 모양을 확인해 보세요.
* $a > 0$ (**양수**)일 때: 그래프는 **아래로 볼록** (컵 모양)합니다.
* $a < 0$ (**음수**)일 때: 그래프는 **위로 볼록** (산 모양)합니다.
""")

st.markdown("### 2. 그래프의 폭 확인 ( $|a|$의 영향)")

st.markdown(f"""
$a$ 값의 **절댓값** $|a| = |{a:.1f}|$의 크기에 따라 그래프의 폭을 비교해 보세요.
* $|a|$ 값이 **클수록** (예: 4.0, -4.0): 그래프의 폭이 **좁아집니다** (y축에 가까워집니다).
* $|a|$ 값이 **작을수록** (예: 0.5, -0.5): 그래프의 폭이 **넓어집니다** (x축에 가까워집니다).
""")
