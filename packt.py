import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.packtpub.com/packt/offers/free-learning'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}
r=requests.get(url, headers=headers).text

soup = BeautifulSoup(r, "html.parser")
name = soup.find_all('h1')[0].text.strip()
print(name)
msg = 'Subject: {}\n{}\n{}'.format(name,name,url)

user_input = []
with open('app.config', 'r') as f:
    for line in f:
        user_input.append(line.strip())

user = user_input[0]
password = user_input[1]

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(user, password)
server.sendmail("from",
                "to@mail.com",
                msg)
server.quit()
