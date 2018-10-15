from collections import namedtuple
import datetime

User = namedtuple('User', ['username', 'account_age', 'comment_karma', 'link_karma'], verbose=True)

def convert_userresp_to_tuple(user_json):
    data = user_json['data']
    today = datetime.datetime.today()

    ret = User(
            username=data['name'],
            account_age=_convert_created_utc_to_account_age(today, data['created_utc']),
            comment_karma=data['comment_karma'],
            link_karma=data['link_karma'],)

    return ret

def _convert_created_utc_to_account_age(from_date, created_utc):
    created_dt = datetime.datetime.fromtimestamp(created_utc)
    return from_date - created_dt
