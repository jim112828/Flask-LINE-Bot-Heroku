from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from datetime import datetime

sched = BlockingScheduler()

token = 'knnjvKtQP3ZTScEdCYtFGTNKDuliEiaeiDw7vbriSjE'
curTime = getCurrentTime()
sendText = "beautiful Sarah, please eat pills!!"
message = f'Current time is :{curTime} and {sendText}'

def getCurrentTime():
    x = datetime.now()

    return x.strftime('%H:%M:%S')

@sched.scheduled_job('cron', day='1-31', hour='9')
def scheduled_job_nine():
    lineNotifyMessage(token,message)
    
@sched.scheduled_job('cron', day='1-31', hour='7')
def scheduled_job_six():
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