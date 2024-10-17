# populate_problems.py
from django.core.management.base import BaseCommand
from api.models import Problem
from api.scraper import return_data_dict
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the database with problems from the scraper'
    Problem.objects.all().delete()
    # Reset the auto-increment ID sequence
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='api_problem';")

    def handle(self, *args, **kwargs):
        data = return_data_dict()
        for item in data:
            Problem.objects.get_or_create(
                number=item['Number'],
                defaults={
                    'name': item['Name'],
                    'link': item['Link'],
                    'time_complexity': item['Time Complexity'],
                    'space_complexity': item['Space Complexity']
                }
            )
        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
