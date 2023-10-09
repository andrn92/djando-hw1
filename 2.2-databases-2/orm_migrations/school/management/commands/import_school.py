import json

from django.core.management.base import BaseCommand
from school.models import Teacher, Student
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('school.json', 'r', encoding='utf8') as file:
            rows = json.load(file)

        # for row in rows:
        #     if row['model'] == 'school.teacher':
        #         Teacher.objects.create(id=row['pk'], name=row['fields']['name'], subject=row['fields']['subject'])
        # for row in rows:
        #     if row['model'] == 'school.student':
        #         Student.objects.create(id=row['pk'], name=row['fields']['name'], teacher=row['fields']['teacher'], group=row['fields']['group'])