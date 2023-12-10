from django.shortcuts import render, redirect, get_object_or_404
from formtools.wizard.views import SessionWizardView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.db import IntegrityError
from .models import *
from .forms import *
from .api_service import *


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            next_url = request.POST.get("next", "index")
            return redirect(next_url)
        else:
            return render(request, "characterforge/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        next_url = request.GET.get("next", "index")
        return render(request, "characterforge/login.html", {"next": next_url})


def logout_view(request):
    logout(request)
    return redirect("index")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "characterforge/register.html", {
                "message": "Passwords must match."
            })
        
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "characterforge/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect("index")
    else:
        return render(request, "characterforge/register.html")


@login_required(login_url='login')
def index(request):
    return render(request, 'characterforge/index.html')


# Form Processing Flow: index.html --> RaceForm, ClassForm, AbilityScoreForm, FeatForm, AlignmentForm, BackgroundForm, 
#                       SkillForm, ProficiencyForm, SpellForm, EquipmentForm, MagicItemForm, DescriptionForm


# Initialize the Character object
@login_required(login_url='login')   
def initailize_character(request):
    character = Character.objects.create(
        user=request.user,
        strength=10,  # default value
        dexterity=10, # default value
        constitution=10, # default value
        intelligence=10, # default value
        wisdom=10, # default value
        charisma=10, # default value
        name="Character Name", # default name
        # Set foreign keys to None initially or to a default value if you have one
        race=None, 
        alignment=None, 
        background=None,
        # Set optional fields to None or default values
        age=None,
        sex=None,
        height="",
        weight=None,
        hair_color="",
        eye_color="",
        skin_color="",
        trait_1="",
        trait_2="",
        ideals="",
        bonds="",
        flaws="",
        image=None,
        faction="",
        backstory=""
    )
    return redirect('character-race', character_id=character.id)

# Handle RaceForm
@login_required(login_url='login')   
def character_race(request, character_id):
    character = Character.objects.get(id=character_id)
    race_choices = APIRace.objects.all().values_list('id', 'name')
    if request.method == 'POST':
        form = RaceForm(request.POST, race_choices=race_choices)
        if form.is_valid():
            race_id = form.cleaned_data['race']
            character.race = APIRace.objects.get(id=race_id)
            character.save()
            return redirect('character-class', character_id=character.id)
    else:
        form = RaceForm(race_choices=race_choices)
    return render(request, 'characterforge/character_race.html', {'form': form, 'character_id': character_id})

# Handle ClassForm
@login_required(login_url='login')   
def character_class(request, character_id):
    character = Character.objects.get(id=character_id)
    class_choices = APIClass.objects.all().values_list('id', 'name')
    if request.method == 'POST':
        form = ClassForm(request.POST, class_choices=class_choices)
        if form.is_valid():
            class_id = form.cleaned_data['class_choice']
            selected_class = APIClass.objects.get(id=class_id)
            character.classes.add(selected_class)
            character.save()
            return redirect('character-ability-scores', character_id=character.id)
    else:
        form = ClassForm(class_choices=class_choices)
    return render(request, 'characterforge/character_class.html', {'form': form, 'character_id': character_id})

# Handle AbilityScoreForm
@login_required(login_url='login')   
def character_ability_score(request, character_id):
    character = Character.objects.get(id=character_id)
    if request.method == 'POST':
        form = AbilityScoreForm(request.POST)
        if form.is_valid():
            character.strength = form.cleaned_data['strength']
            character.dexterity = form.cleaned_data['dexterity']
            character.constitution = form.cleaned_data['constitution']
            character.intelligence = form.cleaned_data['intelligence']
            character.wisdom = form.cleaned_data['wisdom']
            character.charisma = form.cleaned_data['charisma']
            character.save()
            return redirect('character-feat', character_id=character.id)
    else:
        form = AbilityScoreForm()
    return render(request, 'characterforge/character_ability_scores.html', {'form': form, 'character_id': character_id})

