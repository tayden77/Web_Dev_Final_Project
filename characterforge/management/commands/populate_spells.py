from django.core.management.base import BaseCommand
from characterforge.models import APISpell
from characterforge.api_service import get_spells

class Command(BaseCommand):
    help = "Populate the database with spells from the D&D API"

    def handle(self, *args, **kwargs):
        spells = get_spells()
        print(spells)
        for spell_index, spell_name in spells:
            APISpell.objects.get_or_create(
                index = spell_index,
                defaults={'name': spell_name}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated spells.'))