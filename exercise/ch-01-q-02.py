# use data at data/jawiki-country.json 
# language: Japanese
# try morphological analysis with mecab
# make frequency n-ranking table of all words and nouns

import MeCab
import polars as pl
from lib.dataloader import load_jawiki_country_json
from lib.stats import Ranking


def main():
    """
    main function
    """
    raw_data = load_jawiki_country_json()  # load data
    ranking = Ranking()  # stats class
    mecab = MeCab.Tagger()  # morphological analyser

    return raw_data, ranking, mecab


if __name__ == '__main__':
    d, r, m = main()
    import ipdb; ipdb.set_trace()
    print('finished')
