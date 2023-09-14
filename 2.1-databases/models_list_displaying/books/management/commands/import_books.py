import json
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('fixtures/books.json', encoding='utf8') as file:
            data = json.load(file)
        for row in data:
            Book.objects.create(id=row['pk'], name=row['fields']['name'], author=row['fields']['author'], pub_date=row['fields']['pub_date'])


