import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Nae wallet required until I dae the extension")

    def test_song_has_name(self):
        self.assertEqual("Nae wallet required until I dae the extension", self.song.name)