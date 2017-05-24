# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 11:19:17 2016

@author: zuoxiaolei
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:55:48 2016

@author: zuoxiaolei
"""
import logging
import os.path
import sys
import multiprocessing
from gensim.models import Word2Vec

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
         '''
         文件迭代器
         '''
         for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

sentences = MySentences('./seg/') # a memory-friendly iterator

def run():
    '''
    训练模型
    '''
    reload(sys)
    sys.setdefaultencoding('utf8')
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    outp1 = r'wiki_model'
    outp2 = r'vector.txt'
    model = Word2Vec(sentences, size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)

    testData = ['中国','女生','总统','校园']
    for i in testData:
        temp = model.most_similar(i)
        for j in temp:
            print '%f %s'%(j[1],j[0])
        print ''

if __name__=="__main__":
    run()