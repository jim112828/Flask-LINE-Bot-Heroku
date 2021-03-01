import os
from datetime import datetime
import json
from flask import Flask, abort, request
import time
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)
myUserId = "U3add647c81d6ea92dbe149e34a729409"
sarahID = "Uba7298f7cf1920e013ce662cf96d9040"
line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text
    #room_id = event.source.room_id
    user_id = event.source.user_id

    

    sendText = "beautiful Sarah, please eat pills!!"
    # Send To Line
    #aOfEvent = dir(event)
    #reply = TextSendMessage(text=f'{user_id},{sendText}')
    #line_bot_api.reply_message(event.reply_token, reply)
    
    
    curTime = getCurrentTime()
    try: 
            
        if datetime.now().hour == '9' or datetime.now().hour == '19':

            line_bot_api.multicast([sarahID,myUserId], TextSendMessage(text=f'Current time is :{curTime} and {sendText}'))
        
    except LineBotApiError as e:
            pass
        

def getCurrentTime():
    x = datetime.now()

    return x.strftime('%H:%M:%S')
        
        


    
        


