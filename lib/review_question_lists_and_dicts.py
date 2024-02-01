## QUESTION 1

pokemon = [
    {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "is_default": True,
        "order": 1,
        "weight": 69,
        "abilities": [
            {
                "is_hidden": True,
                "slot": 3,
                "ability": {
                    "name": "chlorophyll",
                    "url": "http://pokeapi.co/api/v2/ability/34/",
                },
            }
        ],
    },
    {
        "id": 3,
        "name": "venesaur",
        "base_experience": 50,
        "height": 10,
        "is_default": True,
        "order": 1,
        "weight": 90,
        "abilities": [
            {
                "is_hidden": True,
                "slot": 3,
                "ability": {
                    "name": "fire",
                    "url": "http://pokeapi.co/api/v2/ability/38/",
                },
            }
        ],
    },
    {
        "id": 2,
        "name": "pikachu",
        "base_experience": 60,
        "height": 4,
        "is_default": True,
        "order": 1,
        "weight": 37,
        "abilities": [
            {
                "is_hidden": True,
                "slot": 3,
                "ability": {
                    "name": "lightning",
                    "url": "http://pokeapi.co/api/v2/ability/30/",
                },
            }
        ],
    },
]


# How would you get the url for Bulbasaur's ability?
def get_bulbasaur_url():
    for pokemonObjs in pokemon:
        if pokemonObjs["name"] == 'bulbasaur':
            return pokemon[0]['abilities'][0]['ability']['url']

print(get_bulbasaur_url())

#list comprehension
pokemon_base = [pokemonObjs['abilities'][0]['ability']['url'] for pokemonObjs in pokemon if pokemonObjs['name'] == 'bulbasaur']
print(pokemon_base[0])

# How would you return the first pokemon with base experience over 40?
def pokemon_base_40():
    for pokemonObjs in pokemon:
        if pokemonObjs["base_experience"] > 40:
            return pokemonObjs['name']


# How would you return ALL OF THE pokemon with base experience over 40? (Gotta catch em all)
# How would you return an array of all of the pokemon's names?
# How would you determine whether or not the pokemon array contained any pokemon with a weight greater than 60?
# Whatever method you use should return True if there are any such pokemon, False if not.
