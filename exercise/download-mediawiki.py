# download mediawiki
# url: https://nlp100.github.io/data/jawiki-country.json.gz
# download to data/jawiki-country.json.gz
# unzip to data/jawiki-country.json

import urllib.request
import gzip
import os


def download_mediawiki() -> None:
    """
    This method is for downloading and saving mediawiki data.
    """
    url = 'https://nlp100.github.io/data/jawiki-country.json.gz'
    savepath = './data/jawiki-country.json.gz'
    if not os.path.exists(savepath):
        print('download mediawiki')
        urllib.request.urlretrieve(url, savepath)
    else:
        print('mediawiki already exists')


def unzip_mediawiki() -> None:
    """
    This method is for unzipping mediawiki data.
    """
    savepath = './data/jawiki-country.json.gz'
    unzippath = './data/jawiki-country.json'
    if not os.path.exists(unzippath):
        print('unzip mediawiki')
        with gzip.open(savepath, 'rb') as f:
            bindata = f.read()
        with open(unzippath, 'wb') as f:
            f.write(bindata)
    else:
        print('mediawiki already unzipped')


if __name__ == '__main__':
    download_mediawiki()
    unzip_mediawiki()
