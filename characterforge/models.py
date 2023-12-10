from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class APIRace(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class APIClass(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class APIFeat(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class APIAlignment(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class APIProficiency(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class APISkill(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class APISpell(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class APIBackground(models.Model):
    index = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Feat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Proficiency(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class SchoolOfMagic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Equipment(models.Model):
    EQUIPMENT_TYPES = [
        ('MAGIC', 'Magic Item'),
        ('OTHER', 'Other')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    equipment_type = models.CharField(max_length=6, choices=EQUIPMENT_TYPES)
    applicable_classes = models.ManyToManyField(APIClass, blank=True, related_name="class_equipment")

    def __str__(self):
        return self.name
    

class Sex(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(APIRace, on_delete=models.SET_NULL, null=True, blank=True)
    classes = models.ManyToManyField(APIClass, through='CharacterClass')
    feats = models.ManyToManyField(APIFeat)
    proficiencies = models.ManyToManyField(APIProficiency)
    spells = models.ManyToManyField(APISpell, through='CharacterSpell')
    equipment = models.ManyToManyField(Equipment)
    skills = models.ManyToManyField(APISkill)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    alignment = models.ForeignKey(APIAlignment, on_delete=models.SET_NULL, null=True, blank=True)
    background = models.ForeignKey(APIBackground, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=Sex.choices, null=True, blank=True)
    height = models.CharField(max_length=100, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    hair_color = models.CharField(max_length=100, null=True, blank=True)
    eye_color = models.CharField(max_length=100, null=True, blank=True)
    skin_color = models.CharField(max_length=100, null=True, blank=True)
    trait_1 = models.TextField(null=True, blank=True)
    trait_2 = models.TextField(null=True, blank=True)
    ideals = models.TextField(null=True, blank=True)
    bonds = models.TextField(null=True, blank=True)
    flaws = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/characters/', null=True, blank=True)
    faction = models.CharField(max_length=100, null=True, blank=True)
    backstory = models.TextField(null=True, blank=True)


class CharacterSpell(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    spell = models.ForeignKey(APISpell, on_delete=models.CASCADE)
    level_learned = models.IntegerField(null=True, blank=True)


class CharacterClass(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    class_choice = models.ForeignKey(APIClass, on_delete=models.CASCADE)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.character.name} - {self.class_choice.name} (Level {self.level})"