#!/usr/bin/python3
from Class_KeyEntities import KeyEntities

class Place(KeyEntities):
    """This class represents a Place entity."""

    def __init__(self, id: int, create_at: str, update_at: str, amenities: list, host: str, city: str, reviews: list):
        """
            Initialize a Place entity.
            Args:
        id (int): The id of the place.
        create_at (str): The creation date of the place.
        update_at (str): The update date of the place.
        amenities (list): The list of amenities of the place.
        host (str): The host of the place.
        city (str): The city of the place.
        reviews (list): The list of reviews of the place.
        """
        super().__init__(id, create_at, update_at)
        self.__amenities = amenities
        self.__host = host
        self.__city = city
        self.__reviews = reviews
        
        place = Place()
        
    
    @property
    def amenities(self):
        return self.__amenities

    @amenities.setter
    def amenities(self, obj):
        self.__amenities = obj
        self.new_date()

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, name):
        self.__host = name
        self.new_date()
            
    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, name):
        self.__city = name
        self.new_date()
    
    @property
    def reviews(self):
        return self.__reviews
    
    @reviews.setter
    def reviews(self, text):
        self.__reviews = text
        self.new_date()