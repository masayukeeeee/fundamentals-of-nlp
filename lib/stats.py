"""
This module is for statistics of words.

classes:
    Ranking: This class is for ranking of words.
"""
from dataclasses import dataclass
import polars as pl


@dataclass
class Ranking:
    """
    This dataclass is essentially a polars DataFrame.
    The dataframe has 3 columns: word, type, count.
    args:
        None
    """
    def __post_init__(self):
        self.words = pl.DataFrame(schema={
            'word': str,
            'type': str,
            'count': int
        })

    def isin(self, word: str, word_type: str) -> bool:
        """
        check if word is in words set
        args:
            word (Word): word class
        return:
            bool: True if word is in words set
        """
        return self.words.filter(
            pl.col('word') == word and pl.col('type') == word_type
        ).shape[0] > 0

    def add_word(self,
                 word: str,
                 word_type: str) -> None:
        """
        add word to words dataframe
        Args:
            type (str): word type (noun, verb, etc.)
            word (str): word(spell)
        """
        if not self.isin(word, word_type):
            new_record = pl.DataFrame({
                'word': [word],
                'type': [word_type],
                'count': [1]
            })
            self.words = pl.concat([self.words, new_record], how='vertical')
        else:
            print(f'{word.word} is already in words set')

    def add_count(self,
                  word: str,
                  word_type: str) -> None:
        """
        increment count of a word

        args:
            word (str): target word to increment count
        """
        if self.isin(word, word_type):
            # increment count
            self.words.filter(
                pl.col('word') == word and pl.col('type') == word_type
            ).with_columns(
                pl.col('count') + 1
            )
        else:
            # if word is not in words set, add word to words set
            self.add_word(word, word_type)

    def show_ranking_all(self, n: int):
        """
        show ranking of word frequency.

        args:
            n (int): How many words to show
        """
        ranking = self.words.sort(by_column='count', reverse=True).head(n)
        return ranking

    def show_ranking_type(
            self, n: int,
            word_type: str) -> pl.DataFrame:
        """
        show ranking of word frequency.

        args:
            n (int): How many words to show
        """
        ranking = self.words.filter(
            pl.col('type') == word_type
            ).sort(
                by_column='count', reverse=True
            ).head(n)
        return ranking
