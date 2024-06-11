#!/usr/bin/python3
from Class_KeyEntities import KeyEntities

class Reviews(KeyEntities):
    """This class represents the Reviews table in the database."""
    
    def __init__(self, id: int, create_at: str, update_at: str, place_id: int, user_id: int, rating: int, comment: str):
        """Initializes a Review object."""
        super().__init__(id, create_at, update_at)
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        
    def write_review(self, write_REVIEW):
        """Writes the review to the database."""
        print(write_REVIEW)
    
Review = Reviews()

Review.write_review("Er is een poep")