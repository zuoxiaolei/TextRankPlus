#coding:utf-8
'''
@author: aitech
@email:
'''
from PosFilter import PosFilter
import StopWord
import pyltp
import multiprocessing
import os

#载入分词模型和词性标注模型
segmentor = pyltp.Segmentor()
segmentor.load("../ltp_data/cws.model")
postagger = pyltp.Postagger()
postagger.load("../ltp_data/pos.model")
#print "load model successful"

def seg_line(line):
        '''
        给每一行的文本分词
        '''
        line = line.rstrip() #去掉每一行的换行符
        words = segmentor.segment(line) #分词
        postags = postagger.postag(words) #词性标注
        Pos_Filter = PosFilter(words,postags) #新建一个词性过滤器对指定的词性的单词进行过滤
        words_filter = Pos_Filter.filter_words() #过滤单词
        rm_stop_word = StopWord.filter_words(words_filter) #去掉停用词
        join_word = [ele for ele in rm_stop_word if not ele.isalpha()]
        join_word = ' '.join(join_word) #用空格连接分词结果
        return join_word

def seg_file(filename):
    '''
    给每一个文件的内容分词
    '''
    with open(filename) as fh:
        seg = '' #记录分词结果
        for line in fh:
            join_word = seg_line(line)
            seg = seg+join_word+"\n" #把分词结果合并并添加换行符
    basename = os.path.basename(filename) #文件名

    #分词结果写入文件
    with open("./word2vec/seg/"+basename,"w") as fh:
        fh.write(seg)

    #打印进度
    fininsh_process = 100*len(os.listdir("seg/"))/float(1001)
    print "finish %{}".format(fininsh_process)


if __name__=="__main__":
    print "makedir seg"
    #创建文件夹
    if not os.path.exists("seg"):
        os.mkdir("seg")

    file_list = ["../split/wiki_data_"+str(num)+".txt" for num in range(1,1002)] #文件列表
    pool = multiprocessing.Pool(processes=8)
    pool.map(seg_file,file_list)
    pool.close()
    pool.join()
    print "finish seg"
