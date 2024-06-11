#!/usr/bin/python3
from Class_KeyEntities import KeyEntities

class City(KeyEntities):
    """This class represents a City entity."""
    def __init__(self, id: int, create_at: str, update_at: str, longitude: float, latitude: float, name: str, country: str):
        super().__init__(id, create_at, update_at)
        self.__longitude = longitude
        self.__latitude = latitude
        self.__name = name
        self.__country = country

    @property
    def longitude(self):
        return self.__longitude
        
    @longitude.setter
    def longitude(self, longitude):
        self.__longitude = longitude
        self.new_date()

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        self.__latitude = latitude
        self.new_date()

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        self.new_date()
    
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, country):
        self.__country = country
        self.new_date()
    
city = City()