import pytest
from django.contrib.auth.models import User


@pytest.fixture(scope='function')
def user(db):
    return User.objects.create_user('TestUser', 'user@test.com', 'ThePassword1234')