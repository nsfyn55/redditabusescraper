import requests
import json
from redditscraper.data import posts
from redditscraper.writer import csvwriter
from redditscraper import config

import sys
if sys.version_info[0] > 3.6:
    raise Exception("Must be using Python 3.6")

USER_AGENT = config["Network"].get("user-agent")
DOMAIN = config["Network"].get("domain")

headers = {
    'User-Agent': USER_AGENT,
}
url = DOMAIN

r = requests.get(url, headers=headers)
ps = posts.convert_fullpost_to_list(json.loads(r.text))
csvwriter.write(ps)
