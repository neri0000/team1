from plyer import notification
import schedule
import time
import random
import datetime
import urllib3
from bs4 import BeautifulSoup

#天気情報の獲得
url = 'https://weather.yahoo.co.jp/weather/jp/13/4410.html'
http = urllib3.PoolManager()
instance = http.request('GET', url)
soup = BeautifulSoup(instance.data, 'html.parser')
tenki_today = soup.select_one('#main > div.forecastCity > table > tr > td > div > p.pict')


nia = time.time()

tolk_list = ["軽く机回りを掃除したらどうだ？作業スペースが狭いと効率が落ちるど","課題は終わっているか？早めにやっといた方が...え、終わってる？余計なお世話だったか",
"猫背になってないか？体を伸ばしてあげたらどうだ？","捗っているか？君は頑張り屋だからな、適度に休憩を挟めよ","そろそろ休憩したい。","もしかして煩いか？",
"そろそろアレ買っといた方がいいんじゃない？","スマホ触ってないだろうな？メリハリ持てているか？","お疲れ様！どう？ここらで一旦休憩と行きましょうよ",
"そんでもって今日の天気は"+str(tenki_today.text)+"窓の外見て確認してみてよ...どうだった？"]

act = random.randint(30,60)
count = 0
def work():
    #気まぐれ時間設定
    act = random.randint(30,60)
    global count
    if count >= len(tolk_list):
        random.shuffle(tolk_list)
        count = 0

    #act = random.randint(0,len(tolk_list)-1)

    m,s = minute(nia)

    notification.notify(
    title="いるか先輩",
    message= "私が起きてから約%s分が経過したぞ"%(m)+'\n'+ tolk_list[count],
    app_icon='icon/iru2.ico',
    timeout=5
    )
    count+=1

#経過時間を返す
def minute(num):
    now = time.time()
    t = now - num
    td = datetime.timedelta(seconds=t)
    return divmod(td.seconds, 60)

#10秒経過毎に関数workが実行される
#schedule.every(10).seconds.do(work)
#10分経過毎に関数workが実行される
schedule.every(10).minutes.do(work)
while True:
   schedule.run_pending()
   time.sleep(1)

