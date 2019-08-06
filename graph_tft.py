# coding: utf-8
#!python
# graph_tft.py
# By Timofey Makhlay (github.com/timomak/cs-2.2)

import json

class Champion(object):
    def __init__(self, json):
        """
        Creating champion object from JSON data.
        """
        self.id = json['id']
        self.key_ = json['key'].lower() # name
        self.name = json['name']
        self.origin1 = json['origin'] # Array of 2 at most
        self.origin2 = None # Not all Champs have 2 Origins
        self.class1 = json['class'] # Array of 2 at most
        self.class2 = None # Not all Champs have 2 Classes
        self.cost = json['cost']
        self.ability = json['ability']
        self.stats = json['stats']
        self.items = json['items']
        self.classes = []

        # Adjusting for characters with more than one class or origin attributes.
        if len(self.origin1) > 1:
            self.origin2 = self.origin1[1].lower()
            self.origin1 = self.origin1[0].lower()
            self.classes + [self.origin1, self.origin2]

        else:
            self.origin1 = self.origin1[0].lower()
            self.classes.append(self.origin1)

        if len(self.class1) > 1:
            self.class2 = self.class1[1].lower()
            self.class1 = self.class1[0].lower()
            self.classes + [self.class2, self.class1]

        else:
            self.class1 = self.class1[0].lower()
            self.classes.append(self.class1)



    def __repr__(self):
        """Return a string represenation of this Champion"""
        return 'Champion(key: {!r}, classes: {})'.format(self.key_, self.classes)

class Champion_Class(object):

    def __init__(self, json):
        """Creating class data from json data"""
        self.key = json['key'] # String
        self.name = json['name'] # String
        self.description = json['description'] # String
        self.accentChampionImage = json['accentChampionImage'] # URL as String
        self.bonuses = json['bonuses'] # Array [{'needed': int, 'effect': string}]
        # self.needed = self.bonuses[-1]['needed'] # Check the highest number for needed. (In this case it's the last item in the array)

    def __repr__(self):
        """Return a string represenation of this Champion"""
        return 'Class(key: {!r})'.format(self.key)

class TFT_team_picker(object):

    def __init__(self, champ_file, class_file):
        """Initializing the Team Fight Tactics Team Picker based on the game data stored in JSON files."""
        self.champions = self.create_champ_list(champ_file) # O(n)
        self.classes, self.class_bonus, self.max_bonus, self.classes_dict = self.create_classes_list(class_file) # O(n) * O(3)

    def create_champ_list(self, filename):
        """
        Using the JSON file and the champions class, make a list containing all the champions.
        Runtime: O(n) number of champs.
        """
        champions = [] # [Champion(key: 'aatrox', classes: ['demon', 'blademaster']), ...]

        with open(filename) as json_file: # Open JSON File
            data = json.load(json_file) # Get the JSON
            for champ_obj in data.items(): # O(n) ('aatrox' : { **aatrox data** } )

                # Creating Champions Class Object
                new_champ = Champion(champ_obj[1])
                champions.append(new_champ)

        return champions

    def create_classes_list(self, filename):
        """
        Open JSON file and read the data for the Classes (and Origins).
        filename - the file name as a string.
        Runtime: O(n) * O(3) number of classes.
        """
        classes = [] # [Class(key: 'exile'), Class(key: 'ninja'), ... ]
        class_bonus = { 1: [], 2: [], 3: [], 4 : [], 6 : []} # {1: [Class(key: 'exile'), Class(key: 'ninja'), ...], 2: [...], ... }
        max_bonus = { 1: [], 2: [], 3: [], 4 : [], 6 : []} # {1: [Class(key: 'exile'), Class(key: 'robot')], 2: [...], ... }
        classes_dict = {} # {'assassin': Class('assassin'), ...}
        with open(filename) as json_file:
            data = json.load(json_file)
            for class_obj in data.items(): # O(n)

                # Creating Classes Class Objects
                new_class = Champion_Class(class_obj[1])
                classes.append(new_class)

                # All bonus Tracking
                bonuses = class_obj[1]['bonuses']
                for bonus in bonuses: # O(3) worst case.
                    class_bonus[bonus['needed']] += [new_class]

                # Max Bonus Tracking
                max_bonus[bonuses[-1]['needed']] += [new_class]

                # Creating a class dict.
                classes_dict.update({new_class.key: new_class})

        return classes, class_bonus, max_bonus, classes_dict

    def __repr__(self):
        """Return a string represenation of this Champion"""
        return 'TFT(Champion Count: {!r}, Classes Count: {})'.format(len(self.champions), len(self.classes))

def main():
    """
    Makes the world go round.
    """
    team_picker = TFT_team_picker('champions.json', 'classes.json')
    print(team_picker)

if __name__ == '__main__':
    main()
