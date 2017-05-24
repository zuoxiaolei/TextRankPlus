# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:30:14 2017

@author: Administrator
"""
from PosFilter import PosFilter
import StopWord
from pyltp import SentenceSplitter
import pyltp

#载入分词模型和词性标注模型

def load_model():
    segmentor = pyltp.Segmentor()
    segmentor.load("./ltp_data/cws.model")
    postagger = pyltp.Postagger()
    postagger.load("./ltp_data/pos.model")
    return segmentor,postagger

def release_model(segmentor,postagger):
    segmentor.release()
    postagger.release()

def seg_line(line,segmentor,postagger):
        '''
        给每一句话的处理
        '''
        line = line.rstrip() #去掉每一行的换行符
        words = segmentor.segment(line) #分词
        postags = postagger.postag(words) #词性标注
        Pos_Filter = PosFilter(words,postags) #新建一个词性过滤器对指定的词性的单词进行过滤
        words_filter = Pos_Filter.filter_words() #过滤单词
        rm_stop_word = StopWord.filter_words(words_filter) #去掉停用词
        join_word = [ele for ele in rm_stop_word] #去掉英文单词
        #join_word = [ele for ele in join_word if len(ele)>3] #去掉英文单词
        return join_word

def words_filter_all(text,segmentor,postagger):
     '''
     预处理新闻，分句分词，词性过滤等
     '''
     sentences = SentenceSplitter.split(text)
     sentences = list(sentences)
     #print sentences
     result = [seg_line(line,segmentor,postagger) for line in sentences]
     return result

def split_sentences(text):
    return SentenceSplitter.split(text)

def filter_blank_sentence(sentences,filter_all_list):
    '''
    过滤空的句子
    '''
    for num,ele in enumerate(sentences):
        if ele.strip()=="":
            del sentences[num]
            del filter_all_list[num]
    return sentences,filter_all_list




