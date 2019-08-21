#coding:utf-8
'''
@author: aitech
@email:
'''
from __future__ import absolute_import
import os
from easynlp.Logger import logger
def get_file_line_count(filename):
    '''
    统计文件的行数
    '''
    count = 0
    with open(filename) as fh:
        for line in fh:
            count = count+1 #计数增加
    return count

def split_file(filename,file_count):
    '''
    切割文件
    '''
    count = get_file_line_count(filename)
    split_plan = count/file_count #文件的切分行数
    split_num = file_count #文件的切割份数
    if count%file_count!=0:
        split_num = split_num+1 #计算文件的切割份数

    #创建文件
    if not os.path.exists("./split"):
        os.mkdir("./split")

    #开始切割文件
    with open(filename) as fhin:
        count_lines = 0 #文件行数迭代计数
        file_num = 0 #文件创建数量计数
        fhout = open("./split/wiki_data_"+str(file_num+1)+".txt","w") #创建输出文件
        for line in fhin:
            if line.strip()!='':
                fhout.write(line) #把旧的文件写入新的文件
            count_lines = count_lines+1 #文件行数迭代
            if count_lines%split_plan==0: #判断写入文件的行数达到split_plan
                fhout.close()   #关闭输出文件
                logger.info("finish %{}".format(100*file_num/float(split_num)) )#打印完成进度
                if file_num<=split_num: #判断文件的分割份数达到预期
                    file_num = file_num + 1
                    fhout = open("./split/wiki_data_"+str(file_num+1)+".txt","w") #创建输出文件
        fhout.close() #关闭输出文件
        logger.info("finish")

if __name__=="__main__":
    filename = "./word2vec/simple_wiki_data.txt" #得到文件名
    split_file(filename,1000) #文件切割
