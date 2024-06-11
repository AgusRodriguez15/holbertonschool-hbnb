#!/usr/bin/python3
from Class_KeyEntities import KeyEntities

class Amenities(KeyEntities):
    """This class represents the Amenities entity."""

    def __init__(self, name: str, address: str, description: str, num_rooms: int, num_bathrooms: int, price_night: float, max_guests: int):
        """
            Initializes an Amenities object.
            :param name: The name of the amenity.
            :param address: The address of the amenity.
            :param description: A brief description of the amenity.
            :param num_rooms: The number of rooms in the amenity.
            :param num_bathrooms: The number of bathrooms in the amenity.
            :param price_night: The price per night of the amenity.
            :param max_guests: The maximum number of guests the amenity can accommodate.
            """
        
        self.__name = name
        self.__address = address
        self.__description = description
        self.__num_rooms = num_rooms
        self.__num_bathrooms = num_bathrooms
        self.__price_night = price_night
        self.__max_guests = max_guests

    @property
    def name(self):
        """Getter for the name of the amenity."""
        return self.__name

    @name.setter
    def name(self, val):
        """Setter for the name of the amenity."""
        self.__name = val
        self.new_date()

    @property
    def address(self):
        """Getter for the address of the amenity."""
        return self.__address

    @address.setter
    def address(self, val):
        """Setter for the address of the amenity."""
        self.__address = val
        self.new_date()

    @property
    def description(self):
        """Getter for the description of the amenity."""
        return self.__description

    @description.setter
    def description(self, string):
        """Setter for the description of the amenity."""
        self.__description = string
        self.new_date()

    @property
    def num_rooms(self):
        """Getter for the number of rooms in the amenity."""
        return self.__num_rooms

    @num_rooms.setter
    def num_rooms(self, val):
        """Setter for the number of rooms in the amenity."""
        self.__num_rooms = val
        self.new_date()

    @property
    def num_bathrooms(self):
        """Getter for the number of bathrooms in the amenity."""
        return self.__num_bathrooms

    @num_bathrooms.setter
    def num_bathrooms(self, val):
        """Setter for the number of bathrooms in the amenity."""
        self.__num_bathrooms = val
        self.new_date()

    @property
    def price_night(self):
        """Getter for the price per night of the amenity."""
        return self.__price_night

    @price_night.setter
    def price_night(self, val):
        """Setter for the price per night of the amenity."""
        self.__price_night = val
        self.new_date()

    @property
    def max_guests(self):
        """Getter for the maximum number of guests that can stay in the amenity."""  
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, val):
        """Setter for the maximum number of guests that can stay in the amenity."""
        self.__max_guests = val
        self.new_date()