# Handle FeatForm
@login_required(login_url='login')   
def character_feat(request, character_id):
    character = Character.objects.get(id=character_id)
    feat_choices = APIFeat.objects.all().values_list('id', 'name')
    if request.method == 'POST':
        form = FeatForm(request.POST, feat_choices=feat_choices)
        if form.is_valid():
            feat_ids = form.cleaned_data['feat']
            for feat_id in feat_ids:
                selected_feat = APIFeat.objects.get(id=feat_id)
                character.feats.add(selected_feat)
            return redirect('character-alignment', character_id=character.id)
    else:
        form = FeatForm(feat_choices=feat_choices)
    return render(request, 'characterforge/character_feat.html', {'form': form, 'character_id': character_id})

# Handle AlignmentForm
@login_required(login_url='login')   
def character_alignment(request, character_id):
    character = Character.objects.get(id=character_id)
    alignment_choices = APIAlignment.objects.all().values_list('id', 'name')
    if request.method == 'POST':
        form = AlignmentForm(request.POST, alignment_choices=alignment_choices)
        if form.is_valid():
            alignment_id = form.cleaned_data['alignment']
            character.alignment = APIAlignment.objects.get(id=alignment_id)
            character.save()
            return redirect('character-background', character_id=character.id)
    else:
        form = AlignmentForm(alignment_choices=alignment_choices)
    return render(request, 'characterforge/character_alignment.html', {'form': form, 'character_id': character_id})

# Handle BackgroundForm
@login_required(login_url='login')   
def character_background(request, character_id):
    character = Character.objects.get(id=character_id)
    background_choices = APIBackground.objects.all().values_list('id', 'name')
    if request.method == 'POST':
        form = BackgroundForm(request.POST, background_choices=background_choices)
        if form.is_valid():
            background_id = form.cleaned_data['background']
            character.background = APIBackground.objects.get(id=background_id)
            character.save()
            return redirect('character-skill', character_id=character.id)
    else:
        form = BackgroundForm(background_choices=background_choices)
    return render(request, 'characterforge/character_background.html', {'form': form, 'character_id': character_id})

# Handle SkillForm
@login_required(login_url='login')   
def character_skill(request, character_id):
    character = Character.objects.get(id=character_id)
    skill_choices = APISkill.objects.all().values_list('id', 'name')
    if request.method == 'POST':
        form = SkillForm(request.POST, skill_choices=skill_choices)
        if form.is_valid():
            skill_ids = form.cleaned_data['skill']
            for skill_id in skill_ids:
                selected_skill = APISkill.objects.get(id=skill_id)
                character.skills.add(selected_skill)
            return redirect('character-proficiency', character_id=character.id)
    else:
        form = SkillForm(skill_choices=skill_choices)
    return render(request, 'characterforge/character_skill.html', {'form': form, 'character_id': character_id})

# Handle ProficiencyForm
@login_required(login_url='login')   
def character_proficiency(request, character_id):
    character = Character.objects.get(id=character_id)
    proficiency_choices = APIProficiency.objects.all().values_list('id', 'name')
    if request.method == 'POST': 
        form = ProficiencyForm(request.POST, proficiency_choices=proficiency_choices)
        if form.is_valid():
            proficiency_ids = form.cleaned_data['proficiency']
            for proficiency_id in proficiency_ids:
                selected_proficiency = APIProficiency.objects.get(id=proficiency_id)
                character.proficiencies.add(selected_proficiency)
            return redirect('character-spell', character_id=character.id)
    else:
        form = ProficiencyForm(proficiency_choices=proficiency_choices)
    return render(request, 'characterforge/character_proficiency.html', {'form': form, 'character_id': character_id})

# Handle SpellForm
@login_required(login_url='login')   
def character_spell(request, character_id):
    character = Character.objects.get(id=character_id)
    spell_choices = APISpell.objects.all().values_list('id', 'name')
    if request.method == 'POST':
        form = SpellForm(request.POST, spell_choices=spell_choices)
        if form.is_valid():
            spell_ids = form.cleaned_data['spell']
            for spell_id in spell_ids:
                selected_spell = APISpell.objects.get(id=spell_id)
                character.spells.add(selected_spell)
            return redirect('character-equipment', character_id=character.id)
    else:
        form = SpellForm(spell_choices=spell_choices)
    return render(request, 'characterforge/character_spell.html', {'form': form, 'character_id': character_id})

