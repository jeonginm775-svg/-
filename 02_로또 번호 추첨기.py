import streamlit as st
import random
import pandas as pd

# 🍀 로또 번호 생성 함수
def generate_lotto_numbers(num_sets):
    """
    1부터 45 사이의 숫자 중 6개의 숫자를 중복 없이 무작위로 생성합니다.
    """
    results = []
    for i in range(1, num_sets + 1):
        # 1부터 45까지 숫자 중에서 6개를 무작위로 선택하고 정렬
        numbers = sorted(random.sample(range(1, 46), 6))
        # 리스트 형태로 저장
        results.append(numbers)
    return results

# 📊 당첨 번호 비교 함수
def compare_numbers(generated_sets, winning_numbers):
    """
    생성된 번호 세트와 당첨 번호를 비교하여 일치하는 개수를 계산합니다.
    """
    comparison_results = []
    # 당첨 번호 문자열을 정수 리스트로 변환
    try:
        winning_nums = [int(num.strip()) for num in winning_numbers.split(',') if num.strip().isdigit() and 1 <= int(num.strip()) <= 45]
        if len(winning_nums) != 6:
            st.error("❌ 당첨 번호는 1부터 45 사이의 6개 숫자를 쉼표(,)로 구분하여 입력해야 합니다.")
            return None

    except:
        st.error("❌ 당첨 번호 입력 형식이 올바르지 않습니다.")
        return None

    # 각 세트와 당첨 번호 비교
    for i, lotto_set in enumerate(generated_sets):
        # 집합(set)을 이용해 교집합(일치하는 숫자)의 개수를 계산
        matches = len(set(lotto_set).intersection(set(winning_nums)))
        comparison_results.append({
            '세트': f'{i+1} 세트',
            '생성 번호': ' '.join(map(str, lotto_set)),
            '일치 개수': matches
        })

    return comparison_results

# 🚀 스트림릿 앱 구성
def main():
    st.set_page_config(page_title="로또 번호 추천기 🍀", layout="centered")
    st.title('로또 번호 추천기 🍀')
    st.markdown("1부터 45까지의 숫자 중에서 6개의 로또 번호를 무작위로 추천해 드립니다.")
    st.markdown("---")

    ## 1. 번호 생성 설정
    st.header('1️⃣ 번호 생성 설정')
    # 몇 세트 생성할지 선택
    num_sets = st.slider('몇 세트의 번호를 생성하시겠습니까?', 1, 10, 5)

    # 번호 생성 버튼
    if st.button('🚀 번호 생성', type="primary"):
        # 번호 생성 및 세션 상태에 저장
        generated_numbers = generate_lotto_numbers(num_sets)
        st.session_state['generated_numbers'] = generated_numbers
        st.session_state['has_generated'] = True

        st.subheader(f'{num_sets} 세트의 로또 번호')
        
        # 결과를 보기 쉽게 데이터프레임으로 변환
        data = {
            '세트': [f'{i+1} 세트' for i in range(len(generated_numbers))],
            '번호': [' '.join(map(str, numbers)) for numbers in generated_numbers]
        }
        df = pd.DataFrame(data)
        st.dataframe(df, hide_index=True)
        st.success('✅ 번호 생성이 완료되었습니다!')

    st.markdown("---")

    ## 2. 당첨 번호 비교
    # 번호 생성이 완료된 경우에만 비교 기능을 활성화
    if 'has_generated' in st.session_state and st.session_state['has_generated']:
        st.header('2️⃣ 당첨 번호 비교')
        st.info("비교를 위해 최근 로또 당첨 번호 6개를 쉼표(,)로 구분하여 입력해주세요. (예: 1, 10, 20, 30, 40, 45)")

        # 당첨 번호 입력 필드
        winning_numbers_input = st.text_input('최근 로또 당첨 번호 (6개 숫자)', '')

        if st.button('📊 번호 비교'):
            if winning_numbers_input:
                comparison_results = compare_numbers(st.session_state['generated_numbers'], winning_numbers_input)

                if comparison_results:
                    st.subheader('📌 비교 결과')
                    # 결과를 데이터프레임으로 변환하여 표시
                    comparison_df = pd.DataFrame(comparison_results)
                    st.dataframe(comparison_df, hide_index=True)

                    # 일치 개수에 따른 간단한 코멘트
                    max_matches = max(res['일치 개수'] for res in comparison_results)
                    if max_matches == 6:
                        st.balloons()
                        st.success("🎉 **축하합니다!** 6개 모두 일치하는 번호가 있습니다! (이론상 1등!)")
                    elif max_matches >= 4:
                        st.success(f"👍 **{max_matches}개** 일치하는 번호가 있어 당첨 가능성이 높습니다!")
                    elif max_matches > 0:
                        st.info(f"✨ **{max_matches}개**까지 일치하는 번호가 있습니다.")
                    else:
                        st.warning("🥲 아쉽게도 일치하는 번호가 없습니다. 다음 기회에!")

            else:
                st.error("당첨 번호를 입력해주세요.")

# 앱 실행
if __name__ == '__main__':
    main()
