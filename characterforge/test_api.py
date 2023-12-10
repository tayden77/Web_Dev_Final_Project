import requests

def test_get_races():
    response = requests.get('https://www.dnd5eapi.co/api/races')
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

def test_get_classes():
    response = requests.get('https://www.dnd5eapi.co/api/classes')
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

test_get_races()
print()
test_get_classes()