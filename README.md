# TFT (League of Legends) Team Picker

> Have your team decided for you depending on your first selected champion.

![tft](tft-chart.jpg)

## Project Description

I will be modeling a Graph ADT (Abstract Data Structure) to take in data of all the champions and classes in TFT(Team Fight Tactics). I will create a graph with the champions as the vertices and the champion's inherited classes as edges. All the champions of the same class are gonna be interconnected. Given the first selected champion by the user, the graph will generate a set of champions that can be picked within the game to receive the most optimal team combination with the most in game bonuses.

## Project Problems

* Which champions should I build based on your first champion?
* Which champions should I keep an eye for? (Must have champions)
* Which items go well with my first champion?

# Usage
## Run
```
python graph_tft.py
```

## Input (example)
```
First Champ:tristana
```

## Output (example)
```
TRISTANA's classes are: ['yordle', 'gunslinger']

For YORDLE class:['poppy', 'veigar', 'gnar', 'lulu', 'kennen', 'tristana']

For GUNSLINGER class:['lucian', 'missfortune', 'gangplank', 'graves', 'tristana']

Best Item Combination for TRISTANA: ['titanichydra', 'cursedblade', 'redbuff']
```
