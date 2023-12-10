from django.core.management.base import BaseCommand
from characterforge.models import APIClass
from characterforge.api_service import get_classes

class Command(BaseCommand):
    help = "Populate the database with classes from the D&D API"

    def handle(self, *args, **kwargs):
        classes = get_classes()
        for class_index, class_name in classes:
            APIClass.objects.get_or_create(
                index = class_index,
                defaults={'name': class_name}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated classes.'))