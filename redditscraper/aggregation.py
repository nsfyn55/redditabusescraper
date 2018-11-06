from collections import namedtuple
from dateutil import parser
from redditscraper import config

import datetime
import pathlib
import re

pattern = re.compile('out([0-9].*).csv')

DataPoint= namedtuple('DataPoint', [
    'pid',
    'title',
    'up',
    'down',
    'domain',
    'author_link_karma',
    'author_comment_karma',
    'author',
    'author_account_created_date',
    'created',
    'sample_time'])

process_path_dir = pathlib.Path(config['Data']['process-data-dir'])
aggregate_path_dir = pathlib.Path(config['Data']['aggregate-data-dir'])


def process_files():
    aggregate_file_path = aggregate_path_dir.joinpath(_build_output_file_name())
    with aggregate_file_path.open("a+") as aggregate_file:
        for pth in process_path_dir.iterdir():
            with pth.open('r') as data_file:
                samples = _convert_sample_file_to_data_objects(data_file)

                for sample in samples:
                    line = _convert_sample_to_data_line(sample)
                    aggregate_file.write(line + "\n")


#-------------------------
# UTILITY
#-------------------------
def _convert_line_data_point(line, sample_time):

    (pid, title, up, down, domain, created_date, author, author_link_karma,
            author_comment_karma, author_account_created_date) = line.split(',')

    ret = DataPoint(
        pid=pid,
        title=title,
        up=int(up),
        down=int(down),
        domain=domain,
        author_link_karma=int(author_link_karma),
        author_comment_karma=int(author_comment_karma),
        author=author,
        author_account_created_date=parser.parse(author_account_created_date),
        created=parser.parse(created_date),
        sample_time=sample_time)

    return ret


def _convert_sample_file_to_data_objects(sample_file):

    name = _extract_file_name(sample_file)
    sample_time = _convert_filename_to_date(name)

    ret = []

    for line in sample_file:
        ret.append(_convert_line_data_point(line, sample_time))

    return ret


def _convert_filename_to_date(name):
    match = pattern.match(name)
    return parser.parse(match.group(1))


def _extract_file_name(f):
    return pathlib.Path(f.name).name


def _build_output_file_name():
    return 'aggregate-'+datetime.datetime.now().isoformat()+'-.csv'


def _convert_sample_to_data_line(sample):
   ret = []

   ret.append(str(sample.sample_time.isoformat()))
   ret.append(str(sample.pid))
   ret.append(str(sample.title))
   ret.append(str(sample.up))
   ret.append(str(sample.down))
   ret.append(str(sample.domain))
   ret.append(str(sample.created.isoformat()))

   ret.append(str(sample.author))
   ret.append(str(sample.author_link_karma))
   ret.append(str(sample.author_comment_karma))
   ret.append(str(sample.author_account_created_date.isoformat()))

   return ",".join(ret)
