from django.core.management.base import BaseCommand
from main.models import AccessKey

class Command(BaseCommand):
    help = 'Create a new access key'

    def add_arguments(self, parser):
        parser.add_argument('access_to', type=str)

    def handle(self, *args, **options):
        access_to = options['access_to']
        access_key = AccessKey(access_to=access_to)
        access_key.save()
        self.stdout.write(f'Access key created: {access_key.key}')
