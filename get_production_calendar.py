import json, requests, re, calendar, datetime
from bs4 import BeautifulSoup

def get_production_calendar(start_year, end_year=False):
    end_year = start_year if end_year is False else end_year
    production_calendar = {}
    
    def get_month_number(month_name, locale):
        with calendar.different_locale(locale):
            month_names = [x.lower() for x in calendar.month_abbr]
            return month_names.index(month_name.lower()[:3])
    
    for year in range(start_year, end_year+1):
        try:
            response = requests.get(f'http://www.consultant.ru/law/ref/calendar/proizvodstvennye/{year}')
            soup = BeautifulSoup(response.text, 'lxml')
            months_tables = soup.find_all('table', class_='cal')

            for month_table in months_tables:
                month_name = month_table.find('th', class_='month').text.lower()
                month = get_month_number(month_name, 'ru_RU')

                for weekend in month_table.find_all('td', class_='weekend'):
                    day = int(re.sub(r'\D', '', weekend.text))
                    production_calendar[str(datetime.date(year, month, day))] = 'weekend'

                for nowork in month_table.find_all('td', class_='nowork'):
                    day = int(re.sub(r'\D', '', nowork.text))
                    production_calendar[str(datetime.date(year, month, day))] = 'nowork'

                for preholiday in month_table.find_all('td', class_='preholiday'):
                    day = int(re.sub(r'\D', '', preholiday.text))
                    production_calendar[str(datetime.date(year, month, day))] = 'preholiday'

                for workday in month_table.find_all('td', class_=''):
                    day = int(re.sub(r'\D', '', workday.text))
                    production_calendar[str(datetime.date(year, month, day))] = 'workday'
        except:
            continue
    
    with open('production_calendar.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(production_calendar, ensure_ascii=False))