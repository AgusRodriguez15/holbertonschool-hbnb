#!/usr/bin/python3
from Users import Users

class Reviews(Users):
    def __init__(self, id: int, create_at: str, update_at: str, place_id: int, user_id: int, rating: int, comment: str):
        super().__init__(id, create_at, update_at)
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def write_reviews(self, message):
        print(message)
owner = Reviews ()
Reviewer = Reviews ()