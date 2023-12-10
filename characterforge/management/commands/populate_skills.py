from django.core.management.base import BaseCommand
from characterforge.models import APISkill
from characterforge.api_service import get_skills

class Command(BaseCommand):
    help = "Populate the database with skills from the D&D API"

    def handle(self, *args, **kwargs):
        skills = get_skills()
        for skill_index, skill_name in skills:
            APISkill.objects.get_or_create(
                index = skill_index,
                defaults={'name': skill_name}
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated skills.'))