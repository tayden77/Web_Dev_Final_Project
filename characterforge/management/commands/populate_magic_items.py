from django.core.management.base import BaseCommand
from characterforge.models import Equipment
from characterforge.api_service import get_magic_items

class Command(BaseCommand):
    help = "Populate the database with magic items from the D&D API"

    def handle(self, *args, **kwargs):
        magic_items = get_magic_items()
        for item in magic_items:
            Equipment.objects.get_or_create(
                name=item[1],
                defaults={'equipment_type': 'MAGIC'}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated magic items'))