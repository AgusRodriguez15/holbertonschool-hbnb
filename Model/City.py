#!/usr/bin/python3
from Primary_Keys import KeyEntities

class City(KeyEntities):
    def __init__(self, id: int, create_at: str, update_at: str, longitude: float, latitude: float, name: str, country: str):
        super().__init__(id, create_at, update_at)
        self.longitude = longitude
        self.latitude = latitude
        self.name = name
        self.country = country
city = City ()