import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 제목 설정
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

# a가 0일 경우, 이차함수가 아님을 알림 (슬라이더에서 0을 완전히 피하기 어려울 수 있으므로)
if a == 0:
    st.warning("경고: $a$ 값이 0이면 $y=0$으로, 이는 이차함수가 아닌 **직선** 그래프입니다.")
    a = 0.001 # 그래프를 그리기 위해 0에 매우 가까운 값으로 대체

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

# x, y 축 원점 표시 (눈금선 대신)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)

# 그래프 범위 설정
ax.set_xlim([-5, 5])
# y 축 범위는 a 값에 따라 동적으로 설정하는 것이 좋으나, 여기서는 적절한 범위로 고정
ax.set_ylim([-10, 10])

ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# Streamlit에 그래프 표시
st.pyplot(fig)

st.markdown('---')

## 📊 그래프 분석 결과

### 1. 그래프의 모양 (볼록성)

$a$ 값에 따라 그래프가 어떻게 볼록한지 확인해 보세요.
* $a > 0$ (**양수**): 그래프가 **아래로 볼록** (컵 모양)합니다. $\rightarrow$ 최소값은 꼭짓점에서 가집니다.
* $a < 0$ (**음수**): 그래프가 **위로 볼록** (산 모양)합니다. $\rightarrow$ 최대값은 꼭짓점에서 가집니다.

### 2. 그래프의 폭

$a$ 값의 **절댓값** $|a|$의 크기에 따라 그래프의 폭을 비교해 보세요.
* $|a|$ 값이 **클수록** (예: 4.0, -4.0): 그래프의 폭이 **좁아집니다** (y축에 가까워집니다).
* $|a|$ 값이 **작을수록** (예: 0.5, -0.5): 그래프의 폭이 **넓어집니다** (x축에 가까워집니다).

이 코드를 통해 사용자는 $a$ 값을 바꿔가며 **이차함수의 볼록성과 폭**을 시각적으로 확인하고 원하는 결론을 **귀납적으로 추론**할 수 있을 것입니다.

---
이 영상은 $y=ax^2$ 형태의 이차함수 그래프 실습을 위한 데스모스(Desmos) 사이트 활용법을 보여줍니다.
[Graph Practice: Graph of the Quadratic Function y=ax^2](https://www.youtube.com/watch?v=bTX4HCwIX_Q)
http://googleusercontent.com/youtube_content/0
