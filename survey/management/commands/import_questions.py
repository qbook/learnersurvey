# This code is a commandline to import survey questions.
# Usage: python manage.py import_questions path/to/yourfile.csv
# This uses a tap delimiter 
# Format CVS columns as: code	code_order	question_en	question_zh	section_name_en	section_name_zh	question_number

import csv
from django.core.management.base import BaseCommand
from survey.models import SurveySection, SurveyQuestion

class Command(BaseCommand):
    help = 'Imports questions from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **options):
        with open(options['csv_file'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t')  # Specify the delimiter here
            for row in reader:
                section, _ = SurveySection.objects.get_or_create(
                    name_en=row['section_name_en'],
                    name_zh=row['section_name_zh'],
                    code=row['code'],
                    code_order=int(row['code_order'])
                )
                SurveyQuestion.objects.create(
                    section_code=row['code'],
                    section=section,
                    text_en=row['question_en'],
                    text_zh=row['question_zh'],
                    question_number=int(row['question_number'])
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported questions'))

