import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Mr Red")
        self.guest_2 = Guest("Mr Blue")
        self.guest_3 = Guest("Mr Pink")
        self.guests = [self.guest_1, self.guest_2, self.guest_3]
        self.song_1 = Song("Gotta Get")
        self.song_2 = Song("Through")
        self.song_3 = Song("This")
        self.songs = [self.song_1, self.song_2, self.song_3]
        self.room = Room("Happening Room",(),())

    def test_room_has_guests(self):
        self.assertEqual(3, self.room.guest_count())

    def test_room_can_check_in_guests(self):
        guest_4 = Guests("Mr Yellow")
        self.room.add_guest(guest_4)
        self.assertEqual(4, self.room.guest_count())

    def test_room_can_check_out_guests(self):
        self.room.remove_guest()
        self.assertEqual(3, self.room.guest_count())

    

    

    
        
