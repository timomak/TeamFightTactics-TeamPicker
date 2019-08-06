# More info on these dicts in team_picker_setup.py
dict = {1: {'exile': ['yasuo'], 'robot': ['blitzcrank']}, 2: {'dragon': ['aurelionsol', 'shyvana'], 'phantom': ['karthus', 'kindred', 'mordekaiser'], 'guardian': ['braum', 'leona']}, 3: {'pirate': ['gangplank', 'graves', 'missfortune', 'pyke', 'twistedfate'], 'void': ['chogath', 'kassadin', 'khazix', 'reksai'], 'elementalist': ['anivia', 'brand', 'kennen', 'lissandra'], 'shapeshifter': ['elise', 'gnar', 'nidalee', 'shyvana', 'swain']}, 4: {'imperial': ['darius', 'draven', 'katarina', 'swain'], 'ninja': ['akali', 'kennen', 'shen', 'zed'], 'wild': ['ahri', 'gnar', 'nidalee', 'rengar', 'warwick'], 'brawler': ['blitzcrank', 'chogath', 'reksai', 'volibear', 'warwick'], 'gunslinger': ['gangplank', 'graves', 'lucian', 'missfortune', 'tristana'], 'ranger': ['ashe', 'kindred', 'varus', 'vayne']}, 6: {'demon': ['aatrox', 'brand', 'elise', 'evelynn', 'morgana', 'swain', 'varus'], 'glacial': ['anivia', 'ashe', 'braum', 'lissandra', 'sejuani', 'volibear'], 'noble': ['fiora', 'garen', 'kayle', 'leona', 'lucian', 'vayne'], 'yordle': ['gnar', 'kennen', 'lulu', 'poppy', 'tristana', 'veigar'], 'assassin': ['akali', 'evelynn', 'katarina', 'khazix', 'pyke', 'rengar', 'zed'], 'blademaster': ['aatrox', 'draven', 'fiora', 'gangplank', 'shen', 'yasuo'], 'knight': ['darius', 'garen', 'kayle', 'mordekaiser', 'poppy', 'sejuani'], 'sorcerer': ['ahri', 'aurelionsol', 'karthus', 'kassadin', 'lulu', 'morgana', 'twistedfate', 'veigar']}}

champ_dict = {'aatrox': ['demon', 'blademaster'], 'ahri': ['wild', 'sorcerer'], 'akali': ['ninja', 'assassin'], 'anivia': ['glacial', 'elementalist'], 'ashe': ['glacial', 'ranger'], 'aurelionsol': ['dragon', 'sorcerer'], 'blitzcrank': ['robot', 'brawler'], 'brand': ['demon', 'elementalist'], 'braum': ['glacial', 'guardian'], 'chogath': ['void', 'brawler'], 'darius': ['imperial', 'knight'], 'draven': ['imperial', 'blademaster'], 'elise': ['demon', 'shapeshifter'], 'evelynn': ['demon', 'assassin'], 'fiora': ['noble', 'blademaster'], 'gangplank': ['pirate', 'gunslinger', 'blademaster'], 'garen': ['noble', 'knight'], 'gnar': ['wild', 'yordle', 'shapeshifter'], 'graves': ['pirate', 'gunslinger'], 'karthus': ['phantom', 'sorcerer'], 'kassadin': ['void', 'sorcerer'], 'katarina': ['imperial', 'assassin'], 'kayle': ['noble', 'knight'], 'kennen': ['ninja', 'yordle', 'elementalist'], 'khazix': ['void', 'assassin'], 'kindred': ['phantom', 'ranger'], 'leona': ['noble', 'guardian'], 'lissandra': ['glacial', 'elementalist'], 'lucian': ['noble', 'gunslinger'], 'lulu': ['yordle', 'sorcerer'], 'missfortune': ['pirate', 'gunslinger'], 'mordekaiser': ['phantom', 'knight'], 'morgana': ['demon', 'sorcerer'], 'nidalee': ['wild', 'shapeshifter'], 'poppy': ['yordle', 'knight'], 'pyke': ['pirate', 'assassin'], 'reksai': ['void', 'brawler'], 'rengar': ['wild', 'assassin'], 'sejuani': ['glacial', 'knight'], 'shen': ['ninja', 'blademaster'], 'shyvana': ['dragon', 'shapeshifter'], 'swain': ['imperial', 'demon', 'shapeshifter'], 'tristana': ['yordle', 'gunslinger'], 'twistedfate': ['pirate', 'sorcerer'], 'varus': ['demon', 'ranger'], 'vayne': ['noble', 'ranger'], 'veigar': ['yordle', 'sorcerer'], 'volibear': ['glacial', 'brawler'], 'warwick': ['wild', 'brawler'], 'yasuo': ['exile', 'blademaster'], 'zed': ['ninja', 'assassin']}

