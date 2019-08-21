# -*- coding: utf-8 -*-
from __future__ import absolute_import
import csv
from . import filter_all
from . import TR4Sentence
from .Logger import logger

def get_sort_sentences(raw_text):
    '''
    获取TextRankplus算法的排序的结果
    Keyword arguments:
    raw_text : 原始获取的网页的文本
    window : 单词共现窗口
    pagerank_config : 设置pagerank参数衰减因子
    '''
    word2vec_model, segmentor, postagger = load_model()  # 载入模型
    sentences = filter_all.split_sentences(raw_text)  # 分句列表
    filter_all_list = filter_all.words_filter_all(raw_text, segmentor, postagger)  # 分词二级列表
    sentences = list(sentences)  # 转化为list类型
    sentences, filter_all_list = filter_all.filter_blank_sentence(sentences, filter_all_list)
    return TR4Sentence.sort_sentences(sentences, filter_all_list, word2vec_model)


def keyword_to_csv_file(filename, sorted_words):
    '''
    结果写入到已存在或者不存在的csv文件中
    Keyword arguments :
        filename : 文件路径和文件名
        sorted_words ： TextRankPlus获取的结果
    '''
    with open(filename, "wb") as fh:
        csvwritter = csv.writer(fh)
        for ele in sorted_words:
            csvwritter.writerow((str(ele.weight), ele.sentence))
    logger.info("write result to csv file!")
