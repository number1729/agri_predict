from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# LINE Messaging APIからのメッセージを受け付けるエンドポイント
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    events = data["events"]

    for event in events:
        if event["type"] == "message":
            user_id = event["source"]["userId"]
            text = event["message"]["text"]

            # ユーザーからのメッセージに対する処理
            response_text = "Received: " + text

            # 応答メッセージを送信
            send_message(user_id, response_text)

    return "OK"

# メッセージを送信する関数
def send_message(user_id, message_text):
    print("")
    # LINE Messaging APIを使用してメッセージを送信するコードをここに追加

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
