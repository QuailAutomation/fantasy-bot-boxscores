from datetime import datetime, date
import json
import time

import pandas as pd
from nhl_scraper.nhl import Scraper

from boxscores.celery import Celery

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# season_opening_date = date(2022,10, 7)
# season_end_date = date(2022,10,8)

nhl_scraper = Scraper()

def scrape_boxscores(startdate, enddate, output_dir='/boxscores', sleep_timout=1):
    print(f'start: {startdate}, end: {enddate}')
    game_date_range = pd.date_range(startdate, enddate)
    for game_date in game_date_range:
        nhl_game_date = game_date.to_pydatetime().replace(microsecond=0)
        games = nhl_scraper.games(nhl_game_date.date(), nhl_game_date.date())

        for game in games:
            print('downloading boxscore, id={}'.format(game))
            box_score = nhl_scraper.box_scores(game,format='json')
            box_score['game_date'] = datetime.strftime(nhl_game_date, DATETIME_FORMAT)
            box_score['timestamp'] = game_date.timestamp()
            with open(f'{output_dir}/{game}.json', 'w') as outfile:
                json.dump(box_score, outfile)
            time.sleep(sleep_timout)
