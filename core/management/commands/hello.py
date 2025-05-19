from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Greet the world.'

    def handle(self, *args, **options):
        print('Hello, World..!')