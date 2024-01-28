"""
loading data from the dataset for this project.

methods:
    load_jawiki_country_json: load jawiki-country.json
    unzip_mediawiki: unzip mediawiki data
"""
from pathlib import Path
from typing import Union
import pandas as pd
import polars as pl

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / 'data'


def load_jawiki_country_json(
        data_type: str = 'polars') -> Union[pl.DataFrame, pd.DataFrame]:
    """
    load jawiki-country.json. return as pl.DataFrame.
    If type argument is given as 'pandas', return as pd.DataFrame.
    Returns:
       wiki data: pl.DataFrame or pd.DataFrame
    """
    # validate data_type
    if data_type not in ['polars', 'pandas']:
        raise ValueError(f'''invalid data_type: {data_type}.
                         It must be either "polars" or "pandas''')

    target_path = DATA_DIR / 'jawiki-country.json'
    with open(file=target_path,
              mode='r',
              encoding='utf-8') as f:
        wiki_data = pd.read_json(f, lines=True)

    if data_type == 'polars':
        wiki_data = pl.from_pandas(wiki_data)

    return wiki_data
