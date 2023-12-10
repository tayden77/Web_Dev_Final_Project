from django import forms
from .models import Character, Sex
from .api_service import *

# Forms for setting specific character options
class RaceForm(forms.Form):
    race = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        race_choices = kwargs.pop('race_choices', [])
        super(RaceForm, self).__init__(*args, **kwargs)
        self.fields['race'].choices = race_choices
        print("Race choices in RaceForm:", self.fields['race'].choices)

class ClassForm(forms.Form):
    class_choice = forms.ChoiceField(choices=[])
    level = forms.IntegerField(label='Level', initial=1, max_value=20)

    def __init__(self, *args, **kwargs):
        class_choices = kwargs.pop('class_choices', [])
        super(ClassForm, self).__init__(*args, **kwargs)
        self.fields['class_choice'].choices = class_choices
        print("Class choices in ClassForm:", self.fields['class_choice'].choices)

class AbilityScoreForm(forms.Form):
    strength = forms.IntegerField(label='Strength', initial=8)
    dexterity = forms.IntegerField(label='Dexterity', initial=8)
    constitution = forms.IntegerField(label='Constitution', initial=8)
    intelligence = forms.IntegerField(label='Intelligence', initial=8)
    wisdom = forms.IntegerField(label='Wisdom', initial=8)
    charisma = forms.IntegerField(label='Charisma', initial=8)

class FeatForm(forms.Form):
    feat = forms.MultipleChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        feat_choices = kwargs.pop('feat_choices', [])
        super(FeatForm, self).__init__(*args, **kwargs)
        self.fields['feat'].choices = feat_choices
        print("Feat choices in FeatForm:", self.fields['feat'].choices)

class AlignmentForm(forms.Form):
    alignment = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        alignment_choices = kwargs.pop('alignment_choices', [])
        super(AlignmentForm, self).__init__(*args, **kwargs)
        self.fields['alignment'].choices = alignment_choices

class BackgroundForm(forms.Form):
    background = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        background_choices = kwargs.pop('background_choices', [])
        super(BackgroundForm, self).__init__(*args, **kwargs)
        self.fields['background'].choices = background_choices

class SkillForm(forms.Form):
    skill = forms.MultipleChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        skill_choices = kwargs.pop('skill_choices', [])
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['skill'].choices = skill_choices

class ProficiencyForm(forms.Form):
    proficiency = forms.MultipleChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        proficiency_choices = kwargs.pop('proficiency_choices', [])
        super(ProficiencyForm, self).__init__(*args, **kwargs)
        self.fields['proficiency'].choices = proficiency_choices

class SpellForm(forms.Form):
    spell = forms.MultipleChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        spell_choices = kwargs.pop('spell_choices', [])
        super(SpellForm, self).__init__(*args, **kwargs)
        self.fields['spell'].choices = spell_choices

class EquipmentForm(forms.Form):
    eq = forms.MultipleChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        other_items = kwargs.pop('other_items', [])
        super(EquipmentForm, self).__init__(*args, **kwargs)
        if other_items:
            self.fields['eq'].choices = other_items
        else:
            self.fields['eq'].choices = []
            self.fields['item'].widget.attrs['disabled'] = True

class MagicItemForm(forms.Form):
    item = forms.MultipleChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        magic_items = kwargs.pop('magic_items', [])
        super(MagicItemForm, self).__init__(*args, **kwargs)
        if magic_items:
            self.fields['item'].choices = magic_items
        else:
            self.fields['item'].choices = []
            self.fields['item'].widget.attrs['disabled'] = True

class DescriptionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    age = forms.IntegerField()
    sex = forms.ChoiceField(choices=Sex.choices)
    height = forms.CharField(widget=forms.TextInput())
    weight = forms.FloatField()
    hair_color = forms.CharField(widget=forms.TextInput())
    eye_color = forms.CharField(widget=forms.TextInput())
    skin_color = forms.CharField(widget=forms.TextInput())
    trait1 = forms.CharField(widget=forms.Textarea())
    trait2 = forms.CharField(widget=forms.Textarea())
    ideals = forms.CharField(widget=forms.Textarea())
    bonds = forms.CharField(widget=forms.Textarea())
    flaws = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    faction = forms.CharField(widget=forms.TextInput())
    backstory = forms.CharField(widget=forms.Textarea())

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'

# Future Additions: Add Homebrew Forms for custom races, classes, etc.