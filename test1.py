from plyer import notification
import schedule
import time

def work():
    notification.notify(
    title="いるか",
    message= "そろそろ休憩しませんか？",
    app_name="アプリの名前",
    app_icon='icon/iru.ico',
    timeout=3
)
#一分経過毎に関数workが実行される
schedule.every(0.5).minutes.do(work)

while True:
   schedule.run_pending()
   time.sleep(1)