# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:30:14 2017

@author: Administrator
"""
from __future__ import absolute_import
from .PosFilter import PosFilter
from .filterWords import filter_words
from .Logger import logger
import jieba


def seg_line(line):
    '''
    给每一句话的处理
    '''
    line = line.rstrip()  # 去掉每一行的换行符
    words = jieba.lcut(line)  # 分词
    postags = postagger.postag(words)  # 词性标注
    Pos_Filter = PosFilter(words, postags)  # 新建一个词性过滤器对指定的词性的单词进行过滤
    words_filter = Pos_Filter.filter_words()  # 过滤单词
    rm_stop_word = filter_words(words_filter)  # 去掉停用词
    join_word = [ele for ele in rm_stop_word]  # 去掉英文单词
    # join_word = [ele for ele in join_word if len(ele)>3] #去掉英文单词
    return join_word


def words_filter_all(text, segmentor, postagger):
    '''
    预处理新闻，分句分词，词性过滤等
    '''
    sentences = SentenceSplitter.split(text)
    sentences = list(sentences)
    # print sentences
    result = [seg_line(line, segmentor, postagger) for line in sentences]
    logger.info("finish raw text segmention and pos filter!")
    return result


def filter_blank_sentence(sentences, filter_all_list):
    '''
    过滤空的句子,如果列表里面的句子全部是空格，去掉这句话，和这句话的分词结果
    '''
    for num, ele in enumerate(sentences):
        if ele.strip() == "":
            del sentences[num]
            del filter_all_list[num]
    return sentences, filter_all_list
