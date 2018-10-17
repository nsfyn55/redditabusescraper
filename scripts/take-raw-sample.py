import requests
import json
from redditscraper.data import posts
from redditscraper.writer import csvwriter
from redditscraper import config

USER_AGENT = config["Network"].get("user-agent")
DOMAIN = config["Network"].get("domain")

headers = {
    'User-Agent': USER_AGENT,
}
url = DOMAIN

r = requests.get(url, headers=headers)
ps = posts.convert_fullpost_to_list(json.loads(r.text))
csvwriter.write(ps)
