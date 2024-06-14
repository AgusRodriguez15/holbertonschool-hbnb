#!/usr/bin/python3
from Primary_Keys import KeyEntities

class Users(KeyEntities):
    def __init__(self, id: int, create_at: str, update_at: str, email: str, password: str, first_name: str, last_name: str):
        super().__init__(id, create_at, update_at)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        #user solo puede tener un email 
owner = Users()
reviewer = Users()