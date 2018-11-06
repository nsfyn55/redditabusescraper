from redditscraper import aggregation
from dateutil import parser
from unittest import mock

def test_file_name_parser():
    name = 'out2018-11-05T21:40:04.997088.csv'

    expected = parser.parse('2018-11-05T21:40:04.997088')
    actual = aggregation._convert_filename_to_date(name)

    assert expected == actual


def test_convert_line_to_datapoint():
    line = '9up310,election day control of congress at stake as voters head to the polls,10,0,washingtonpost.com,2018-11-06T15:08:45,Ruth_Dunavant,7,0,2018-10-30T12:38:13'

    sample_time = parser.parse('2018-11-05T21:40:04.997088')

    expected = aggregation.DataPoint(
        pid='9up310',
        title='election day control of congress at stake as voters head to the polls',
        up=10,
        down=0,
        domain='washingtonpost.com',
        author_link_karma=7,
        author_comment_karma=0,
        author='Ruth_Dunavant',
        author_account_created_date=parser.parse('2018-10-30T12:38:13'),
        created=parser.parse('2018-11-06T15:08:45'),
        sample_time=sample_time)

    actual = aggregation._convert_line_data_point(line, sample_time)

    assert actual == expected

def test_convert_sample_file_to_data_objects():

    name = 'out2018-11-05T21:40:04.997088.csv'
    sample_time = parser.parse('2018-11-05T21:40:04.997088')

    l1 = '9up310,election day control of congress at stake as voters head to the polls,10,0,washingtonpost.com,2018-11-06T15:08:45,Ruth_Dunavant,7,0,2018-10-30T12:38:13'
    l2 = '9up311,election day control of congress at stake as voters head to the polls,10,0,washingtonpost.com,2018-11-06T15:08:45,Ruth_Dunavant,7,0,2018-10-30T12:38:13'
    l3 = '9up312,election day control of congress at stake as voters head to the polls,10,0,washingtonpost.com,2018-11-06T15:08:45,Ruth_Dunavant,7,0,2018-10-30T12:38:13'

    ex1 = aggregation.DataPoint(
        pid='9up310',
        title='election day control of congress at stake as voters head to the polls',
        up=10,
        down=0,
        domain='washingtonpost.com',
        author_link_karma=7,
        author_comment_karma=0,
        author='Ruth_Dunavant',
        author_account_created_date=parser.parse('2018-10-30T12:38:13'),
        created=parser.parse('2018-11-06T15:08:45'),
        sample_time=sample_time)

    ex2 = aggregation.DataPoint(
        pid='9up311',
        title='election day control of congress at stake as voters head to the polls',
        up=10,
        down=0,
        domain='washingtonpost.com',
        author_link_karma=7,
        author_comment_karma=0,
        author='Ruth_Dunavant',
        author_account_created_date=parser.parse('2018-10-30T12:38:13'),
        created=parser.parse('2018-11-06T15:08:45'),
        sample_time=sample_time)

    ex3 = aggregation.DataPoint(
        pid='9up312',
        title='election day control of congress at stake as voters head to the polls',
        up=10,
        down=0,
        domain='washingtonpost.com',
        author_link_karma=7,
        author_comment_karma=0,
        author='Ruth_Dunavant',
        author_account_created_date=parser.parse('2018-10-30T12:38:13'),
        created=parser.parse('2018-11-06T15:08:45'),
        sample_time=sample_time)

    expected = [ex1, ex2, ex3]

    file_mock = mock.MagicMock()
    file_mock.__iter__.return_value = (l1, l2, l3)
    file_mock.name = name

    actual = aggregation._convert_sample_file_to_data_objects(file_mock)

    assert actual == expected

def test_convert_sample_to_data_line():

    sample_time = parser.parse('2018-11-05T21:40:04.997088')

    sample_input = aggregation.DataPoint(
        pid='9up310',
        title='election day control of congress at stake as voters head to the polls',
        up=10,
        down=0,
        domain='washingtonpost.com',
        author_link_karma=7,
        author_comment_karma=0,
        author='Ruth_Dunavant',
        author_account_created_date=parser.parse('2018-10-30T12:38:13'),
        created=parser.parse('2018-11-06T15:08:45'),
        sample_time=sample_time)

    expected = '2018-11-05T21:40:04.997088,9up310,election day control of congress at stake as voters head to the polls,10,0,washingtonpost.com,2018-11-06T15:08:45,Ruth_Dunavant,7,0,2018-10-30T12:38:13'
    actual = aggregation._convert_sample_to_data_line(sample_input)

    assert expected == actual
