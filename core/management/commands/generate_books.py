from django.core.management.base import BaseCommand, CommandError
from core.models import Publisher, Author, Books
from faker import Faker
import random


faker = Faker()


class Command(BaseCommand):
    help = "Generate fake Books."

    def add_arguments(self, parser):
        parser.add_argument(
            "no",
            nargs="?",
            type=int,
            default=1,
            help="Number of books to generate.",
        )

    def handle(self, *args, **options):
        try:
            authors = list(Author.objects.all())
            publishers = list(Publisher.objects.all())

            if not authors or not publishers:
                self.stdout.write(
                    self.style.ERROR(
                        "You must have Authors and Publishers in the database first."
                    )
                )
                return

            for _ in range(options["no"]):
                authors = list(Author.objects.all())
                publishers = list(Publisher.objects.all())

                book = Books.objects.create(
                    title=faker.sentence(nb_words=5),
                    genre=faker.word(),
                    price=random.randint(100, 1000),
                    published_date=faker.date_between(
                        start_date="-10y", end_date="today"
                    ),
                    author=random.choice(authors),
                    publisher=random.choice(publishers),
                )
                self.stdout.write(self.style.SUCCESS(f"Created Book: {book}"))
        except Exception as e:
            raise CommandError(e)
