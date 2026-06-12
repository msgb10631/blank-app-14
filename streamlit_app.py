import streamlit as st
import random

# 웹 페이지 제목 설정
st.title("점심 메뉴 추천기 🍕")
st.caption("먹고 싶은 음식 후보를 등록하고, 오늘 점심 메뉴를 추천받아보세요!")

# 1. 세션 상태(session_state)에 음식 목록 저장 공간 초기화
if "food_list" not in st.session_state:
    st.session_state.food_list = []

# 카드가 나뉘는 효과를 주기 위해 영역 분할
with st.container(border=True):
    st.subheader("📌 음식 후보 추가하기")
    
    # 2. 사용자 입력 위젯 (텍스트 입력)
    # 엔터를 누르거나 '추가' 버튼을 누르면 목록에 저장됩니다.
    new_food = st.text_input("음식 이름을 입력하세요:", key="food_input", placeholder="예: 김치찌개, 짜장면")
    
    if st.button("목록에 추가", use_container_width=True):
        if new_food.strip():  # 빈 입력값 방지
            if new_food not in st.session_state.food_list:
                st.session_state.food_list.append(new_food)
                st.toast(f"'{new_food}' 추가 완료!")
            else:
                st.warning("이미 등록된 음식입니다.")
        else:
            st.error("음식 이름을 입력해 주세요.")



# 3. 데이터 표시 및 추천 영역
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 현재 후보 목록")
    if st.session_state.food_list:
        # 리스트를 깔끔하게 DataFrame 형태로 보여줍니다.
        st.dataframe(st.session_state.food_list, column_config={"value": "음식명"}, use_container_width=True)
        
        # 목록 초기화 버튼
        if st.button("목록 전체 삭제", type="secondary"):
            st.session_state.food_list = []
            st.rerun()
    else:
        st.info("아직 등록된 음식이 없습니다.")

with col2:
    st.subheader("🎲 오늘의 메뉴 추천")
    if st.session_state.food_list:
        # 4. 메뉴 추천 로직 (기존 random.choice 유지)
        if st.button("메뉴 골라주기! ✨", type="primary", use_container_width=True):
            result = random.choice(st.session_state.food_list)
            st.success(f"오늘의 추천 메뉴는 바로... **{result}** 입니다! 🎉")
            st.balloons()  # 축하하는 풍선 애니메이션 효과
    else:
        st.write("후보 목록에 음식을 먼저 추가해 주세요.")
