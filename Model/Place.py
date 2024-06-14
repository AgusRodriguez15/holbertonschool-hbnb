#!/usr/bin/python3
from Primary_Keys import KeyEntities

class Place(KeyEntities):
    """Class for Place entity"""

    def __init__(self, id: int, create_at: str, update_at: str, amenities: list, host: str, city: str, reviews: list):
        """
        Initialize the Place class
        Args:
        id (int): Unique identifier for the place
        create_at (str): Creation date of the place
        update_at (str): Last update date of the place
        amenities (list): List of amenities available in the place
        host (str): Host of the place
        city (str): City where the place is located
        reviews (list): List of reviews for the place
        """
        super().__init__(id, create_at, update_at)
        self.amenities = amenities
        self.host = host
        self.city = city
        self.reviews = reviews
        #solo puede tener un host
place = Place()