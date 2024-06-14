# test_classes.py

import pytest
from classes import User, Place, Review

@pytest.fixture
def user1():
    return User('test1@example.com', 'password1', 'First1', 'Last1')

@pytest.fixture
def user2():
    return User('test2@example.com', 'password2', 'First2', 'Last2')

def test_unique_email(user1):
    with pytest.raises(ValueError):
        User('test1@example.com', 'password3', 'First3', 'Last3')

def test_update(user1):
    old_updated_at = user1.updated_at
    user1.update()
    assert old_updated_at!= user1.updated_at


@pytest.fixture
def place():
    user = User('test@example.com', 'password', 'First', 'Last')
    return Place('Test Place', 'A nice place.', '123 Test St', 'Test City', 0, 0, user, 2, 1, 100.0, 2, [])

def test_place_creation(place):
    assert place.name == 'Test Place'
    assert place.host == place.user

def test_place_update(place):
    old_updated_at = place.updated_at
    place.update()
    assert old_updated_at!= place.updated_at


@pytest.fixture
def review(place):
    return Review(place, place.user, 5, 'Great place!')

def test_review_creation(review):
    assert review.place == review.place
    assert review.user == review.user

def test_review_update(review):
    old_updated_at = review.updated_at
    review.update()
    assert old_updated_at!= review.updated_at