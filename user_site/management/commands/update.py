from django.core.management.base import BaseCommand
from user_site.models import Team
import datetime
import logging
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_teams = requests.get('https://api.opendota.com/api/teams', auth=('user', 'pass'))
        all_teams=all_teams.json()

        for item in all_teams:
            item['logo'] = item.pop('logo_url')



        for item in all_teams:

                timestamp = item['last_match_time']
                last_match_time = datetime.datetime.fromtimestamp(timestamp)

                if item['logo']==None:
                    item['logo']='http://127.0.0.1:8000/img/media/placeholder.png'


                Team.objects.update_or_create(pk=item['team_id'],
                                                  defaults={'name': item['name'], 'tag': item['tag'],
                                                            'rating': item['rating'], 'wins': item['wins'],
                                                            'losses': item['losses'],
                                                            'last_match_time': last_match_time.strftime('%Y-%m-%d'),
                                                            'logo': item['logo']})
                logging.info('Data add is successful!!!')




