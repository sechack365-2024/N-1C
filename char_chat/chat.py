import streamlit as st
from streamlit_chat import message
import os
from groq import Groq
import json

# Groqクライアントの作成
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# StreamlitのUIの作成
st.title("SecHack365")
st.caption("とても辛いナイトセッション")

# セッション状態にチャット履歴が存在しない場合、初期化する
if 'history' not in st.session_state:
    st.session_state.history = []

# ユーザー名の入力
user_name = st.text_input("名前を入力してください")

# 入力フォームと送信ボタンの作成
text_input = st.text_input("メッセージを入力してください")

# プルダウンメニューの作成
options = ["かわいい", "かっこいい", "ふざけた", "元気な", "ネガティブな", "ハリウッドな"]
selected_option = st.text_input("キャラ設定を入力してください(例: ネガティブな)")#st.selectbox("キャラを選択してください", options)

# 送信ボタン
send_button = st.button("Send")

# ボタンが押された時の処理
if send_button and text_input and user_name:
    # システムプロンプトの設定
    system_prompt = {
        "role": "system",
        "content": f"あなたは便利なアシスタントです。私の言葉を繰り返した後に，{selected_option}決め台詞を追加してください．ただし出力には鉤括弧は含めないでください．"
    }

    # ユーザープロンプトの作成
    user_prompt = {"role": "user", "content": text_input}
    chat_history = [system_prompt, user_prompt]

    # Groq APIによる応答生成
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=100,
        temperature=1.2
    )

    # AIの応答をチャット履歴に追加
    st.session_state.history.append(
        {
            'user_type': 'user', 
            'message':response.choices[0].message.content, 
            'user_name': user_name
        }
    )

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(st.session_state.history, json_file, ensure_ascii=False, indent=4)

with open('data.json', 'r', encoding='utf-8') as json_file:
    st.session_state.history = json.load(json_file)

# チャット履歴の表示
for index, chat_message in enumerate(reversed(st.session_state.history)):
    if chat_message['user_type'] == 'user':
        message(f"{chat_message['user_name']}: {chat_message['message']}", is_user=True, key=2 * index)
