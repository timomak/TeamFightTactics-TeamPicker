# https://boards.na.leagueoflegends.com/de/c/teamfight-tactics/pNEWFQMv-teamfight-tactics-developer-api

# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/champions.json
# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/classes.json
# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/items.json
# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/origins.json
# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/tierlist.json

# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

"""
Final Project: Team Fight Tactics (League of Legends) Team Picker

Goal: Get a team with as many possible class boosts.

    • Has to print out all the options for which characters to buy.
        • Has to color code late game champions.
    • Has to show which classes those heroes are in.

Stretch Challenges:
    • Multiple classes choices.
    • Round by round reccomendations.
"""

""" Class Struct
"demon": {
    "key": "demon",
    "name": "Demon",
    "description": "Attacks from Demons have a chance to burn all of an enemy's mana and deal that much true damage.",
    "accentChampionImage": "https://cdn.blitz.gg/blitz/centered/Aatrox_Splash_Centered_0.jpg",
    "bonuses": [
      {
        "needed": 2,
        "effect": "25% chance on hit to Mana Burn"
      },
      {
        "needed": 4,
        "effect": "50% chance on hit to Mana Burn"
      },
      {
        "needed": 6,
        "effect": "85% chance on hit to Mana Burn"
      }
    ]
}
"""

""" Champion Struct
  "Aatrox": {
    "id": "266",
    "key": "Aatrox",
    "name": "Aatrox",
    "origin": ["Demon"],
    "class": ["Blademaster"],
    "cost": 3,
    "ability": {
      "name": "The Darkin Blade",
      "description": "Aatrox cleaves the area in front of him, dealing damage to enemies inside it.",
      "type": "Active",
      "manaCost": 75,
      "manaStart": 0,
      "stats": [{ "type": "Damage", "value": "400 / 700 / 1000" }]
    },
    "stats": {
      "offense": {
        "damage": 65,
        "attackSpeed": 0.65,
        "dps": 42,
        "range": 1
      },
      "defense": {
        "health": 750,
        "armor": 25,
        "magicResist": 20
      }
    },
    "items": [
      "titanichydra",
      "phantomdancer",
      "dragonsclaw"
    ]
  }
"""

""" The Dict I made with the code below to set up graph.
{1: {'exile': {'yasuo'}, 'robot': {'blitzcrank'}}, 2: {'dragon': {'aurelionsol', 'shyvana'}, 'phantom': {'karthus', 'mordekaiser', 'kindred'}, 'guardian': {'braum', 'leona'}}, 3: {'pirate': {'pyke', 'graves', 'gangplank', 'twistedfate', 'missfortune'}, 'void': {'kassadin', 'chogath', 'reksai', 'khazix'}, 'elementalist': {'lissandra', 'anivia', 'brand', 'kennen'}, 'shapeshifter': {'gnar', 'nidalee', 'swain', 'shyvana', 'elise'}}, 4: {'imperial': {'katarina', 'draven', 'swain', 'darius'}, 'ninja': {'kennen', 'shen', 'zed', 'akali'}, 'wild': {'gnar', 'nidalee', 'warwick', 'rengar', 'ahri'}, 'brawler': {'chogath', 'warwick', 'blitzcrank', 'reksai', 'volibear'}, 'gunslinger': {'tristana', 'lucian', 'graves', 'gangplank', 'missfortune'}, 'ranger': {'vayne', 'varus', 'ashe', 'kindred'}}, 6: {'demon': {'aatrox', 'swain', 'brand', 'morgana', 'evelynn', 'varus', 'elise'}, 'glacial': {'anivia', 'lissandra', 'ashe', 'braum', 'sejuani', 'volibear'}, 'noble': {'kayle', 'lucian', 'leona', 'fiora', 'vayne', 'garen'}, 'yordle': {'gnar', 'tristana', 'poppy', 'veigar', 'lulu', 'kennen'}, 'assassin': {'katarina', 'zed', 'akali', 'rengar', 'evelynn', 'pyke', 'khazix'}, 'blademaster': {'yasuo', 'aatrox', 'gangplank', 'shen', 'fiora', 'draven'}, 'knight': {'kayle', 'poppy', 'darius', 'sejuani', 'mordekaiser', 'garen'}, 'sorcerer': {'morgana', 'aurelionsol', 'veigar', 'kassadin', 'ahri', 'lulu', 'karthus', 'twistedfate'}}}
"""

