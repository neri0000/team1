from plyer import notification
import schedule
import time
import random
import datetime
import urllib3
from bs4 import BeautifulSoup

url = 'https://weather.yahoo.co.jp/weather/jp/13/4410.html'

#URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
http = urllib3.PoolManager()
instance = http.request('GET', url)
#instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(instance.data, 'html.parser')
tenki_today = soup.select_one('#main > div.forecastCity > table > tr > td > div > p.pict')


nia = time.time()

tolk_list = ["軽く机回りを掃除したらどうだ？作業スペースが狭いと効率が落ちるど","課題は終わっているか？早めにやっといた方が...え、終わってる？余計なお世話だったか",
"猫背になってないか？体を伸ばしてあげたらどうだ？","捗っているか？君は頑張り屋だからな、適度に休憩を挟めよ","そろそろ休憩したい。","もしかして煩いか？",
"そろそろアレ買っといた方がいいんじゃない？","スマホ触ってないだろうな？メリハリ持てているか？","お疲れ様！どう？ここらで一旦休憩と行きましょうよ...あっ保存忘れずにね",
"そんでもって今日の天気は"+tenki_today.text+"らしいぞ！窓の外見て確認してみてよ...どうだった？"]

act = random.randint(0,len(tolk_list)-1)

def work():
    act = random.randint(0,len(tolk_list)-1)

    now = time.time()
    t = now - nia
    td = datetime.timedelta(seconds=t)

    m,s  = divmod(td.seconds, 60)

    notification.notify(
    title="カイル先輩",
    message= "私が起きてから約%s分が経過したぞ"%(m)+'\n'+ tolk_list[act],
    app_icon='icon/iru.ico',
    timeout=5
)
#一分経過毎に関数workが実行される
schedule.every(10).seconds.do(work)
#schedule.every(1).minutes.do(work)
while True:
   schedule.run_pending()
   time.sleep(1)

