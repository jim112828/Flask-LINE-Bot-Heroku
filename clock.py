from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from datetime import datetime

def getCurrentTime():
    now = datetime.now()
    ThaiTime = now - datetime.timedelta(hours = 1)
    return ThaiTime.strftime('%H:%M:%S')

sched = BlockingScheduler()
token = 'knnjvKtQP3ZTScEdCYtFGTNKDuliEiaeiDw7vbriSjE'




@sched.scheduled_job('cron', day='1-31', hour='9')
def scheduled_job_nine():
    ThaiNow = getCurrentTime()
    sendText = "beautiful Sarah, please eat pills!!"
    message = f'Current time is :{ThaiNow} and {sendText}'
    lineNotifyMessage(token,message)
    
@sched.scheduled_job('cron', day='1-31', hour='19')
def scheduled_job_six():
    ThaiNow = getCurrentTime()
    sendText = "beautiful Sarah, please eat pills!!"
    message = f'Current time is :{ThaiNow} and {sendText}'
    lineNotifyMessage(token,message)

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

sched.start()