import json

def _classes_dict(filename):
    """
    Open JSON file and read the data for the Classes (and Origins).
    filename - the file name as a string.
    Runtime: O(n)
    """
    class_dict = {} # {'robot': ['blitzcrank']}
    class_bonus_dict = {}
    dict = { 1: {}, 2: {}, 3: {}, 4 : {}, 6 : {}} # { 1 : { 'robot' : set['blitzcrank'], 'exile' : set['yasuo'] }, 2 : ... }
    with open(filename) as json_file:
        data = json.load(json_file)
        for class_obj in data.items(): # O(n)

            key = class_obj[1]['key'] # String
            name = class_obj[1]['name'] # String
            description = class_obj[1]['description'] # String
            accentChampionImage = class_obj[1]['accentChampionImage'] # URL as String
            bonuses = class_obj[1]['bonuses'] # Array [{'needed': int, 'effect': string}]
            needed = bonuses[-1]['needed'] # Check the highest number for needed. (In this case it's the last item in the array)

            class_dict[key] = []
            class_bonus_dict[key] = needed
            dict[needed].update({class_obj[0]: []})

    return dict

def _champ_dict(dict, filename):
    """
    Sorts the heroes into their place in the dictionary.
    Runtime: O(n) * O(m) * O(5) (Number of champions * Number of classes * 5)
    """
    champ_dict = {} # { 'aatrox' : ['demon', 'blademaster'], ...}
    with open(filename) as json_file:
        data = json.load(json_file)
        for champ_obj in data.items(): # O(n)

            id = champ_obj[1]['id']
            key_ = champ_obj[1]['key'].lower() # name
            name = champ_obj[1]['name']
            origin = champ_obj[1]['origin'] # Array of 2 at most
            origin2 = None # Not all Champs have 2 Origins
            class_ = champ_obj[1]['class'] # Array of 2 at most
            class2 = None # Not all Champs have 2 Classes
            cost = champ_obj[1]['cost']
            ability = champ_obj[1]['ability']
            stats = champ_obj[1]['stats']
            items = champ_obj[1]['items']

            champ_dict[key_] = []

            # Adjusting for characters with more than one class or origin attributes.
            if len(origin) > 1:
                origin2 = origin[1].lower()
                origin = origin[0].lower()
                champ_dict[key_] += [origin, origin2]
                # dict[origin] += [key_]
                # dict[origin2] += [key_]
            else:
                origin = origin[0].lower()
                champ_dict[key_] += [origin]
                # dict[origin] += [key_]

            if len(class_) > 1:
                class2 = class_[1].lower()
                class_ = class_[0].lower()
                champ_dict[key_] += [class_, class2]
                # dict[class_] += [key_]
                # dict[class2] += [key_]
            else:
                class_ = class_[0].lower()
                champ_dict[key_] += [class_]
                # dict[class_] += [key_]


            # print("Name: {}\nOrigin: {}, Origin 2: {}, Class: {}, Class 2: {}".format(name, origin, origin2, class_, class2))

            for range in dict.items(): # O(5)
                for key in range[1]: # Not too expensive as an operation O(m)
                    if key == origin or key == origin2 or key == class_ or key == class2:
                        range[1][key].append(key_)
                        # print(name, "Should be added to ", key, range[1][key])

    return dict#, champ_dict


# print(_classes_dict('classes.json'))
print(_champ_dict(_classes_dict('classes.json'), 'champions.json'))
