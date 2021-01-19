from django.core.management.base import BaseCommand
from user_site.models import Team
import datetime
import logging
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_teams = requests.get("https://api.opendota.com/api/teams")
        all_teams = all_teams.json()
        create = 0
        update = 0
        for item in all_teams:

            timestamp = item["last_match_time"]
            last_match_time = datetime.datetime.fromtimestamp(timestamp)

            if item["logo_url"] == None:
                item[
                    "logo_url"
                ] = "http://127.0.0.1:8000/img/media/placeholder.png"

            _,created= Team.objects.update_or_create(
                opendota_team_id=item["team_id"],
                defaults={
                    "name": item["name"],
                    "tag": item["tag"],
                    "rating": item["rating"],
                    "wins": item["wins"],
                    "losses": item["losses"],
                    "last_match_time": last_match_time,
                    "logo": item["logo_url"],
                },
            )

            if created:
                create += 1
            else:
                update += 1
        logging.info(
                "{} Teams updated and {} created.".format(update,create)
            )
