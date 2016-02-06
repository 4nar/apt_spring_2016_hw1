from bottle import route, run, template
import requests
from bs4 import BeautifulSoup
import os 

url = "http://public.mig.kz/"
@route('/')
def index():
    # return {"usd": 378, "eur": 415, "rub": 4.82}
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")


    l1 = []
    l2 = []
    for tag in soup.find_all('ul'):
        if tag.has_attr('class') and 'clearfix' in tag.attrs['class'] and len(tag.attrs['class'])==1:

        	l1 = tag.find_all('h4')
        	l2 = tag.find_all('p')
        	for i in range(0,len(l1)):
        		l1[i]=l1[i].text
        		l2[i]=float(l2[i].text.split()[0])

    dic = dict(zip(l1,l2))
    return dic     	

 
    	


URL = "https://github.com/giAtSDU/apt_spring_2016_hw1"

@route('/forks')
def forks():
    resp = requests.get(URL)
    bs4 = BeautifulSoup(resp.content, "html.parser")
    res = None
    for tag in bs4.find_all('a'):
        if tag.has_attr('class') and 'social-count' in tag.attrs['class']:
            res = int(tag.string)
    return {"forks": res}

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
