import smtplib
import ssl
import requests
from bs4 import BeautifulSoup


#url of targeted Stock page from Yahoo Finance
url = 'https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch'

re = requests.get(url)

soup=BeautifulSoup(re.text, 'html.parser') #scrapping using BeautifulSoup.
print(soup.title.text)

price = float(soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text)
change = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text

if price <xyz: #replace 'xyz' with your target amount.
    mail="sender@xyz.com" #replace it with sender's email address.
    passw= "sender email password" #replace it with sender's email password.
    smt = smtplib.SMTP("smtp.gmail.com") #replace it with sender's email type for yahoomail: 'smtp.mail.yahoo.com'
    smt.starttls()
    smt.login(mail, passw)

#replace receiver's mail below:
    smt.sendmail("mail","receiver's mail",f"Subject: Stock Price Alert\n\n Hey,Current Price of your choosen stock is {price}.\n Buy now!!")
    smt.quit()
