from django.core.management.base import BaseCommand
from users.models import User
import os


class Command(BaseCommand):

    help = "This command creates superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username=os.environ.get("ADMIN_NAME"))
        if not admin:
            User.objects.create_superuser(
                os.environ.get("ADMIN_NAME"),
                os.environ.get("ADMIN_EMAIL"),
                os.environ.get("ADMIN_PW"),
            )
            self.stdout.write(self.style.SUCCESS(f"Superuser Created"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser Exists"))
