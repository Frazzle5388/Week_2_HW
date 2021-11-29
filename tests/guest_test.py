import unittest
from classes.guest import Guest


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Mr Smith")

    def test_guest_has_name(self):
        self.assertEqual("Mr Smith", self.guest.name)