from django.core.management.base import BaseCommand, CommandError
from shortener.models import fesURL

class Command(BaseCommand):
    help = 'Refreshes all fesURL shorcodes'

    def handle(self, *args, **options):
        return fesURL.objects.refresh_shortcodes(items=options['items'])
        
