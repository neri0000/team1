from plyer import notification
import psycopg2
import schedule
import time

def job(cur):
    alert = ""

    cur.execute("select data from sample order by time desc limit 1;")
    rows = cur.fetchall()
    hoge = rows[0][0]

    if int(hoge) >= 98:
        alert += "hogeが100%に近付いています。"

    if alert != "":
        notification.notify(
            title = "警告",
            message = alert,
            app_name = "モニター監視"
        )


print("監視を開始します。\n基準値付近になるとデスクトップ通知を行います。")

# 接続情報作成
con = psycopg2.connect("host=xxx.xxx.xxx.xxx port=xxxx dbname=xxxx user=xxxx password=xxxx")
cur = con.cursor()

# 指定時間ごとにjobを実行（今回は10秒ごと）
schedule.every(10).seconds.do(job, cur)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        print("中断しました。")
        cur.close()
        con.close()
        break