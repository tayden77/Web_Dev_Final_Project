from django.core.management.base import BaseCommand
from characterforge.models import APIFeat
from characterforge.api_service import get_feats

class Command(BaseCommand):
    help = "Populate the database with feats from the D&D API"

    def handle(self, *args, **kwargs):
        feats = get_feats()
        for feat_index, feat_name in feats:
            APIFeat.objects.get_or_create(
                index = feat_index,
                defaults={'name': feat_name}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated feats.'))
