from redditscraper.data import posts, users

from unittest import mock
import json
import datetime

post_file =  open('redditscraper/tests/data/posts.json', 'r')
post_json = json.loads(post_file.read())

single_post = post_json['data']['children'][0]


def test_clean_title():
    raw_title = "Obama and Biden ride again (as detectives!) in the fun mystery, 'Hope Never Dies'"
    expected = 'obama and biden ride again as detectives in the fun mystery hope never dies'

    actual = posts._clean_title(raw_title)

def test_clean_title_single_tick():
    raw_title = "trump says ‘rogue killers’ may be involved in saudi journalist case"
    expected = 'trump says rogue killers may be involved in saudi journalist case'

    actual = posts._clean_title(raw_title)

    assert actual == expected


def test_convert_post():

    with mock.patch('redditscraper.data.posts._clean_title') as m:
       with mock.patch('redditscraper.data.posts._get_user_by_name') as user:

            user.return_value =  users.User(
                username="nsfyn55",
                account_created_date=datetime.datetime.fromtimestamp(1326982593),
                comment_karma=10436,
                link_karma=352)

            m.return_value = "clean title"

            expected = posts.Post(
                    pid="92ntdm",
                    title="clean title",
                    up=0,
                    down=0,
                    domain='usatoday.com',
                    author_link_karma=352,
                    author_comment_karma=10436,
                    author='nsfyn55',
                    author_account_created_date=datetime.datetime.fromtimestamp(1326982593),
                    created=datetime.datetime(2018, 7, 28, 13, 27, 22))

            actual = posts.convert_postjson_to_tuple(single_post)

            assert expected == actual


def test_convert_posts():

    with mock.patch('redditscraper.data.posts._clean_title') as m:
        with mock.patch('redditscraper.data.posts._get_user_by_name') as user:

            user.return_value =  users.User(
                username="nsfyn55",
                account_created_date=datetime.datetime.fromtimestamp(1326982593),
                comment_karma=10436,
                link_karma=352)

            m.return_value = "clean title"

            expected1 = posts.Post(
                    pid="92ntdm",
                    title="clean title",
                    up=0,
                    down=0,
                    domain='usatoday.com',
                    author='nsfyn55',
                    author_link_karma=352,
                    author_comment_karma=10436,
                    author_account_created_date=datetime.datetime.fromtimestamp(1326982593),
                    created=datetime.datetime(2018, 7, 28, 13, 27, 22))

            expected2 = posts.Post(
                    pid="92ntd1",
                    title="clean title",
                    up=1,
                    down=0,
                    domain='apnews.com',
                    author='nsfyn55',
                    author_link_karma=352,
                    author_comment_karma=10436,
                    author_account_created_date=datetime.datetime.fromtimestamp(1326982593),
                    created=datetime.datetime(2018, 7, 28, 13, 27, 19))

            actual = posts.convert_fullpost_to_list(post_json)
            expected = [expected1, expected2]

            assert expected == actual
