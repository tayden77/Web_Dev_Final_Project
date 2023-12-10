from django.core.management.base import BaseCommand
from characterforge.models import Equipment
from characterforge.api_service import get_equipment

class Command(BaseCommand):
    help = "Populate the database with equipment items that aren't magic from the D&D API"

    def handle(self, *args, **kwargs):
        other_items = get_equipment()
        for item in other_items:
            Equipment.objects.get_or_create(
                name=item[1],
                defaults={'equipment_type': 'OTHER'}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated non-magic items'))