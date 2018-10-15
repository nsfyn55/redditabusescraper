from redditscraper.data import posts
from redditscraper.writer import csvwriter

from unittest import mock
import json
import datetime

post_file =  open('redditscraper/tests/data/posts.json', 'r')
post_json = json.loads(post_file.read())
ps = posts.convert_fullpost_to_list(post_json)

def test_post_writeline():
    """pid,title,up,down,domain,created"""

    test_in = ps[0]
    actual = "92ntdm,obama and biden ride again as detectives in the fun mystery hope never dies,0,0,usatoday.com,2018-07-28T13:27:22"
    expected = csvwriter._convert_post_line(test_in)

    assert actual == expected

