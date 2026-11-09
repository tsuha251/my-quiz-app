import math
import streamlit as st

# クイズ問題を定義
QUIZ = [
    {"問題": "固定資産を贈与により無償で取得した場合には、公正な評価額（時価）をもって取得原価とする", "答え": "Yes"},
    {"問題": "固定資産を無償で取得した場合、公正な評価額（時価）をもって取得原価とするが、これは、当該固定資産に将来の収益を獲得する能力（経済的便益）が認められるからである。", "答え": "Yes"},
    {"問題": "固定資産を交換する場合、取得資産の取得原価は投資が継続してるか清算されているかによって異なる。", "答え": "Yes"},
    {"問題": "中古車の下取り買替えにおいて、中古車の下取り価額がその時価よりも高く設定されている場合、下取価格が時価を超える部分については、通常、中古車に係る売却益と考えられる。", "答え": "No"},
    {"問題": "圧縮記帳の目的は補助金の受け入れが収益計上されることにより、受け入れた期に一括課税されるのを防止することである。", "答え": "Yes"},
    {"問題": "固定資産を購入により取得した場合、固定資産の稼働後の保険料は取得原価に算入せず、期間費用として処理する。", "答え": "Yes"},
    {"問題": "固定資産を自家建設した場合、建設に要する借入資本の利子で稼働後の期間に属するものは、これを取得原価に算入することができる。", "答え": "No"},
    {"問題": "資本的支出とは、固定資産の価値を高め、その原価を構成する支出をいう。また、収益的支出とは、原価に算入されず、当該期間の費用（修繕費）として処理される支出をいう。", "答え": "Yes"},
    {"問題": "ここの鳥皮ってカリカリしてます？", "答え": "No"},
    {"問題": "アルフォートは水色より青の方がおいしい？", "答え": "Yes"},
]

# ゲームの初期設定
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.ok = 0
    st.session_state.answered = False
    st.session_state.selected = None

# タイトル
st.title("クイズアプリ")

# 問題を出題
if st.session_state.index < len(QUIZ):

    i = st.session_state.index
    qdata = QUIZ[i]

    st.subheader(f"クイズ 第{i+1}問目")
    st.progress((i + 1) / len(QUIZ))

    st.write(qdata["問題"])

    # 回答前
    if not st.session_state.answered:

        with st.form("quiz_form"):
            user = st.radio(
                "答えを選んでください",
                ["Yes", "No"]
            )

            submitted = st.form_submit_button("回答する")

        if submitted:
            st.session_state.selected = user
            st.session_state.answered = True

            if user == qdata["答え"]:
                st.session_state.ok += 1

            st.rerun()

    # 回答後
    else:

        if st.session_state.selected == qdata["答え"]:
            st.success("正解！エリートか？！")
        else:
            st.error("不正解！なにやってるんですか！")

        if st.button("次の問題へ"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.session_state.selected = None
            st.rerun()

# 全問終了
else:

    ok = st.session_state.ok
    rate = math.floor(ok / len(QUIZ) * 100)

    st.title("成績発表！")

    st.write(f"お疲れさまでした！")
    st.subheader(f"{ok}問正解！")
    st.subheader(f"正解率：{rate}%")

    if st.button("もう一度遊ぶ"):
        st.session_state.index = 0
        st.session_state.ok = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.rerun()
