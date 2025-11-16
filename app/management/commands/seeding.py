import csv
from django.core.management.base import BaseCommand
from app.models import Data

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('./data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Data.objects.create(city=row['city'], country=row['country'], long=row['lng'], lati=row['lat'])
                print(f"added {row['city']}, {row['country']}")