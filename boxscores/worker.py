from datetime import date, timedelta, datetime
from boxscores.celery import cel
from boxscores.download_boxscores import scrape_boxscores

@cel.task(name='hello_world', queue='boxscores')
def hello(name='world', name2='d'):
    return 'hello ' + name

@cel.task(name='download_boxscores', queue='boxscores')
def scrape_boxscores_task(last_day=None, ndays=1):
    if last_day is None:
        last_day = date.today()
    else:
        last_day = datetime.strptime(last_day, '%Y-%m-%d')
    
    scrape_boxscores(startdate = last_day - timedelta(days=ndays), enddate=last_day)

print("executed tasks.py")