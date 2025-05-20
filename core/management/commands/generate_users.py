from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from core.models import User


faker = Faker()


class Command(BaseCommand):
    help = "Generate fake Users."

    def add_arguments(self, parser):
        parser.add_argument(
            "no", nargs="?", type=int, help="Number of users to generate.", default=1
        )

    def handle(self, *args, **options):
        try:
            for _ in range(options["no"]):
                user = User.objects.create(
                    username=faker.user_name(), email=faker.email()
                )

                self.stdout.write(self.style.SUCCESS(f"Created User: {user}"))
        except Exception as e:
            raise CommandError(e)
