#coding:utf-8
'''
@author: Ray
@email:
'''
class PosFilter():
    def __init__(self,words,postags):
        '''
        用分词结果和词性标注结果初始化对象
        '''
        self.words = words
        self.postags = postags
        self.pos_filter = {'a','j','n','nh','ni','ns','nt','nz','v','ws'}

    def filter_words(self):
        return [self.words[num] for num,ele in enumerate(self.postags) if ele in self.pos_filter]

    def filter_pos(self):
        return [ele for ele in self.postags if ele in self.pos_filter]


