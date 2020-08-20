from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates groups'

    def handle(self, *args, **options):

        print('Done')
