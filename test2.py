from plyer import notification
import schedule
import time

def work():
    notification.notify(
    title="Pythonで通知",
    message= "そろそろ休憩しませんか？",
    app_name="アプリの名前",
    timeout=3
)
#一分経過毎に関数workが実行される
schedule.every(1).minutes.do(work)

while True:
   schedule.run_pending()
   time.sleep(1)

