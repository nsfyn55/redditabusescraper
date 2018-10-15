from redditscraper.data import posts

from unittest import mock
import json
import datetime

post_file =  open('redditscraper/tests/data/posts.json', 'r')
post_json = json.loads(post_file.read())

single_post = post_json['data']['children'][0]


def test_clean_title():
    raw_title = "Obama and Biden ride again (as detectives!) in the fun mystery, 'Hope Never Dies'"
    expected = 'Obama and Biden ride again as detectives in the fun mystery Hope Never Dies'

    actual = posts._clean_title(raw_title)

    assert actual == expected


@mock.patch('redditscraper.data.posts._clean_title')
def test_convert_post(m):

    m.return_value = "clean title"

    expected = posts.Post(
            title="clean title",
            up=0,
            down=0,
            domain='usatoday.com',
            created=datetime.datetime(2018, 7, 28, 13, 27, 22))

    actual = posts.convert_postjson_to_tuple(single_post)

    assert expected == actual


@mock.patch('redditscraper.data.posts._clean_title')
def test_convert_posts(m):

    m.return_value = "clean title"

    expected1 = posts.Post(
            title="clean title",
            up=0,
            down=0,
            domain='usatoday.com',
            created=datetime.datetime(2018, 7, 28, 13, 27, 22))

    expected2 = posts.Post(
            title="clean title",
            up=1,
            down=0,
            domain='apnews.com',
            created=datetime.datetime(2018, 7, 28, 13, 27, 19))

    actual = posts.convert_fullpost_to_list(post_json)
    expected = [expected1, expected2]

    assert expected == actual
