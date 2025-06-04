import streamlit as st
import os
# from dotenv import load_dotenv
# load_dotenv("pass.env")

# streamlit run kabusiki.py

st.set_page_config(
    page_title="화성 갈끄니까까",
)

SECRET_KEY = st.secrets["DB_TOKEN"]
# SECRET_KEY = '1'
##############################################
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated: # 아직 인증 안 됐으면 비밀번호 입력 창 보여주기
    st.title("🔐 비밀번호를 입력하세요!!")
    password = st.text_input("비밀번호", type="password")
    st.caption("1. 10만원만 먹어도 부장급이다")
    st.caption("2. 목표가 도달해서 매도한 종목은 다시 따라 들어가지 말자")
    st.caption("3. 장중 시드 추가 입금 금지")
    st.caption("4. 잘못 샀다고 인지한 즉시 시장가 매도! 반등 기다리다가 망한다")
    st.caption("5. 원하는 종목 없을때 쉴 수 있는 것도 실력이다")
    st.caption("6. 충동적으로 매매, 매도하면 무조건 손해본다")
    st.caption("7. 완벽이란 없다. 자만하지 말자")

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
        def technical(king,selection,tenDateLine,LowSelection,beforeHigher,beforeHigherCheck,reverseLine,jumpuLine,hightime,minmove3,LowAgree
                    ,minLimitHigh2,minmove3_1,reverseLine2,minmove3A):
            
            techNameLow =''
            techNameReverse =''
            techNameGap =''
            techNameFisrt = ''
            techNameGold = ''

            kingScore = 0
            mamoruScore = 0

            if '인기테마' in king and '대장주' in king:
                kingScore = 35
            elif '대장주' in king:
                kingScore = 30


            ## 수급시간
            hightimeScore = 0
            if hightime == ':mostly_sunny:':
                hightimeScore = 20
            elif hightime == ':crescent_moon:':
                hightimeScore = - 20

            ## 일봉 기술
            # 돌지10
            techNameDol10 = ''
            if LowAgree == True:
                if tenDateLine == True and '↑' in beforeHigher and '전)역대 신고가' in beforeHigher:
                    techNameDol10 = '[돌파돌지10]'
                elif tenDateLine == True and '↓' in beforeHigher and '전)역대 신고가' in beforeHigher:
                    techNameDol10 = '[반등돌지10]'
                elif tenDateLine == True and '↓' in beforeHigher and '하락추세 돌파' in beforeHigher:
                    techNameDol10 = '[바닥돌지10]'
            # 과락이
            lowScore = 0
            if selection == "-50%↑":
                techNameLow = '[과락이]'

            #역단이
            if reverseLine2 == True:
                if tenDateLine == True and twentyDateLine == True and reverseLine2 == True:
                    techNameReverse = '[역단이]'

            #갭상이
            if '2차수급後하락' in minLimitHigh2 and '저점유지' in minLimitHigh2 and '2차수급後상승' in minLimitHigh2:
                techNameGap = '[reCheck]'
            elif jumpuLine == True and '2차수급後하락' in minLimitHigh2 and '저점유지' in minLimitHigh2:
                techNameGap = '[갭상이]'

            ## 분봉 기술
            # 1차 상승
            if minmove2 == '1차수급' and minmove3_1 == '後하락':
                techNameFisrt = '[1차상승(분)]'
            # 눌금이,돌금이
            if '1차上돌파' in minmove3 and '後상승' in minmove3 and '後하락' in minmove3:
                techNameGold = '[reCheck]'
            elif '1차上돌파' in minmove3 and '後하락' in minmove3:
                techNameGold = '[눌금이]'
                if minmove3A == '後재상승':
                    techNameGold = '[눌금이+저지]'
                    mamoruScore = 7
                elif minmove3A == '저점유지':
                    techNameGold = '[눌금이+저지]'
                    mamoruScore = 5

            elif '1차上돌파' in minmove3 and '後상승' in minmove3:
                techNameGold = '[돌금이]'




        #### MIX ##########
            mixScore = 0
            techTomorrow = ''
            if techNameDol10 == '[돌파돌지10]' and (techNameFisrt == '[1차상승(분)]' or techNameGold == '[돌금이]'):
                mixScore = 20
                techTomorrow = '관종 후 하루 지켜보자'
            elif techNameDol10 == '[반등돌지10]' and (techNameGold == '[눌금이]' or techNameGold == '[돌금이]' or techNameGold == '[눌금이+저지]' or techNameGold == '[돌금이+저지]'):
                mixScore = 30
            elif techNameDol10 == '[바닥돌지10]' and (techNameGold == '[눌금이]' or techNameGold == '[돌금이]' or techNameGold == '[눌금이+저지]' or techNameGold == '[돌금이+저지]'):
                mixScore = 30
                if techNameLow == '[과락이]':
                    mixScore = mixScore + 10

            if techNameLow == '[과락이]' and (techNameGold == '[눌금이]' or techNameGold == '[돌금이]' or techNameGold == '[눌금이+저지]' or techNameGold == '[돌금이+저지]' or techNameFisrt == '[1차상승(분)]'):
                mixScore = 25

            if techNameReverse == '[역단이]' and (techNameFisrt == '[1차상승(분)]' or techNameGold == '[눌금이+저지]'):
                mixScore = 30
                if techNameLow == '[과락이]':
                    mixScore = mixScore + 10

            if techNameGap == '[갭상이]':
                mixScore = 30

            ## 언덕이.. 1파후2파는 나중에...
            if techNameDol10 == '[바닥돌지10]':
                danger = '※3파동이면 접자'

            TotaltechName = techNameDol10 + techNameLow + techNameReverse + techNameGap + techNameFisrt + techNameGold + techTomorrow + danger
            TotalScore = kingScore + hightimeScore + mixScore + mamoruScore
            return TotalScore , TotaltechName
        
        ##################################################

        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'tech' not in st.session_state:
            st.session_state.tech = " "
        if 'text' not in st.session_state:
            st.session_state.text = "화성 갈끄니까!"
        if 'color' not in st.session_state:
            st.session_state.color = "black"
        if 'imoji' not in st.session_state:
            st.session_state.imoji = "😴"


        colA, colB = st.columns(2)
        with colA:
            st.markdown(
                f"<h3>종목평가 : <span style='color:{st.session_state.color}'>{st.session_state.score}점 {st.session_state.imoji}</span></h3>",
                unsafe_allow_html=True)
        with colB:
            st.markdown(
                f"<h3><span style='color:{st.session_state.color}'>{st.session_state.text}</span></h3>",
                unsafe_allow_html=True)
            
        st.markdown(
            f"<h3><span style='color:{st.session_state.color}'>기술명: {st.session_state.tech}</span></h3>",
            unsafe_allow_html=True)


        if "show" not in st.session_state:
            st.session_state.show = False

        if st.button(":arrows_counterclockwise:"):
            st.session_state.show = not st.session_state.show

        if st.session_state.show:
            options = ["인기테마", "대장주"]
            king = st.segmented_control("대장주??", options, selection_mode="multi")

            options = ["-40%↓", "-40~-50%", "-50%↑"]
            selection = st.segmented_control("최고점 하락값 [6개월]", options, selection_mode="single")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('''**:gray[일봉 CHART!!]**''')

                beforeHigherCheck =''
                LowSelection = ''
                reverseLine2 = ''
                beforeHigher = ''

                LowAgree = st.checkbox("돌지10")
                if LowAgree == True:
                    options = ["10일선↓(지지)","10일선↑"]
                    LowSelection = st.segmented_control("차트변동 추세", options, selection_mode="single")
                    if LowSelection == "10일선↓(지지)":
                        options = ["↓","↑",'전)역대 신고가','하락추세 돌파']
                        beforeHigher = st.pills("전고점 대비 상승폭", options, selection_mode="multi")

                tenDateLine = st.toggle("10 LINE 돌파")
                twentyDateLine = st.toggle("20 LINE 돌파")
                reverseLine = st.toggle("REVERSE")
                if reverseLine == True:
                    reverseLine2 = st.checkbox("하락추세의 양봉")

                jumpuLine = st.toggle("시초갭상승")



            with col2:
                st.markdown('''**:gray[분봉 CHART!!]**''')
                minmove2 = ''
                hightime =''
                minmove3 = ''
                minLimitHigh2 = ''
                minmove3_1 = ''
                minmove3A = ''

                options = [":mostly_sunny:",":crescent_moon:"]
                hightime = st.segmented_control("수급시간", options, selection_mode="single")

                options = ["시초하락","장중하락"]
                minmove = st.segmented_control("분봉움직임", options, selection_mode="single")
                if minmove == "시초하락" :
                    minLimitHigh = st.checkbox("시초 돌파後하락")
                    if minLimitHigh == True:
                        options = ["2차수급後상승","2차수급後하락",'저점유지']
                        minLimitHigh2 = st.segmented_control("갭상이CHECK", options, selection_mode="multi")

                if minmove == '장중하락':
                    options = ["1차수급","2차수급"]
                    minmove2 = st.segmented_control("차트 변화", options, selection_mode="single")
                if minmove2 == '1차수급':
                    options = ["後상승","後보합",'後하락']
                    minmove3_1 = st.segmented_control("KEY-POINT", options, selection_mode="single")

                elif minmove2 == '2차수급':
                    options = ["많다","적다"]
                    minmoveA = st.segmented_control("1차 대비 수급량", options, selection_mode="single")
                    if minmoveA == "적다":
                        options = ["1차上돌파","後상승","後하락"]
                        minmove3 = st.segmented_control("KEY-POINT", options, selection_mode="multi")
                        if "後하락" in minmove3:
                            options = ["後재상승","저점이탈","저점유지"]
                            minmove3A = st.segmented_control("저점기준", options, selection_mode="single")



                # options = ["시외","대체"]
                # minResult = st.segmented_control("거래소", options, selection_mode="single")

            TotalScore,TotaltechName = technical(king,selection,tenDateLine,LowSelection,beforeHigher,beforeHigherCheck,reverseLine,jumpuLine,hightime,minmove3,LowAgree,
                                            minLimitHigh2,minmove3_1,reverseLine2,minmove3A)

        if st.button("✅ 확인"):
            try:
                st.session_state.score = TotalScore
                st.session_state.tech = TotaltechName
                if st.session_state.score >= 90: #90점이상
                    st.session_state.text = "님아 안사고 뭐해?침팬치 매매 가즈아!!" 
                    st.session_state.color = '#ff0000'
                    st.session_state.imoji = "🙊"

                elif st.session_state.score < 90 and st.session_state.score >=80: #80점이상
                    st.session_state.text = "이 종목은 살만 할지도...?" 
                    st.session_state.color = '#ff0000'
                    st.session_state.imoji = "💸"

                elif st.session_state.score < 80 and st.session_state.score >=70: #90점이상
                    st.session_state.text = "신중히 고민해보자"
                    st.session_state.color = '#b04157'
                    st.session_state.imoji = "🧐"

                elif st.session_state.score < 70 and st.session_state.score >=50: #50~70점이상
                    st.session_state.text = "이거사면 물리는거야"
                    st.session_state.color = 'blue'
                    st.session_state.imoji = "🤪"

                elif st.session_state.score < 50 and st.session_state.score >=10: #0~50점이상
                    st.session_state.text = "이 종목을 본다고?? 실화임? "
                    st.session_state.color = 'blue'
                    st.session_state.imoji = "💩"

                elif st.session_state.score == 0: #0~50점이상
                    st.session_state.text = "화성갈끄니까!"
                    st.session_state.color = 'black'
                    st.session_state.imoji = "😴"
            except NameError as e:
                print(e)
                pass
            st.rerun()

    # if st.button("🔄 초기화"):
    #     st.session_state.clear()
    #     st.rerun()