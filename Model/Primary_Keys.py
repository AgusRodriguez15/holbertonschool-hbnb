#!/usr/bin/python3
import uuid
import datetime
"""create all the clses for the AirBnB"""

class KeyEntities:
    """Base class for all entities"""

    def __init__(self, id: int, create_at: str, update_at: str):
        """
        Initialize the base class
        Args:
        id (int): Unique identifier for the entity
        create_at (str): Creation date of the entity
        update_at (str): Last update date of the entity
        """
        self.id = uuid.uuid4()
        self.create_at = create_at if create_at else datetime.now().isoformat()
        self.update_at = update_at if update_at else datetime.now().isoformat()