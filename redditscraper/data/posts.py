from collections import namedtuple
import datetime
import re

Post= namedtuple('Post', ['pid', 'title', 'up', 'down', 'domain','created'])


def convert_fullpost_to_list(posts):
    ret = []
    children = posts['data']['children']

    for child in children:
        p = convert_postjson_to_tuple(child)
        ret.append(p)
    return ret


def convert_postjson_to_tuple(post):

    data = post['data']
    ret = Post(
            pid=data['id'],
            title=_clean_title(data['title']),
            up=data['ups'],
            down=data['downs'],
            domain=data['domain'],
            created=datetime.datetime.fromtimestamp(int(data['created_utc'])),)

    return ret


def _clean_title(title):
    return re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,\'\‘\’]", "", title).lower()
