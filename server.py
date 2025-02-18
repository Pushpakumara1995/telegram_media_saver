from flask import Flask, request
from telethon import TelegramClient
import asyncio

app = Flask(__name__)

# Replace with your actual Telegram API credentials and phone number
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
PHONE_NUMBER = "YOUR_PHONE_NUMBER"

# Replace with the chat (group/user) ID where messages should be sent
CHAT_ID = "GROUP_CHAT_ID"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
