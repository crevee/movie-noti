import requests
import telegram
from bs4 import BeautifulSoup

from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = ' ')

url = 'http://www.cgv.co.kr/theaters/?areacode=03%2C205&theaterCode=0007&date=20221116'

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    imax = soup.select_one('span.imax')

    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id = 312421412, text= title + 'IMAX 예매가 열렸습니다.' )
        sched.pause()

    
sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds = 30)
sched.start