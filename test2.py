from plyer import notification
import schedule
import time
import random
import datetime

nia = time.time()

tolk_list = ["軽く机回りを掃除したらどうだ？効率が落ちるど","課題は終わっているか？早めにやっといた方が...終わってる？アッハイスミマセンでした",
"猫背になってないか？肘をのばして体を伸ばしてあげたらどうだ？","捗っているか？君は頑張り屋だからな、適度に休憩を挟めよ","そろそろ休憩したい。","もしかして煩いか？...ちょっと黙るわ",
"そろそろアレ買っといた方がいいんじゃない？","スマホ触ってないだろうな？メリハリ持てているか？","大好きだぜ～"]

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

