# coding:utf-8
'''
@author: aitech
@email:
'''
from __future__ import absolute_import
from pathlib import Path

stopwords_path = Path(__file__).parent.parent / 'data' / 'stopWord.txt'


def load_stop_words(path=str(stopwords_path)):
    with open(path) as fh:
        return set([line.rstrip() for line in fh])

def filter_words(words):
    stop_words = load_stop_words()
    return [ele for ele in words if ele not in stop_words]
