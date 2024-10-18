from django.core.management.base import BaseCommand
from events.models import Event
from faker import Faker
from datetime import date, time

class Command(BaseCommand):
    help = 'Populates the database with event data'

    def handle(self, *args, **kwargs):
        faker = Faker()

        Event.objects.all().delete()

        for _ in range(10):
            Event.objects.create(
                name=faker.word(),
                description=faker.text(),
                date=date.today(),
                time=time(12, 0)
            )

        self.stdout.write(self.style.SUCCESS('Event seeding completed!'))

