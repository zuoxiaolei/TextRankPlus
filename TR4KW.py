# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:57:15 2017

@author: Administrator
"""
import numpy as np
import networkx as nx
from gensim.models import Word2Vec

def load_model():
    model = Word2Vec.load("./word2vec/wiki_model")
    return model

def release_model(model):
    del model

class AttrDict(dict):
    """构造有属性特征的字典"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

def combine(word_list, window = 2):
    """构造在window下的单词组合，用来构造单词之间的边。

    Keyword arguments:
    word_list  --  list of str, 由单词组成的列表。
    windows    --  int, 窗口大小。
    """
    if window < 2: window = 2
    for x in xrange(1, window):
        if x >= len(word_list):
            break
        word_list2 = word_list[x:]
        res = zip(word_list, word_list2)
        for r in res:
            yield r

def sort_words(vertex_source, edge_source, model, window = 2, pagerank_config = {'alpha': 0.85,}):
    """将单词按关键程度从大到小排序

    Keyword arguments:
    vertex_source   --  二维列表，子列表代表句子，子列表的元素是单词，这些单词用来构造pagerank中的节点
    edge_source     --  二维列表，子列表代表句子，子列表的元素是单词，根据单词位置关系构造pagerank中的边
    window          --  一个句子中相邻的window个单词，两两之间认为有边
    pagerank_config --  pagerank的设置
    """

    #记录词和词的位置信息
    sorted_words   = []
    word_index     = {}
    index_word     = {}
    _vertex_source = vertex_source
    _edge_source   = edge_source
    words_number   = 0
    for word_list in _vertex_source:
        for word in word_list:
            if not word in word_index:
                word_index[word] = words_number
                index_word[words_number] = word
                words_number += 1

    graph = np.zeros((words_number, words_number))

    #图赋权
    for word_list in _edge_source:
        for w1, w2 in combine(word_list, window):
            if w1 in word_index and w2 in word_index:
                index1 = word_index[w1]
                index2 = word_index[w2]
                try:
                    similarity = model.similarity(w1,w2)
                    if similarity<0:
                        similarity = 0
                    print similarity
                except:
                    similarity = 0
                graph[index1][index2] = similarity
                graph[index2][index1] = similarity
#                graph[index1][index2] = 1.0
#                graph[index2][index1] = 1.0

    nx_graph = nx.from_numpy_matrix(graph)

    #添加权重
#    for i in range(words_number):
#         for j in range(i+1,words_number):
#              if graph[i][j]==1.0:
#                   word1 = index_word[i]
#                   word2 = index_word[j]
#                   try:
#                        similarity = model.similarity(word1,word2)
#                   except:
#                        similarity = 1e-5
#                   nx_graph.add_weighted_edges_from([(i,j,similarity),(j,i,similarity)])

    scores = nx.pagerank(nx_graph, max_iter=100,**pagerank_config)          # this is a dict
    sorted_scores = sorted(scores.items(), key = lambda item: item[1], reverse=True)
    for index, score in sorted_scores:
        item = AttrDict(word=index_word[index], weight=score)
        sorted_words.append(item)
    return sorted_words

def filter_keywords(sort_words):
    '''
    去掉一个字个关键词
    '''
    return [ele for ele in sort_words if len(ele.word)>3]

