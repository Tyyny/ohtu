import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
#    def test_sort_by_points_returns_correct(self):
#        self.player = self.statistics._players[0]
#        self.points = self.statistics.sort_by_points(self.player)
#        self.assertAlmostEquals(self.points, 16)
    
    def test_konstruktori_luo_listan_pelaajista(self):
        self.assertAlmostEqual(len(self.statistics._players), 5)
        
    def test_search_loytaa_pelaajan_nimella(self):
        pelaaja = self.statistics.search("Kurri")
        self.assertEqual(pelaaja, self.statistics._players[2])

    def test_search_palauttaa_none_jos_pelaajaa_ei_ole(self):
        pelaaja = self.statistics.search("Koira")
        self.assertEqual(pelaaja, None)    
    
    def test_team_palauttaa_oikean_pituisen_listan(self):
        lista = self.statistics.team("EDM")
        self.assertAlmostEqual(len(lista), 3)

    def test_top_palauttaa_oikean_pituisen_listan(self):
        lista = self.statistics.top(3)
        self.assertAlmostEqual(len(lista), 4)