class_dict = {'demon': ['aatrox', 'brand', 'elise', 'evelynn', 'morgana', 'swain', 'varus'], 'dragon': ['aurelionsol', 'shyvana'], 'exile': ['yasuo'], 'glacial': ['anivia', 'ashe', 'braum', 'lissandra', 'sejuani', 'volibear'], 'imperial': ['darius', 'draven', 'katarina', 'swain'], 'noble': ['fiora', 'garen', 'kayle', 'leona', 'lucian', 'vayne'], 'ninja': ['akali', 'kennen', 'shen', 'zed'], 'pirate': ['gangplank', 'graves', 'missfortune', 'pyke', 'twistedfate'], 'phantom': ['karthus', 'kindred', 'mordekaiser'], 'robot': ['blitzcrank'], 'void': ['chogath', 'kassadin', 'khazix', 'reksai'], 'wild': ['ahri', 'gnar', 'nidalee', 'rengar', 'warwick'], 'yordle': ['gnar', 'kennen', 'lulu', 'poppy', 'tristana', 'veigar'], 'assassin': ['akali', 'evelynn', 'katarina', 'khazix', 'pyke', 'rengar', 'zed'], 'blademaster': ['aatrox', 'draven', 'fiora', 'gangplank', 'shen', 'yasuo'], 'brawler': ['blitzcrank', 'chogath', 'reksai', 'volibear', 'warwick'], 'elementalist': ['anivia', 'brand', 'kennen', 'lissandra'], 'guardian': ['braum', 'leona'], 'gunslinger': ['gangplank', 'graves', 'lucian', 'missfortune', 'tristana'], 'knight': ['darius', 'garen', 'kayle', 'mordekaiser', 'poppy', 'sejuani'], 'ranger': ['ashe', 'kindred', 'varus', 'vayne'], 'shapeshifter': ['elise', 'gnar', 'nidalee', 'shyvana', 'swain'], 'sorcerer': ['ahri', 'aurelionsol', 'karthus', 'kassadin', 'lulu', 'morgana', 'twistedfate', 'veigar']}

class_bonus_dict = {'demon': 6, 'dragon': 2, 'exile': 1, 'glacial': 6, 'imperial': 4, 'noble': 6, 'ninja': 4, 'pirate': 3, 'phantom': 2, 'robot': 1, 'void': 3, 'wild': 4, 'yordle': 6, 'assassin': 6, 'blademaster': 6, 'brawler': 4, 'elementalist': 3, 'guardian': 2, 'gunslinger': 4, 'knight': 6, 'ranger': 4, 'shapeshifter': 3, 'sorcerer': 6}

def help_me(first):
    """
    Given the first champion, output who I should build.
    Runtime:
    """
    # first = input("Name of your first chamption: ").lower()

    perfect_team = {}
    team = [first]
    classes = champ_dict[first]
    remaining_slots = 8

    remaining_for_bonus = class_bonus_dict[classes[0]] - 1

    print(remaining_for_bonus, "more for ", classes[0], " bonus")


    current_class = classes[0]
    perfect_team.update({current_class: [first]})

    for i in range(remaining_for_bonus): # Loop for each remaining slot for the bonus.

        new_champ = None

        # If the character is not already inside the perfect team, add it within the correct class.
        if class_dict[current_class][i] not in perfect_team[current_class]:

            # Adding the new character to the perfect team
            new_champ = class_dict[current_class][i]
            perfect_team[current_class] += [new_champ]
            team.append(new_champ)

        else:
            # Adding the new character to the perfect team
            new_champ = class_dict[current_class][i+1]
            perfect_team[current_class] += [new_champ]
            team.append(new_champ)


        for c in champ_dict[new_champ]:
            if c not in classes:
                classes.append(c)

        remaining_slots -= 1
    # Working this far.

    # TODO: Build the rest of the team. Figure out what the next class should be.
    if remaining_slots == 5: # There is no bonus with exaclty 5 characters.
        # Do 2 more classes.
        print("NO CLASS WITH 5")

        
        pass
    else:
        options_for_next_class = dict[remaining_slots] # All classes that need all the current remaining slots.
        next_class = None # Class that is already present in list and is an option in the list above.

        for c in classes: # Finding a match
            if c in options_for_next_class.keys():
                next_class = c
                break
        if next_class == None: # No matches
            # TODO: Pick at random.
            print("NO MATCHES FOUND")

        # print("Next Class: ", next_class)

        slots_for_next = 0
        options_for_next_champ = list(set(class_dict[next_class]) - set(team))

        # print("Options for {} class: {}".format(next_class, options_for_next_champ))

        perfect_team.update({next_class : []})
        for count in range(remaining_slots):
            new_class_champ = options_for_next_champ[count]
            perfect_team[next_class].append(new_class_champ)
            remaining_slots -= 1

            team.append(new_class_champ)
            for c in champ_dict[new_class_champ]:
                if c not in classes:
                    classes.append(c)



    print("Perfect Team:",perfect_team)
    print("Team:",team)
    print("Classes:", classes)
    print("Remaining Slots:", remaining_slots)



help_me('kennen')
