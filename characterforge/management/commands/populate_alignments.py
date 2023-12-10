from django.core.management.base import BaseCommand
from characterforge.models import APIAlignment
from characterforge.api_service import get_alignments

class Command(BaseCommand):
    help = "Populate the database with alignments from the D&D API"

    def handle(self, *args, **kwargs):
        alignments = get_alignments()
        for alignment_index, alignment_name in alignments:
            APIAlignment.objects.get_or_create(
                index = alignment_index,
                defaults={'name': alignment_name}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated alignments.'))