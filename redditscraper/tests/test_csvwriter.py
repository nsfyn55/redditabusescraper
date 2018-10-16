from redditscraper.data import posts, users
from redditscraper.writer import csvwriter

from unittest import mock
import json
import datetime

post_file =  open('redditscraper/tests/data/posts.json', 'r')
post_json = json.loads(post_file.read())

def test_post_writeline():
    """pid,title,up,down,domain,created"""
    with mock.patch('redditscraper.data.posts._get_user_by_name') as user:
        user.return_value =  users.User(
            username="nsfyn55",
            account_created_date=datetime.datetime.fromtimestamp(1326982593),
            comment_karma=10436,
            link_karma=352)
        ps = posts.convert_fullpost_to_list(post_json)

        test_in = ps[0]
        actual = "92ntdm,obama and biden ride again as detectives in the fun mystery hope never dies,0,0,usatoday.com,2018-07-28T13:27:22,nsfyn55,352,10436,2012-01-19T09:16:33"
        expected = csvwriter._convert_post_line(test_in)

        assert actual == expected

