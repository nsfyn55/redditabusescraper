from collections import namedtuple
from redditscraper.data import users
import datetime
import re

Post= namedtuple('Post', [
    'pid',
    'title',
    'up',
    'down',
    'domain',
    'author_link_karma',
    'author_comment_karma',
    'author',
    'author_account_created_date',
    'created'])


def convert_fullpost_to_list(posts):
    ret = []
    children = posts['data']['children']

    for child in children:
        p = convert_postjson_to_tuple(child)
        ret.append(p)
    return ret


def convert_postjson_to_tuple(post):

    data = post['data']
    author = _get_user_by_name(data['author'])
    
    title = _clean_title(data['title'])
    ret = Post(
            pid=data['id'],
            title=_clean_title(data['title']),
            up=data['ups'],
            down=data['downs'],
            domain=data['domain'],
            author_link_karma=author.link_karma,
            author_comment_karma=author.comment_karma,
            author=author.username,
            author_account_created_date=author.account_created_date,
            created=datetime.datetime.fromtimestamp(int(data['created_utc'])),)

    return ret


def _get_user_by_name(username):
    return users.get_user_by_name(username)

def _clean_title(title):
    return re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,\'\‘\’]", "", title).lower()
