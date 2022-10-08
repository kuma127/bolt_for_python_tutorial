import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


# echoコマンドは受け取ったコマンドをそのまま返す
@app.command("/echo")
def repeat_text(ack, respond, command):
    # command リクエストを確認
    ack()
    respond(f"{command['text']}")


# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
