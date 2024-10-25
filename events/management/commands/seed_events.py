from django.core.management.base import BaseCommand
from events.models import Event, Appointment
from faker import Faker
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populates the database with event data'

    def handle(self, *args, **kwargs):
        faker = Faker()

        Event.objects.all().delete()
        Appointment.objects.all().delete()

        for _ in range(10):
            Event.objects.create(
                name=faker.word(),
                description=faker.text(),
                price=100.00,
                duration=timedelta(hours=2)
            )

        for _ in range(10):
            event = Event.objects.order_by('?').first()
            Appointment.objects.create(
                event=event,
                date_time=faker.date_time_between(start_date=date.today(), end_date=date.today() + timedelta(days=1)),
                user_name=faker.name(),
                user_email=faker.email(),
                user_phone="(11) 1234-5678",
                notes=faker.text(),
            )

        self.stdout.write(self.style.SUCCESS('Event seeding completed!'))

