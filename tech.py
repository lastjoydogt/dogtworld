import streamlit as st
import os
# from dotenv import load_dotenv
# load_dotenv("pass.env")

# streamlit run tech.py

st.set_page_config(
    page_title="화성 갈끄니까까",
)

SECRET_KEY = 'dogt'

##############################################
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated: # 아직 인증 안 됐으면 비밀번호 입력 창 보여주기
    st.title("🔐 비밀번호를 입력하세요!!")
    password = st.text_input("비밀번호", type="password")
    if st.button("LOGIN"):
        if password == SECRET_KEY:
            st.session_state.authenticated = True
            st.success("✅ 인증 성공! 메인 페이지로 이동합니다.")
            st.rerun()  # 다시 실행해서 페이지를 새로 그림
        else:
            st.error("❌ 비밀번호가 틀렸습니다.")
else:
    # 인증된 상태에서는 메인 페이지 보여주기
    page = "🏠 MAIN"  # 여기에 다른 페이지 선택 로직을 추가해도 돼
    if page == "🏠 MAIN":
        ### 과락이 ###
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if st.button("🔄 RESET "):
            st.session_state.score = 0


        st.write(f"종목평가: **{st.session_state.score}점**")

        options = ["-40%↓", "-40~-50%", "-50%↑"]
        selection = st.segmented_control("최고점 하락값 [52주]", options, selection_mode="single")
        if selection == "-40%↓":
            lowScore = 0
        elif selection == "-40~-50%":
            lowScore = 10
        elif selection == "-50%↑":
            lowScore = 15
        else:
            lowScore = 0

        col1, col2 = st.columns(2)
        with col1:
            st.write("일봉상 CHART STATUS!!")

            stoneScore = 0
            stone = st.checkbox("전고점 하락(돌지10)")
            if stone == True:
                options = ["10일↑", "10일↓"]
                selection2 = st.segmented_control("최고점 하락값", options, selection_mode="single")
                if selection2 == "-10일↑":
                    stoneScore = 0
                elif selection2 == "10일↓":
                    stoneScore = 10
                else:
                    stoneScore = 0

            tenDateLine = st.toggle("10 LINE 돌파 ↑")
            if tenDateLine == True:
                tenDateScore = 5
            else:
                tenDateScore = 0

            twentyDateLine = st.toggle("20 LINE 돌파 ↑")
            if twentyDateLine == True:
                pass
            
            reverseScore = 0
            reverseLine = st.toggle("REVERSE")
            if reverseLine == True:
                if tenDateLine == True:
                    if twentyDateLine == True:
                        reverseScore = 10
                    else:
                        reverseScore = 0    

        if st.button("✅ 확인"):
            st.session_state.score = lowScore + tenDateScore + reverseScore + stoneScore
            st.rerun()



        # #######분봉 체크#####
        # with col2:
        #     st.write("분봉상 CHART CHECK !!")
        #     option_map = {
        #     0: "오전",
        #     1: "점심",
        #     2: "오후",}
        #     selection = st.pills("수급시간",
        #         options=option_map.keys(),
        #         format_func=lambda option: option_map[option],
        #         selection_mode="single",)
            
        #     minuteFirstLow = st.checkbox("1차 하락")
        #     if minuteFirstLow == True:
        #         minuteSecondHigh = st.checkbox("2차 상승")