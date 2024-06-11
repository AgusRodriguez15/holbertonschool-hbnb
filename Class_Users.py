#!/usr/bin/python3
from Class_KeyEntities import KeyEntities

class EmailAlreadyExistError(Exception):
    pass

class Users(KeyEntities):
    """This class represents the Users table in the database"""

    def __init__(self, id: int, create_at: str, update_at: str, email: str, password: str, first_name: str, last_name: str):
        """
            Initialize a User object
            :param id: The user's id
            :param create_at: The date and time the user was created
            :param update_at: The date and time the user was last updated
            :param email: The user's email
            :param password: The user's password
            :param first_name: The user's first name
            :param last_name: The user's last name
            """
        super().__init__(id, create_at, update_at)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def create_review(self, message_review):
            print(message_review)

owner = Users()
reviwer = Users()

owner.create_review("Review of the owner")
reviwer.create_review("Review of the owner")

def register_user(email):
    """
    Register a new user
    :param email: The user's email
    :return: A new User object
    """
    if not email:  # Check if email is not empty
        raise ValueError("Email cannot be empty")
    else:
        if email in ["existing@example.com"]:
            raise EmailAlreadyExistError(f"The email {email} already exists")
        else:
            print(f"User {email} has been registered succesfully")

try:
    register_user("user1example@gmail.com")
except EmailAlreadyExistError as e:
    print(e)
except ValueError as e:
    print(e)