# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:46:47 2017

@author: Administrator
"""

import filter_all
import TR4Sentence
import csv
raw_text = '''5月12日，保险业学习贯彻习近平总书记关于金融工作重要讲话精神专题培训班在京举行。中国保监会副主席陈文辉就深入贯彻习近平总书记关于金融工作的系列重要讲话精神，进一步强化保险监管，防范保险市场风险，促进行业健康发展，维护国家金融安全做报告。中央纪委驻保监会纪检组组长陈新权，保监会副主席黄洪、梁涛出席。
　　陈文辉指出，习近平总书记关于金融工作的重要论述，特别是在中央政治局第四十次集体学习上的重要讲话，高屋建瓴、思想深刻、内容全面，是以习近平同志为核心的党中央治国理政新理念新思想新战略的重要组成部分，具有重大现实意义和深远历史意义，是全面做好金融工作、切实维护国家金融安全的根本指针和重要遵循。保险业要以高度的政治自觉，深入学习、深化认识、全面领会，将思想和行动高度统一到习近平总书记重要讲话精神上来，站在坚持总体国家安全观的政治高度，深刻认识维护金融安全的极端重要性，全面提升新形势下金融工作的能力。
　　陈文辉指出，要站在维护国家金融安全的高度深刻认识保险业和保险监管面临的形势和要求。要深刻理解中央对金融工作的要求，提高保险工作的政治站位，置身于服务中央治国理政的大逻辑下把握保险工作，站在维护国家安全和金融安全的高度把握保险工作，找准促进经济平稳健康发展的切入点把握保险工作。要围绕加强和巩固党的执政地位、协调推进“四个全面”战略布局、落实中央重大决策部署来统筹推进各项改革，坚持专注保险主业，回归金融服务经济的发展本源，着力发展党和人民需要的金融保险事业，为实体经济发展创造良好金融环境。要深刻把握保险行业面临的困难和挑战，增强做好保险工作的危机感和紧迫感，强化问题导向，加强改进金融监管和风险防控工作，增强风险防范意识，未雨绸缪，坚决治理市场乱象，切实守住风险底线，有效化解和平稳处置一批风险点。要深刻认识保险监管工作存在的不足，增强做好保险监管工作的责任感和使命感，不断加强监管制度建设，及时弥补监管短板，着力提升监管水平，强化监管工作力度，深入推进反腐倡廉工作，重构行业风清气正的政治生态。
　　陈文辉强调，学习贯彻习近平总书记关于金融工作的重要讲话精神，必须坚持“两手抓，两手硬”。在政治上，就是要继续深化“两学一做”学习教育，自觉用习近平总书记治国理政思想和关于金融工作重要讲话精神武装头脑、指导实践。在业务上，就是要按照习近平总书记关于做好金融工作的要求，围绕“金融活，经济活；金融稳，经济稳”总体方针，抓好近期保监会“1+4”系列文件的落实。下一步，保险监管系统要切实坚持“保险业姓保、保监会姓监”，全力抓好系列文件的落实，坚决守住不发生系统性风险底线，整治保险市场乱象，补齐监管和行业短板，更好地支持实体经济，筑牢保险业稳定健康发展的根基。同时，要着眼全局，加强监管统筹和协调，把握监管力度和节奏，细化落实措施，充分评估监管政策效果，加强对市场形势的研判和应对，同步做好政策解读，稳定市场预期，稳妥推进相关工作。'''
model = TR4Sentence.load_model()
segmentor,postagger = filter_all.load_model()

sentences = filter_all.split_sentences(raw_text) #分句列表
filter_all_list = filter_all.words_filter_all(raw_text,segmentor,postagger) #分词二级列表
sentences = list(sentences) #句子划分
sentences,filter_all_list = filter_all.filter_blank_sentence(sentences,filter_all_list)

with open ("sentences.txt","w") as fh:
    fh.write('\n'.join(sentences))

sorted_sentences = TR4Sentence.sort_sentences(sentences, filter_all_list, model) #摘要提取

#释放内存
TR4Sentence.release_model(model)
filter_all.release_model(segmentor,postagger)

# 结果保存到文件
with open("sentence_sort_wmd.csv","wb") as fh:
    csvwritter = csv.writer(fh)
    for ele in sorted_sentences:
        csvwritter.writerow((ele.sentence,ele.weight,ele.index))

#经典TextRank算法
import numpy as np
import networkx as nx
import math
class AttrDict(dict):
    """构造有属性特征的字典"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

def get_similarity(word_list1, word_list2):
    """默认的用于计算两个句子相似度的函数。

    Keyword arguments:
    word_list1, word_list2  --  分别代表两个句子，都是由单词组成的列表
    """
    words   = list(set(word_list1 + word_list2))
    vector1 = [float(word_list1.count(word)) for word in words]
    vector2 = [float(word_list2.count(word)) for word in words]

    vector3 = [vector1[x]*vector2[x]  for x in xrange(len(vector1))]
    vector4 = [1 for num in vector3 if num > 0.]
    co_occur_num = sum(vector4)

    if abs(co_occur_num) <= 1e-12:
        return 0.

    denominator = math.log(float(len(word_list1))) + math.log(float(len(word_list2))) # 分母

    if abs(denominator) < 1e-12:
        return 0.

    return co_occur_num / denominator

def sort_sentences(sentences, words, sim_func = get_similarity, pagerank_config = {'alpha': 0.85,}):
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

    for x in xrange(sentences_num):
        for y in xrange(x, sentences_num):
            similarity = sim_func( _source[x], _source[y] )
            graph[x, y] = similarity
            graph[y, x] = similarity

    nx_graph = nx.from_numpy_matrix(graph)
    scores = nx.pagerank(nx_graph, **pagerank_config)              # this is a dict
    sorted_scores = sorted(scores.items(), key = lambda item: item[1], reverse=True)

    for index, score in sorted_scores:
        item = AttrDict(index=index, sentence=sentences[index], weight=score)
        sorted_sentences.append(item)

    return sorted_sentences

others_sort_sentences = sort_sentences(sentences, filter_all_list)

# 结果保存到文件
with open("sentence_sort_tr.csv","wb") as fh:
    csvwritter = csv.writer(fh)
    for ele in others_sort_sentences:
        csvwritter.writerow((ele.sentence,ele.weight,ele.index))
##打印结果
#for ele in sorted_sentences:
#    print "{} {}".encode('gbk').format(ele.word,ele.score)