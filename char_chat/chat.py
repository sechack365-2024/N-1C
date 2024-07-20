import streamlit as st
from streamlit_chat import message
import os
from groq import Groq

# Groqクライアントの作成
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


# StreamlitのUIの作成
st.title("SecHack365")
st.caption("いやーなナイトセッション")

# セッション状態にチャット履歴が存在しない場合、初期化する
if 'history' not in st.session_state:
    st.session_state.history = []

# 入力フォームと送信ボタンの作成
text_input = st.text_input("Enter your message")

# プルダウンメニューの作成
options = ["かわいい", "かっこいい", "ふざけた", "元気な", "ネガティブな", "ハリウッドな"]
selected_option = st.selectbox("Choose an option", options)

# 送信ボタン
send_button = st.button("Send")

# ボタンが押された時の処理
if send_button and text_input:
    # システムプロンプトの設定
    system_prompt = {
        "role": "system",
        "content": f"あなたは便利なアシスタントです。私の言葉を繰り返した後に，{selected_option}決め台詞を追加してください．ただし出力はに鉤括弧は含めないでください．"
    }

    st.session_state.history.append(('user', text_input))
    
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
    st.session_state.history.append(('ai', response.choices[0].message.content))

# チャット履歴の表示
for index, chat_message in enumerate(reversed(st.session_state.history)):
    if chat_message[0] == 'user':
        message(chat_message[1], is_user=True, key=2 * index)
    elif chat_message[0] == 'ai':
        message(chat_message[1], is_user=False, key=2 * index + 1)
