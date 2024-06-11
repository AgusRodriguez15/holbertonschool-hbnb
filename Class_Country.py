#!/usr/bin/python3
from Class_City import City

class Country(City):
    """This class represents a Country."""
    def __init__(self, id: int, create_at: str, update_at: str, name: str):
        super().__init__(id, create_at, update_at)
        self.name = name