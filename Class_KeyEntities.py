#!/usr/bin/python3

from datetime import datetime

class KeyEntities:
    """This class represents the key entities in the system."""

    def __init__(self, id: int, create_at: str, update_at: str):
        """
            Initialize a KeyEntities object.
            :param id: The id of the key entity.
            :param create_at: The creation date of the key entity.
            :param update_at: The last update date of the key entity.
            """
        self.__id = id
        self.__create_at = datetime.now().isoformat()
        self.__update_at = self.__create_at

    @property
    def id(self):
        """Get/set the id of the object"""
        return self.__id

    @id.setter
    def id(self, val):
        pass

    @property
    def create_at(self):
        """Get/set the creation date"""
        return self.__create_at

    @property
    def update_at(self):
        """Get/set the updating date"""
        return self.__update_at
    
    def new_date(self):
        self.__update_at = datetime.now().isoformat
