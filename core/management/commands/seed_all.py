from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Executes the seeds for all apps'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Starting seed for all apps...'))

        call_command('seed_events') 
        call_command('seed_products')

        self.stdout.write(self.style.SUCCESS('Seed for all apps completed!'))
