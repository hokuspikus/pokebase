import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_user(user):
    assert user in User.objects.all()
    assert len(User.objects.filter(username="NotAName")) == 0

@pytest.mark.django_db
def test_check_password(user):
    user.set_password('unbelievably_hard_to_crack_password')
    assert user.check_password('unbelievably_hard_to_crack_password') is True

