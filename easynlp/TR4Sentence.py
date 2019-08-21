# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:02:37 2017

@author: Administrator
"""
from __future__ import absolute_import
import numpy as np
import networkx as nx
from gensim.models import Word2Vec
from pyemd import emd


class AttrDict(dict):
    """构造有属性特征的字典"""

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def get_common_list(list1, list2):
    '''
    获取共同字典
    '''
    return list(set(list1).union(set(list2)))  # 构建两句话的并集


def get_vector(list1, common_list):
    '''
    获取词向量
    '''
    vector = [0] * len(common_list)
    for ele in list1:
        vector[common_list.index(ele)] += 1  # 创建BOW模型
    return vector


def get_similarity(list1, list2, model):
    '''
    构建词袋模型
    '''
    common_list = get_common_list(list1, list2)
    vector1 = get_vector(list1, common_list)
    vector2 = get_vector(list2, common_list)
    distance_matrix = np.zeros((len(common_list), len(common_list)), dtype=np.float64)

    # 计算词和词之间的距离
    for i in range(len(common_list)):
        for j in range(len(common_list)):
            try:
                dist = np.sqrt(np.sum(np.square(model.wv[common_list[i]] - model.wv[common_list[j]])))
            except:
                dist = 100
            distance_matrix[i, j] = dist

    # 计算emd距离
    vector1 = np.array(vector1, dtype=np.float64)
    vector2 = np.array(vector2, dtype=np.float64)
    #    print "run here"
    #    print vector1
    #    print vector2
    #    print distance_matrix
    try:
        result = emd(vector1, vector2, distance_matrix)
    except:
        return 0
    # print result
    return result - 3000


def sort_sentences(sentences, words, model, pagerank_config={'alpha': 0.85, }):
    """将句子按照关键程度从大到小排序

    Keyword arguments:
    sentences         --  列表，元素是句子
    words             --  二维列表，子列表和sentences中的句子对应，子列表由单词组成
    sim_func          --  计算两个句子的相似性，参数是两个由单词组成的列表
    pagerank_config   --  pagerank的设置
    """
    sorted_sentences = []
    _source = words
    sentences_num = len(_source)
    graph = np.zeros((sentences_num, sentences_num))

    for x in range(sentences_num):
        for y in range(x, sentences_num):
            similarity = get_similarity(_source[x], _source[y], model)
            graph[x, y] = similarity
            graph[y, x] = similarity
    nx_graph = nx.from_numpy_matrix(graph)
    scores = nx.pagerank(nx_graph, **pagerank_config)  # this is a dict
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    for index, score in sorted_scores:
        item = AttrDict(index=index, sentence=sentences[index], weight=score)
        sorted_sentences.append(item)

    return sorted_sentences
