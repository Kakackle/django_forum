import pytest

from django.contrib.auth.models import User
from forum.models import Topic, Thread

# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('test', 'test@localhost.com', 'test')
#     assert User.objects.count() == 1

# @pytest.mark.django_db
# def test_set_check_password(test_user):
#     test_user.set_password("newpassword")
#     assert test_user.check_password("newpassword") is True


# ---------------------------------------------------------------------------- #
#                                   manually                                   #
# ---------------------------------------------------------------------------- #

# @pytest.fixture()
# def new_user(db, new_user_factory):
#     return new_user_factory("testuser", "password", "John Test", is_staff=True)

# def test_create_new_user(new_user):
#     assert new_user.last_name == "lastname"
#     assert new_user.username == "testuser"
#     assert new_user.is_staff == True


# ---------------------------------------------------------------------------- #
#                                with factoryboy                               #
# ---------------------------------------------------------------------------- #

@pytest.mark.django_db
def test_new_user(user_factory):
    # user = user_factory.build()
    user = user_factory.create()
    print(user.username)
    assert User.objects.count() == 1


def test_thread(thread_factory):
    thread = thread_factory.build()
    print(thread.name)
    assert True

@pytest.mark.parametrize(
    "name, description, validity",
    [
        ("Topic 1", "Topic 1 desc", True),
        ("Topic 2", "Topic 2 desc", True),
        # ("", "", False),
    ],
)
def test_topic_instance(
    db, topic_factory, name, description, validity
):
    test = topic_factory(
        name=name,
        description=description
    )

    item = Topic.objects.count()
    assert item == validity

# @pytest.mark.parametrize(
#     "name, topic",
#     [
#         ("Topic 1 thread", 1),
#         ("Topic 2 thread", 2),
#     ],
# )