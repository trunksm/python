import requests
from bs4 import *

#mes = input("Enter your message: ")
def website():
	url = "https://www.salahtimes.com/india/kalyan"
	url_req = requests.get(url).text
	soup = BeautifulSoup(url_req, "html.parser")
	table = soup.find_all('table', {'class':'table table-responsive table-condensed table-prayertimes'})
	for i in table:
		h = i.find_all('tbody')
		for j in h:
			a = j.find_all('tr',{'class':'today'})
			for z in a:
				c = z.find_all('td')
				message = 'day-' +c[0].string+ ' Fajr-' +c[2].string+ ' Zohr-' +c[4].string+ ' Asr-' +c[5].string+ " Mgrib-" +c[6].string+ " Isha-" +c[7].string
				print(len(message))
				return message

run = website()
def sms(message):
    urlsms = 'http://site24.way2sms.com/Login1.action?username=7208376237&password=shoaibmu123456&Submit=Sign+in'
    varsreq = requests.Session()
    varsreq.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
    req = varsreq.post(urlsms)
    jession_id = varsreq.cookies.get_dict()['JSESSIONID'][4:]
    sendsms = 'http://site24.way2sms.com/smstoss.action'
    payload = {
        'ssaction':'ss',
        'Token':jession_id,
        'mobile':'8850395059',
        'message':message,
        'msgLen':'136'
    }
    q = varsreq.post(sendsms, data=payload)
    if q.status_code==200:
        print("successfull")
    else:
        print("unsuccessfull")

sms(run)
