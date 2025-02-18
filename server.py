from flask import Flask, request, jsonify
from telethon import TelegramClient
import asyncio
import os

# API_ID = os.environ.get("API_ID")
# API_HASH = os.environ.get("API_HASH")
# PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
# CHAT_ID = os.environ.get("CHAT_ID")


app = Flask(__name__)

async def send_message(media_link):
    client = TelegramClient("session_name", API_ID, API_HASH)
    await client.start(PHONE_NUMBER)
    await client.send_message(CHAT_ID, media_link)
    await client.disconnect()

@app.route('/send_telegram', methods=['GET'])
def send_telegram():
    media_link = request.args.get("link", "")
    if not media_link:
        return {"status": "error", "message": "No media link provided"}, 400

    asyncio.run(send_message(media_link))
    return {"status": "success", "message": "Message sent to Telegram"}

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))

