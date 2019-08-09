# coding: utf-8
#!python
# graph_tft.py
# By Timofey Makhlay (github.com/timomak/cs-2.2)

import json
from graph import ArrayGraph

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
            # self.classes + [self.origin1, self.origin2]
            self.classes.append(self.origin1)
            self.classes.append(self.origin2)

        else:
            self.origin1 = self.origin1[0].lower()
            self.classes.append(self.origin1)

        if len(self.class1) > 1:
            self.class2 = self.class1[1].lower()
            self.class1 = self.class1[0].lower()
            # self.classes + [self.class2, self.class1]
            self.classes.append(self.class2)
            self.classes.append(self.class1)

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

        self.champions_in_class = class_dict = {'demon': ['aatrox', 'brand', 'elise', 'evelynn', 'morgana', 'swain', 'varus'], 'dragon': ['aurelionsol', 'shyvana'], 'exile': ['yasuo'], 'glacial': ['anivia', 'ashe', 'braum', 'lissandra', 'sejuani', 'volibear'], 'imperial': ['darius', 'draven', 'katarina', 'swain'], 'noble': ['fiora', 'garen', 'kayle', 'leona', 'lucian', 'vayne'], 'ninja': ['akali', 'kennen', 'shen', 'zed'], 'pirate': ['gangplank', 'graves', 'missfortune', 'pyke', 'twistedfate'], 'phantom': ['karthus', 'kindred', 'mordekaiser'], 'robot': ['blitzcrank'], 'void': ['chogath', 'kassadin', 'khazix', 'reksai'], 'wild': ['ahri', 'gnar', 'nidalee', 'rengar', 'warwick'], 'yordle': ['gnar', 'kennen', 'lulu', 'poppy', 'tristana', 'veigar'], 'assassin': ['akali', 'evelynn', 'katarina', 'khazix', 'pyke', 'rengar', 'zed'], 'blademaster': ['aatrox', 'draven', 'fiora', 'gangplank', 'shen', 'yasuo'], 'brawler': ['blitzcrank', 'chogath', 'reksai', 'volibear', 'warwick'], 'elementalist': ['anivia', 'brand', 'kennen', 'lissandra'], 'guardian': ['braum', 'leona'], 'gunslinger': ['gangplank', 'graves', 'lucian', 'missfortune', 'tristana'], 'knight': ['darius', 'garen', 'kayle', 'mordekaiser', 'poppy', 'sejuani'], 'ranger': ['ashe', 'kindred', 'varus', 'vayne'], 'shapeshifter': ['elise', 'gnar', 'nidalee', 'shyvana', 'swain'], 'sorcerer': ['ahri', 'aurelionsol', 'karthus', 'kassadin', 'lulu', 'morgana', 'twistedfate', 'veigar']}

        self.graph = ArrayGraph(self.champions)
        self._add_edges()

        self.first_champ = input("First Champ:").lower() # User inputs key for first champion

        self.first_champ_class_selection = self.graph.find_all_champs_same_class_as(self.first_champ) # O(6273) { 'yordle': set('kennen', ...), ...}

        self.extract_data_from_(self.first_champ_class_selection) # O(441) Prints data.

        self.graph.find_important_data(self.first_champ)

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

    def _add_edges(self):
        """
        Given the graph with all the champions, add edges to connect people of the same class.
        Runtime: O(n^3) Probably even worse because of graph.AddEdge.
        """
        for class_ in self.champions_in_class.keys(): # For each class
            for champ in self.champions_in_class[class_]: # For each Champ of that class
                for champ_of_same_class in self.champions_in_class[class_]: # Loop to all the other champions of the same class.
                    if champ != champ_of_same_class: # Don't connect to itself
                        # print("Champ 1: {}, Champ 2: {}".format(champ,champ_of_same_class))
                        self.graph.addEdge(fromVert=champ, toVert=champ_of_same_class) # Connect Champ and all the champs of same class.

    def extract_data_from_(self, matches):
        """
        Find champions that are repeated within the first_champ_class_selection dict.
        Runtime: O(441) = O(3) * O(7) * O(21)
        """
        all_matching_class_champions = []
        doubles = []
        for class_ in matches.keys(): # O(3) Worse
            champs_in_class_ = [i.champ.key_ for i in matches[class_]]
            print("For {} class:{}\n".format(class_.upper(), champs_in_class_))
            for champ in matches[class_]: # O(7) Worse
                if champ not in all_matching_class_champions: # O(21) Worse
                    all_matching_class_champions.append(champ)
                else:
                    if champ.champ.key_ != self.first_champ:
                        doubles.append(champ)

        # print("All Mathcing Champs:", all_matching_class_champions)
        # print("Doubles:",doubles)
        if len(doubles) > 0:
            print("MUST GET:", [c.champ.key_ for c in doubles], "\n")


    def __repr__(self):
        """Return a string represenation of this Champion"""
        return 'TFT(Champion Count: {!r}, Classes Count: {})'.format(len(self.champions), len(self.classes))

def main():
    """
    Makes the world go round.
    """
    print("STARTING")
    team_picker = TFT_team_picker('champions.json', 'classes.json')

if __name__ == '__main__':
    main()
