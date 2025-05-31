import streamlit as st
# import streamlit.components.v1 as components
import os
# from dotenv import load_dotenv
# load_dotenv("pass.env")

# streamlit run tech2.py

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
    page = "🏠 MAIN"
    if page == "🏠 MAIN":
        def technical(king,selection,tenDateLine,LowSelection,beforeHigher,beforeHigherCheck,reverseLine,jumpuLine,hightime,minmove3,minResult,LowAgree
                      ,minLimitHigh2):
            techName = ''

            kingScore = 0
            if king == True:
                kingScore = 20

            lowScore = 0
            if selection == "-40%↓":
                lowScore = 0
            elif selection == "-40~-50%":
                lowScore = 5
            elif selection == "-50%↑":
                lowScore = 10
                techName = '[과락이]'

            tenDateScore = 0
            if tenDateLine == True and "10일선↓" in LowSelection and beforeHigher == "↓":
                tenDateScore = 20
            elif tenDateLine == True and "10일선↓" in LowSelection and beforeHigher == "↑" and beforeHigherCheck == True:
                tenDateScore = 15
            elif tenDateLine == True and "10일선↓" in LowSelection: ## 범용...
                tenDateScore = 10

            ## 역단이
            reverseScore = 0
            techName2 = ''
            if reverseLine == True:
                if tenDateLine == True and twentyDateLine == True and selection == "-50%↑" and beforeHigher == '↓'and "10일선↓" in LowSelection:
                    reverseScore = 15 ## 역단이 최종 70점
                    techName2 = '[역단이]'
                elif tenDateLine == True and twentyDateLine == True and beforeHigher == '↓'and "10일선↓" in LowSelection:
                    reverseScore = 10 ## 역단이 최종 55점
                    techName2 = '[역단이]'
                elif tenDateLine == True and twentyDateLine == True and selection == "-50%↑" and LowAgree == False:
                    reverseScore = 15
                    techName2 = '[역단이]'
                elif tenDateLine == True and twentyDateLine == False:
                    reverseScore = 0

            ##갭상이
            techName4 = ''
            jumpScore = 0
            if jumpuLine == True:
                jumpScore = 10
            if minLimitHigh2 == "저점유지 후 상승" and jumpuLine == True:
                techName4 = '[갭상이]'
                jumpScore = 30

            ## 수급시간
            hightimeScore = 0
            if hightime == '오전수급':
                hightimeScore = 15
            elif hightime == '오후수급':
                hightimeScore = - 20


            #돌지10
            techName3 = ''
            if LowAgree == True:
                if beforeHigherCheck == True and "고점돌파 후 하락" in minmove3 and minResult == '상승추세' and tenDateLine == True and "10일선↓" in LowSelection:
                    techName3 = '[돌파 돌지10]'
                    if king == True:
                        kingScore = 30
                    elif king == False:
                        kingScore = -30
                elif tenDateLine == True and "10일선↓" in LowSelection:
                        techName3 = '[돌지10]'


            ##1차 상승
            techName5 =''
            fisthighScore = 0
            if minmove2 == '1차하락' and minResult == '하락추세':
                fisthighScore = 10
                techName5 = '[1차상승(분)]'

            ## 수급시간
            if hightime == '오전수급':
                hightimeScore = 15
            elif hightime == '오후수급':
                hightimeScore = - 20

            minResultScore = 0
            if minResult == '상승추세':
                minResultScore = 10
            elif minResult == '보합추세':
                minResultScore = 5
            elif minResult == '하락추세':
                minResultScore = -10





            TotaltechName = techName + techName2 + techName3 + techName4 + techName5
            TotalScore = kingScore + lowScore + tenDateScore + reverseScore + jumpScore + hightimeScore +minResultScore + fisthighScore
            return TotalScore , TotaltechName
        
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'tech' not in st.session_state:
            st.session_state.tech = " "
        if 'text' not in st.session_state:
            st.session_state.text = "화성 갈끄니까!"
        if 'color' not in st.session_state:
            st.session_state.color = "black"






        colA, colB = st.columns(2)
        with colA:
            st.markdown(
                f"<h3>종목평가 : <span style='color:{st.session_state.color}'>{st.session_state.score}점 😎</span></h3>",
                unsafe_allow_html=True)
        with colB:
            st.markdown(
                f"<h3><span style='color:{st.session_state.color}'>{st.session_state.text}</span></h3>",
                unsafe_allow_html=True)
            
        st.markdown(
            f"<h3><span style='color:{st.session_state.color}'>기술명: {st.session_state.tech}</span></h3>",
            unsafe_allow_html=True)

        king = st.checkbox("대장주")

        options = ["-40%↓", "-40~-50%", "-50%↑"]
        selection = st.segmented_control("최고점 하락값 [6개월]", options, selection_mode="single")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('''**:gray[일봉상 CHART STATUS!!]**''')

            beforeHigherCheck =''

            LowAgree = st.checkbox("돌지10CHART")
            options = ["10일선↓","10일선↑","앞)전고_장대양봉"]
            LowSelection = st.segmented_control("차트변동 추세", options, selection_mode="multi")

            options = ["↓","↑"]
            beforeHigher = st.pills("전고점 대비 상승폭", options, selection_mode="single")
            if beforeHigher == "↑":
                beforeHigherCheck = st.checkbox("52주 신고가")

            tenDateLine = st.toggle("10 LINE 돌파")

            twentyDateLine = st.toggle("20 LINE 돌파")

            reverseLine = st.toggle("REVERSE")

            jumpuLine = st.toggle("시초갭상승")

        with col2:
            st.markdown('''**:gray[분봉상 CHART STATUS!!]**''')
            minmove2 = ''
            hightime =''
            minmove3 = ''
            minLimitHigh2 =''

            options = ["오전수급","오후수급"]
            hightime = st.segmented_control("수급시간", options, selection_mode="single")

            options = ["시초하락","장중하락"]
            minmove = st.segmented_control("분봉움직임", options, selection_mode="single")
            if minmove == "시초하락" :
                minLimitHigh = st.checkbox("시초 돌파 후 하락")
                if minLimitHigh == True:
                    options = ["저점유지 후 상승","저점이탈"]
                    minLimitHigh2 = st.segmented_control("갭상이CHECK", options, selection_mode="single")

            if minmove == '장중하락':
                options = ["1차하락","2차하락"]
                minmove2 = st.segmented_control("차트 변화", options, selection_mode="single")
            if minmove2 == '2차하락':
                options = ["고점돌파 후 하락","저점유지"]
                minmove3 = st.segmented_control("KEY-POINT", options, selection_mode="multi")

            options = ["하락추세","보합추세", "상승추세"]
            minResult = st.segmented_control("3시10분 이후", options, selection_mode="single")

        TotalScore , TotaltechName = technical(king,selection,tenDateLine,LowSelection,beforeHigher,beforeHigherCheck,reverseLine,jumpuLine,hightime,minmove3,minResult,LowAgree
                                               ,minLimitHigh2)

        if st.button("✅ 확인"):
            st.session_state.score = TotalScore
            st.session_state.tech = TotaltechName
            if st.session_state.score >= 90: #90점이상
                st.session_state.text = "님아 안사고 뭐해? 가즈아!!" 
                st.session_state.color = '#ff0000'
            elif st.session_state.score < 90 and st.session_state.score >=80: #80점이상
                st.session_state.text = "이 종목은 살만 할지도...?" 
                st.session_state.color = '#ff0000'
            elif st.session_state.score < 80 and st.session_state.score >=70: #90점이상
                st.session_state.text = "신중히 고민해보자"
                st.session_state.color = '#b04157'
            elif st.session_state.score < 70 and st.session_state.score >=50: #50~70점이상
                st.session_state.text = "이거사면 물리는거야"
                st.session_state.color = 'blue'
            elif st.session_state.score < 50 and st.session_state.score >=10: #0~50점이상
                st.session_state.text = "이 종목을 본다고?? 실화임? "
                st.session_state.color = 'violet'
            elif st.session_state.score == 0: #0~50점이상
                st.session_state.text = "화성갈끄니까!"
                st.session_state.color = 'black'
            st.rerun()

    # if st.button("🔄 초기화"):
    #     st.session_state.clear()
    #     st.rerun()