from django.core.management.base import BaseCommand
from characterforge.models import APIRace
from characterforge.api_service import get_races

class Command(BaseCommand):
    help = "Populate the database with races from the D&D API"

    def handle(self, *args, **kwargs):
        races = get_races()
        print(races)
        for race_index, race_name in races:
            APIRace.objects.get_or_create(
                index = race_index,
                defaults={'name': race_name}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated races.'))