from redditscraper.data import users
import datetime
import json
from unittest import mock

user_file =  open('redditscraper/tests/data/user.json', 'r')
user_json = json.loads(user_file.read())


@mock.patch('redditscraper.data.users._convert_created_utc_to_account_age')
def test_convert_user_json(m):

    params = user_json
    m.return_value = datetime.timedelta(2461, 15423, 583541)

    expected = users.User(
            username="nsfyn55",
            account_age=datetime.timedelta(2461, 15423, 583541),
            comment_karma=10436,
            link_karma=352)

    actual = users.convert_userresp_to_tuple(params)

    assert expected == actual


def test_convert_createdutc_to_account_age():

    input_utc = 1326982593
    input_from = datetime.datetime(2018, 10, 15, 13, 33, 36, 583541)
    expected = datetime.timedelta(2461, 15423, 583541)

    actual = users._convert_created_utc_to_account_age(input_from, input_utc)

    assert actual == expected
