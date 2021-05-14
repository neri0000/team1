from plyer import notification
import schedule
import time
import random

tolk_list = ["机の上掃除してる？","課題終わらせたかー？","ちゃんとキーボードも掃除してる？溝とか隙間にほこり溜まりやすいのよね",
"休憩しませんか？","休憩したい","ちょっと黙るわ","そろそろアレ買っといた方がいいんじゃない？","ちゃんとキーボードも掃除してる？溝とか隙間にほこり溜まりやすいのよね",
"休憩しませんか？"]


act = random.randint(0,len(tolk_list)-1)
def work():
    act = random.randint(0,len(tolk_list)-1)

    notification.notify(
    title="いるか",
    message= tolk_list[act],
    app_name="アプリの名前",
    app_icon='icon/iru.ico',
    timeout=5
)
#一分経過毎に関数workが実行される
schedule.every(10).seconds.do(work)
#schedule.every(1).minutes.do(work)
while True:
   schedule.run_pending()
   time.sleep(1)

