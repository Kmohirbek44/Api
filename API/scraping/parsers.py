

import requests
from  bs4 import BeautifulSoup as bs
from random import randint
__all__=['hh']
headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    ]

# url='https://tashkent.hh.uz/search/vacancy?clusters=true&area=2759&ored_clusters=true&order_by=publication_time&enable_snippets=true&salary=&st=searchVacancy&text=python'

host='https://tashkent.hh.uz'
def hh(url,city=None,language=None):

    jobs = []
    errors = []
    if url:
        r = requests.get(url, headers=headers[randint(0, 2)])
        if r.status_code==200:
            soup=bs(r.content,'html.parser')
            main_div=soup.find('div','sticky-container')
            if main_div:
                vacation_divs=main_div.find('div','bloko-gap')
                vacations=vacation_divs.find_all('div','vacancy-serp-item')
                for vacation in vacations:
                    title_and_format=vacation.find('a','bloko-link')
                    jobs.append({
                        'url':title_and_format.get('href'),
                        # 'price': vacation.find('span',attrs={'data-qa':'vacancy-serp__vacancy-compensation'}),
                        'title': title_and_format.get_text(),
                        'company':vacation.find('div','vacancy-serp-item__meta-info-company').a.get_text(),
                        # 'company_href':host+vacation.find('div','vacancy-serp-item__meta-info-company').a.get('href'),
                        'description':vacation.find('div','g-user-content').get_text(),
                        'city_id':city,
                        'language_id':language




                    })

            else:
                errors.append({'url':url,'title':'main_div not exicst'})

        else:
            errors.append({'url':url,'title':'Page do not response'})

    return jobs,errors