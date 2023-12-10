from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Skill, Feat, Proficiency, SchoolOfMagic, Equipment, Character, CharacterClass, CharacterSpell, APIRace, APIClass, APIFeat, APIProficiency, APISkill, APISpell, APIBackground

admin.site.register(User, UserAdmin)
admin.site.register(Skill)
admin.site.register(Feat)
admin.site.register(Proficiency)
admin.site.register(SchoolOfMagic)
admin.site.register(Equipment)
admin.site.register(Character)
admin.site.register(CharacterSpell)
admin.site.register(CharacterClass)
admin.site.register(APIRace)
admin.site.register(APIClass)
admin.site.register(APIFeat)
admin.site.register(APIProficiency)
admin.site.register(APISkill)
admin.site.register(APISpell)
admin.site.register(APIBackground)