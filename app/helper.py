import random
from datetime import datetime


char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


class Helper:
    def __init__(self):
        self.store_room = {}
        # self.store_room.update({"admin": {"room": "admin", "username": "admin"}})

    def room(self, length):
        return "".join(random.choices(char, k=length))

    def get_time(self):
        return datetime.now().strftime("%H:%M")

    def add_rooms(self, username, room, time):
        self.store_room.update({username: {'room': room, 'time': time}})
        return self.store_room

    def view_rooms(self):
        return self.store_room


helper = Helper()
