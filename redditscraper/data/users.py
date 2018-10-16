from redditscraper import config

import requests
from collections import namedtuple
import datetime
import json

USER_AGENT = config["Network"].get("user-agent")
headers = {
    'User-Agent': USER_AGENT,
}
url_frag_1 = "https://www.reddit.com/user/"
url_frag_2 = "/about.json"

User = namedtuple('User',
        [
            'username',
            'account_created_date',
            'comment_karma',
            'link_karma'])

def convert_userresp_to_tuple(user_json):
    data = user_json['data']
    today = datetime.datetime.today()

    ret = User(
            username=data['name'],
            account_created_date=datetime.datetime.fromtimestamp(data['created_utc']),
            comment_karma=data['comment_karma'],
            link_karma=data['link_karma'],)

    return ret


def get_user_by_name(username):
    url = "{}{}{}".format(url_frag_1,username,url_frag_2)
    r = requests.get(url, headers=headers)
    return convert_userresp_to_tuple(json.loads(r.text))


