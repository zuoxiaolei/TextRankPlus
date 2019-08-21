# coding:utf-8
from __future__ import absolute_import
import jieba.posseg as pseg
from pathlib import Path
import re
import six
import synonyms
from . import TR4KW
import numpy as np
import networkx as nx

stopwords_path = Path(__file__).parent.parent / 'data' / 'stopWord.txt'


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


class StringPrepare(object):

    def __init__(self):
        '''
        用分词结果和词性标注结果初始化对象
        '''
        self.pos_filter = {'a', 'j', 'n', 'nr', 'an', 'i', 'Ng',
                           'ns', 'nt', 'nz', 'v', 'vd', 'vn'}

    @classmethod
    def split_sentence(self, text):
        '''
        文本分句
        '''
        return re.split('。|！|\!|\.|？|\?', text)

    def filter_words(self, words, postags):
        '''
        词性过滤
        '''
        return [words[num] for num, ele in enumerate(postags) if ele in self.pos_filter]

    def filter_blank_sentence(self, sentences, filter_all_list):
        '''
        过滤空的句子,如果列表里面的句子全部是空格，去掉这句话，和这句话的分词结果
        '''
        for num, ele in enumerate(sentences):
            if ele.strip() == "":
                del sentences[num]
                del filter_all_list[num]
        return sentences, filter_all_list

    @classmethod
    def load_stop_words(self):
        path = str(stopwords_path)
        if six.PY3:
            with open(path, encoding='utf-8') as fh:
                return set([line.rstrip() for line in fh])
        else:
            with open(path) as fh:
                return set([line.rstrip() for line in fh])

    def filter_stop_words(self, words):
        stop_words = self.load_stop_words()
        return [ele for ele in words if ele not in stop_words]

    def seg_line(self, line):
        '''
        给每一句话的处理
        '''
        line = line.rstrip()  # 去掉每一行的换行符
        words, postags = [], []
        for word, flag in pseg.cut(line):
            words.append(word)
            postags.append(flag)

        words_filter = self.filter_words(words, postags)  # 过滤单词
        rm_stop_word = self.filter_stop_words(words_filter)  # 去掉停用词
        join_word = [ele for ele in rm_stop_word]  # 去掉英文单词
        return join_word

    def words_filter_all(self, text):
        '''
        预处理新闻，分句分词，词性过滤等
        '''
        sentences = self.split_sentence(text)
        result = [self.seg_line(line) for line in sentences if line]
        return result

    def get_similrity(self, word1, word2):
        try:
            v1 = synonyms.v[word1]
            v2 = synonyms.v[word2]
            similar = np.dot(v1, v2) / (np.linalg.norm(v1) * (np.linalg.norm(v2)))
            return similar
        except:
            return synonyms.compare(word1, word2, seg=False)

    def get_sort_keyword(self, raw_text, pagerank_config={'alpha': 0.85, }):
        '''
        获取TextRankplus算法的排序的结果
        Keyword arguments:
        raw_text : 原始获取的网页的文本
        pagerank_config : 设置pagerank参数衰减因子
        '''
        filter_all_list = stringPrepareHandle.words_filter_all(raw_text)  # 过滤原始文本
        sorted_words = TR4KW.sort_words(filter_all_list, filter_all_list,
                                        self.get_similrity, window=2,
                                        pagerank_config=pagerank_config)  # 关键词排序
        return TR4KW.filter_keywords(sorted_words)  # 返回过滤的结果

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


stringPrepareHandle = StringPrepare()

if __name__ == '__main__':
    res = stringPrepareHandle.words_filter_all(
        " 经历移植jinja2到python3的痛苦之后，我把项目暂时放一放，因为我怕打破python3的兼容。我的做法是只用一个python2的代码库，然后在安装的时候用2to3工具翻译成python3。不幸的是哪怕一点点的改动都会打破迭代开发。如果你选对了python的版本，你可以专心做事，幸运的避免了这个问题。")
    print(res)
