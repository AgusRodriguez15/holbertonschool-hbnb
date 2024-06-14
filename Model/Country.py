#!/usr/bin/python3
from City import city

class Country(city):
    def __init__(self, id: int, create_at: str, update_at: str, name: str):
        super().__init__(id, create_at, update_at)
        self.name = name
country = Country()