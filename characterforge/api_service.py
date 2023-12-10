import requests


def get_races():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/races/')
        response.raise_for_status()
        data = response.json()
        print("Races fetched: ", data)
        return [(race['index'], race['name']) for race in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return []
    

def get_classes():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/classes/')
        response.raise_for_status()
        data = response.json()
        print("Classes fetched: ", data)
        return [(class_choice['index'], class_choice['name']) for class_choice in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None
    

def get_ability_scores():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/ability-scores/')
        response.raise_for_status()
        data = response.json()
        print("Abilities Scores fetched ", data)
        return [(ability_score['index'], ability_score['name']) for ability_score in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None


def get_feats():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/feats/')
        response.raise_for_status()
        data = response.json()
        print("Feats fetched ", data)
        return [(feat['index'], feat['name']) for feat in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None


def get_alignments():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/alignments/')
        response.raise_for_status()
        data = response.json()
        print("Alignments fetched ", data)
        return [(alignment['index'], alignment['name']) for alignment in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None


def get_backgrounds():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/backgrounds/')
        response.raise_for_status()
        data = response.json()
        print("Backgrounds fetched ", data)
        return [(background['index'], background['name']) for background in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None


def get_proficiencies():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/proficiencies/')
        response.raise_for_status()
        data = response.json()
        print("Proficiencies fetched ", data)
        return [(proficiency['index'], proficiency['name']) for proficiency in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None


def get_spells():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/spells/')
        response.raise_for_status()
        data = response.json()
        print("Spells fetched ", data)
        return [(spell['index'], spell['name']) for spell in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None  
    

def get_equipment():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/equipment/')
        response.raise_for_status()
        data = response.json()
        print("Equipment fetched ", data)
        return [(eq['index'], eq['name']) for eq in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None


def get_magic_items():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/magic-items/')
        response.raise_for_status()
        data = response.json()
        print("Magic Items fetched ", data)
        return [(item['index'], item['name']) for item in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None
    

def get_skills():
    try:
        response = requests.get('https://www.dnd5eapi.co/api/skills/')
        response.raise_for_status()
        data = response.json()
        print("Skills fetched ", data)
        return [(skill['index'], skill['name']) for skill in data.get('results', [])]
    except requests.RequestException as e:
        print(e)
        return None