from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from .models import Cryptocurrency


@shared_task
def crawl_currency():
    print('Crawling data and creating objects in database ..')
    req = Request('https://coinranking.com', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    # Find first 5 table rows
    rows = bs.find('tbody', class_="table__body").find_all('tr', class_="table__row")[0:5]
    for row in rows:
        cryptocurrency = row.find('span', class_="profile__name").get_text().strip().replace('\n', '')
        values = row.find_all('div', class_="valuta")
        price = values[0].get_text().strip().replace('\n', '')
        market_cap = values[1].get_text().strip().replace('\n', '')
        change = row.find('div', class_="change").find('span').get_text().strip().replace('\n', '')
        print({'cryptocurrency': cryptocurrency, 'price':price, 'market_cap':market_cap, 'change':change}) 
        # Create object in database from crawled data 
        Cryptocurrency.objects.create(
            cryptocurrency = cryptocurrency,
            price = price,
            market_cap = market_cap,
            change = change
        )
        # Sleep 3 seconds to avoid any errors
        sleep(3)
@shared_task
def update_currency():
    print('Updating data ..')
    req = Request('https://coinranking.com', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    
    rows = bs.find('tbody', class_="table__body").find_all('tr', class_="table__row")[0:5]
    for row in rows:
        cryptocurrency = row.find('span', class_="profile__name").get_text().strip().replace('\n', '')
        values = row.find_all('div', class_="valuta")
        price = values[0].get_text().strip().replace('\n', '')
        market_cap = values[1].get_text().strip().replace('\n', '')
        change = row.find('div', class_="change").find('span').get_text().strip().replace('\n', '')
        print({'cryptocurrency': cryptocurrency, 'price':price, 'market_cap':market_cap, 'change':change})
        data = {'cryptocurrency': cryptocurrency, 'price':price, 'market_cap':market_cap, 'change':change}
        Cryptocurrency.objects.filter(cryptocurrency=cryptocurrency).update(**data)
        
        sleep(3)   

if not Cryptocurrency.objects:      
    crawl_currency()

while True:
    sleep(15)
    update_currency()