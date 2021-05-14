from plyer import notification
import schedule
import time
import urllib3
from bs4 import BeautifulSoup

url = 'https://weather.yahoo.co.jp/weather/jp/13/4410.html'

#URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
http = urllib3.PoolManager()
instance = http.request('GET', url)
#instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(instance.data, 'html.parser')
tenki_today = soup.select_one('#main > div.forecastCity > table > tr > td > div > p.pict')

def work():
    notification.notify(
    title="いるか",
    message= "今日の天気は"+tenki_today.text,
    app_name="アプリの名前",
    app_icon='icon/iru.ico',
    timeout=3
)
#一分経過毎に関数workが実行される
schedule.every(0.5).minutes.do(work)

while True:
   schedule.run_pending()
   time.sleep(1)

