import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


# 'approve_button' という action_id のブロックエレメントがトリガーされるたびに、このリスナーが呼び出させれる
@app.action("approve_button")
def update_message(ack, body, client):
    ack()
    client.reactions_add(
        name="white_check_mark",
        channel=body["channel"]["id"],
        timestamp=body["container"]["message_ts"],
    )


# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