# Handle EquipmentForm
@login_required(login_url='login')   
def character_equipment(request, character_id):
    character = Character.objects.get(id=character_id)
    other_items = Equipment.objects.filter(equipment_type='OTHER').values_list('id', 'name')
    if request.method == 'POST':
        form = EquipmentForm(request.POST, other_items=other_items)
        if form.is_valid():
            equipment_ids = form.cleaned_data['eq']
            for equipment_id in equipment_ids:
                selected_eq = Equipment.objects.get(id=equipment_id)
                character.equipment.add(selected_eq)
            return redirect('character-item', character_id=character.id)
    else:
        form = EquipmentForm(other_items=other_items)
    return render(request, 'characterforge/character_equipment.html', {'form': form, 'character_id': character_id})

# Handle MagicItemForm
@login_required(login_url='login')   
def character_item(request, character_id):
    character = Character.objects.get(id=character_id)
    magic_items = Equipment.objects.filter(equipment_type='MAGIC').values_list('id', 'name')
    if request.method == 'POST':
        form = MagicItemForm(request.POST, magic_items=magic_items)
        if form.is_valid():
            item_ids = form.cleaned_data['item']
            for item_id in item_ids:
                selected_item = Equipment.objects.get(id=item_id)
                character.equipment.add(selected_item)
            return redirect('character-description', character_id=character.id)
    else:
        form = MagicItemForm(magic_items=magic_items)
    return render(request, 'characterforge/character_item.html', {'form': form, 'character_id': character_id})

# Handle DescriptionForm
@login_required(login_url='login')   
def character_description(request, character_id):
    character = Character.objects.get(id=character_id)
    if request.method == 'POST':
        form = DescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            character.name = form.cleaned_data['name']
            character.age = form.cleaned_data['age']
            character.sex = form.cleaned_data['sex']
            character.height = form.cleaned_data['height']
            character.weight = form.cleaned_data['weight']
            character.hair_color = form.cleaned_data['hair_color']
            character.eye_color = form.cleaned_data['eye_color']
            character.skin_color = form.cleaned_data['skin_color']
            character.trait_1 = form.cleaned_data['trait1']
            character.trait_2 = form.cleaned_data['trait2']
            character.ideals = form.cleaned_data['ideals']
            character.bonds = form.cleaned_data['bonds']
            character.flaws = form.cleaned_data['flaws']
            character.faction = form.cleaned_data['faction']
            character.backstory = form.cleaned_data['backstory']
            if 'image' in request.FILES:
                character.image = request.FILES['image']
            character.save()
            return redirect('confirm-character', character_id=character.id)
    else:
        form = DescriptionForm()
    return render(request, 'characterforge/character_description.html', {'form': form, 'character_id': character_id})


@login_required(login_url='login')
def confirm_character(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    print("Character Details:", character.name, character.race, character.classes)

    if request.method == 'POST':
        character.confirmed = True
        character.save()
        return redirect('character-detail', character_id=character.id)

    return render(request, 'characterforge/confirm_character.html', {'character': character, 'character_id': character_id})


@login_required(login_url='login')
def character_detail_view(request, character_id):
    character = get_object_or_404(Character, id=character_id)

    return render(request, 'characterforge/character_detail.html', {'character': character, 'character_id': character_id})
    

@login_required(login_url='login')    
def character_edit_view(request, character_id):
    character = get_object_or_404(Character, id=character_id, user=request.user)
    form = CharacterForm(instance=character)
    
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('character-detail', character_id=character.id)
        else:
            form = CharacterForm(instance=character)
    return render(request, 'characterforge/edit_character.html', {'form': form, 'character':character, 'character_id': character_id})


@login_required(login_url='login')   
def delete_character(request, character_id):
    character = get_object_or_404(Character, id=character_id, user=request.user)
    if request.method == 'POST':
        character.delete()
        return redirect('character-list')
    return render(request, 'characterforge/confirm_delete.html', {'character': character})
    

@login_required(login_url='login')
def character_list_view(request):
    characters = Character.objects.filter(user=request.user)
    return render(request, 'characterforge/character_list.html', {'characters': characters})
    