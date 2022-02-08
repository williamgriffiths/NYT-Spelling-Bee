import datetime
import requests
from bs4 import BeautifulSoup

def write(date):

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    url = 'https://nytbee.com/Bee_{}.html'.format(date)
    print(url)
    web = requests.get(url, headers=headers)

    data = web.content
    soup = BeautifulSoup(data, features="html.parser")

    f = open('dictionary6.txt','a')

    missing_dates = ["20181223","20181117","20181103","20180912","20180730"]

    if date in missing_dates:
        pass

    elif int(date) >= 20190817:
        for item in soup.findAll('div',{"class":"answer-list","id":"main-answer-list"}):
            answer_list = item.findAll('li')
            for word in answer_list:
                f.write(word.text.strip()+"\n")

    else:
        answer_list = soup.find('div',class_='answer-list').find('ul')
        for word in answer_list:
            f.write(word.text.strip()+"\n")
        f.close()

    with open('output.txt','r') as f:
        with open('allwords.txt','w') as file:
            for line in f:
                if not line.isspace():
                    file.write(line)
            


today = datetime.date.today()
# today = datetime.date(2018,7,30)
start_date = datetime.date(2018,7,29)
delta = (today - start_date).days

for i in range(delta+1):
    j = datetime.timedelta(days=i)
    date = (today - j).strftime('%Y%m%d')
    print(date)
    write(date)
    print("Written {}".format(date))