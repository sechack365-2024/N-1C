# チャットに投稿した⽂字にキャラ付けされるチャットシステム
## 製作要件
- 完全独⾃システムでも既存チャットの拡張機能でも可
- 投稿者が⾃分のペルソナを設定・または選択出来ること
- 普通の⽂章を⼊⼒すると⾃動でキャラ付けされた⽂章で投稿されること

## ライブラリ
- `pip3 install streamlit streamlit-chat`

## 実行方法
- `export GROQ_API_KEY="your-api-key-here"`
- `python3 -m streamlit run chat.py`
