from graph_tft import TFT_team_picker, ArrayGraph
import unittest

class Graph_tft_test(unittest.TestCase):
    def test_init(self):
        team_picker = TFT_team_picker('champions.json', 'classes.json')
        assert len(team_picker.champions) == team_picker.graph.size # All the champs are vertices on the graph.

    def adding_edges(self):
        team_picker = TFT_team_picker('champions.json', 'classes.json')
        assert len(team_picker.graph.vertices[0].edges) == 11
        assert team_picker.graph.vertices[0].key_ == 'aatrox'
