from django.core.management.base import BaseCommand
from characterforge.models import APIProficiency
from characterforge.api_service import get_proficiencies

class Command(BaseCommand):
    help = "Populate the database with proficiencies from the D&D API"

    def handle(self, *args, **kwargs):
        proficiencies = get_proficiencies()
        for proficiency_index, proficiency_name in proficiencies:
            APIProficiency.objects.get_or_create(
                index = proficiency_index,
                defaults={'name': proficiency_name}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated proficiencies.'))