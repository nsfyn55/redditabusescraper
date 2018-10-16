from redditscraper.data import users
import datetime
import json
from unittest import mock

user_file =  open('redditscraper/tests/data/user.json', 'r')
user_json = json.loads(user_file.read())


def test_convert_user_json():

    params = user_json

    expected = users.User(
            username="nsfyn55",
            account_created_date=datetime.datetime.fromtimestamp(1326982593),
            comment_karma=10436,
            link_karma=352)

    actual = users.convert_userresp_to_tuple(params)

    assert expected == actual

