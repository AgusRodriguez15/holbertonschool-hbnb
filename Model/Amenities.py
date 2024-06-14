#!/usr/bin/python3
from Primary_Keys import KeyEntities

class Amenities(KeyEntities):
    """Class for Amenities entity"""

    def __init__(self, id: int, create_at: str, update_at: str, name: str, address: str, description: str, num_rooms: int, num_bathrooms: int, price_night: float, max_guests: int):
        """
            Initialize the Amenities class
            Args:
            id (int): Unique identifier for the amenity
            create_at (str): Creation date of the amenity
            update_at (str): Last update date of the amenity
            name (str): Name of the amenity
            address (str): Address of the amenity
            description (str): Description of the amenity
            num_rooms (int): Number of rooms in the amenity
            num_bathrooms (int): Number of bathrooms in the amenity
            price_night (float): Price per night of the amenity
            
        """
        self.name = name
        self.address = address
        self.description = description
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_night = price_night
        self.max_guests = max_guests

amenities = Amenities()