from django.core.management.base import BaseCommand, CommandError
from core.models import Publisher
from faker import Faker
import random

faker = Faker()


class Command(BaseCommand):
    help = "Generate fake Publishers."

    def add_arguments(self, parser):
        parser.add_argument(
            "no",
            nargs="?",
            type=int,
            default=1,
            help="Number of publisher to generate.",
        )

    def handle(self, *args, **options):
        try:

            for _ in range(options["no"]):
                publishers = list(Publisher.objects.all())
                
                publisher = Publisher.objects.create(
                    firstname=faker.first_name(),
                    lastname=faker.last_name(),
                    recommendedby=random.choice(publishers) if publishers else None,
                    joindate=faker.date_between("-5y", "today"),
                    popularity_score=random.randint(1, 100),
                )

                self.stdout.write(self.style.SUCCESS(f"Created Publisher: {publisher}"))
        except Exception as e:
            raise CommandError(e)
