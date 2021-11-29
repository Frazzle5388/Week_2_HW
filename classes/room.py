class Room:
    def __init__(self, name, guests, songs):
        self.name = name
        self.guests = ()
        self.songs = songs
        
    def guest_count(self):
        return len(self.guests)

    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self):
        return self.guests.pop()