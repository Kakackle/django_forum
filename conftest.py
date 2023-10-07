import pytest

# ---------------------------------------------------------------------------- #
#                                   manually                                   #
# ---------------------------------------------------------------------------- #

# from django.contrib.auth.models import User

# @pytest.fixture(scope="session")
# @pytest.fixture
# def test_user(db):
#     user =User.objects.create_user('test', 'test@localhost.com', 'test')
#     return user

# # factory
# @pytest.fixture
# def new_user_factory(db):
#     def create_app_user(
#             username: str,
#             password: str = None,
#             first_name: str = "firstname",
#             last_name: str = "lastname",
#             email: str = "test@test.com",
#             is_staff: bool = False,
#             is_superuser: bool = False,
#             is_active: bool = True,
#     ):
#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name = last_name,
#             email = email,
#             is_staff = is_staff,
#             is_superuser = is_superuser,
#             is_active = is_active,
#         )
#         return user
#     return create_app_user


# ---------------------------------------------------------------------------- #
#                         with factoryboy, class based                         #
# ---------------------------------------------------------------------------- #

from pytest_factoryboy import register
from pytests.factories import UserFactory, TopicFactory, ThreadFactory

register(UserFactory)
register(TopicFactory)
register(ThreadFactory)