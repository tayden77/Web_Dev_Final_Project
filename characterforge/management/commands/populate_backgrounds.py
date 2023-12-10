from django.core.management.base import BaseCommand
from characterforge.models import APIBackground
from characterforge.api_service import get_backgrounds

class Command(BaseCommand):
    help = "Populate the database with backgrounds from the D&D API"

    def handle(self, *args, **kwargs):
        backgrounds = get_backgrounds()
        print(backgrounds)
        for background_index, background_name in backgrounds:
            APIBackground.objects.get_or_create(
                index = background_index,
                defaults={'name': background_name}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated backgrounds.'))