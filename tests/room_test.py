import unittestimport unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Mr Red", 2.00, True)
        self.customer_2 = Customer("Mr Blue", 3.00, True)
        self.customer_3 = Customer("Mr Pink", 4.00, True)
        self.customers = [self.customer_1, self.customer_2, self.customer_3]
        self.song_1 = Song("Gotta Get")
        self.song_2 = Song("Through")
        self.song_1 = Song("This")
        self.songs = [self.song_1, self.song_2, self.song_3]
        self.room = Room("Happening Room", 100.00, self.drinks)
        
