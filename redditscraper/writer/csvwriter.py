from redditscraper import config
import os
import datetime

OUTPUT_DIR=config['Output']['dir']


def write(ps):
    """ write a post list to a csv """

    ls = _convert_post_to_line_list(ps)

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    path = _build_path(OUTPUT_DIR)

    _write(ls, path)


def _write(data, path):
    with open(path, 'w') as f:
        for l in data:
            f.write(l)
            f.write('\n')


def _build_path(directory):
    return OUTPUT_DIR + '/out'+datetime.datetime.now().isoformat()+'.csv'


def _convert_post_to_line_list(ps):
    ret = []

    for p in ps:
        ret.append(_convert_post_line(p))

    return ret


def _convert_post_line(p):
   ret = []

   ret.append(str(p.pid))
   ret.append(str(p.title))
   ret.append(str(p.up))
   ret.append(str(p.down))
   ret.append(str(p.domain))
   ret.append(str(p.created.isoformat()))

   ret.append(str(p.author))
   ret.append(str(p.author_link_karma))
   ret.append(str(p.author_comment_karma))
   ret.append(str(p.author_account_created_date.isoformat()))

   return ",".join(ret)
