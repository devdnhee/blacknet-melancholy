"""

"""
import scrapy
import json
import re
import operator

UG_LOOKUP_URL = 'https://www.ultimate-guitar.com/search.php?search_type=title&value='
UG_URL_JOIN = '%20'
UG_SEARCH_REGEX = re.compile("store.page = (\{.*\});")

from ...utils import read_playlist

class UltimateGuitarSpider(scrapy.Spider):
    """

    """
    name = "UltimateGuitar"

    def __init__(self, playlist='posthardcore', *args, **kwargs):
        """

        :param playlist:
        :param args:
        :param kwargs:
        """
        super(UltimateGuitarSpider, self).__init__(*args, **kwargs)
        self.playlist_df = read_playlist(playlist)

    def start_requests(self):

        # create urls and store them in the dataframe
        song_artist_series = self.playlist_df['Song'] + ' ' + self.playlist_df['Artist']
        self.playlist_df['url'] = UG_LOOKUP_URL + song_artist_series.str.replace(' ', '%20')

        for index, row in self.playlist_df.iterrows():
            meta = {
                'Song': row['Song'],
                'Artist': row['Artist'],
                'url': row['url'],
            }
            yield scrapy.Request(url=row['url'], callback=self.parse, meta=meta)

    def parse(self, response):
        xp_info = response.xpath('//body/script[1]/text()').extract_first()
        try:
            d = UG_SEARCH_REGEX.findall(xp_info)[0]
            search_info = json.loads(d)
        except:
            print('Parsing failed for {}'.format(
                response.meta
            ))
            return

        meta = response.meta
        results = search_info.get('data').get('results')

        # sort results on rating, only keep best guitar pro file and yield new request
        sort_on = [(d.get('rating'), d) for d in results if d.get('type') == 'Pro']
        if len(sort_on) > 0:
            best_pro = sorted(sort_on, key=operator.itemgetter(0))[-1]
            meta = {**meta, **(best_pro[1])}
            url = meta['tab_url']

            yield meta

    def parse_tab(self, response):
        with open('test.html', 'wb') as f:
            f.write(response.body)
        print(response.body)
