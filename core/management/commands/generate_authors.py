from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from core.models import Author, User
import random


faker = Faker()


class Command(BaseCommand):
    help = "Generate fake Authors"

    def add_arguments(self, parser):
        parser.add_argument(
            "no",
            nargs="?",
            type=int,
            help="Number of authors  to generate.",
            default=1,
        )

    def handle(self, *args, **options):
        try:
            no = options["no"]


            for _ in range(no):
                authors = list(Author.objects.all())
                users = list(User.objects.all())
                
                author = Author.objects.create(
                    firstname=faker.first_name(),
                    lastname=faker.last_name(),
                    address=faker.address(),
                    zipcode=faker.zipcode(),
                    tel_no=faker.phone_number(),
                    join_date=faker.date_between(start_date="-5y", end_date="today"),
                    recommend_by=random.choice(authors) if authors else None,
                    popularity_score=random.randint(1, 100),
                )

                author.followers.set(
                    random.sample(users, random.randint(0, min(5, len(users))))
                )
                self.stdout.write(self.style.SUCCESS(f"Created Author: {author}"))
        except Exception as e:
            raise CommandError(e)
