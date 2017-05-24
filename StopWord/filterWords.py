#coding:utf-8
'''
@author: aitech
@email:
'''
def load_stop_words(path="./StopWord/stopWord.txt"):
    with open(path) as fh:
        return set([line.rstrip() for line in fh])

def filter_words(words):
    stop_words = load_stop_words()
    return [ele for ele in words if ele not in stop_words]

