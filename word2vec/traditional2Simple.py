#coding:utf-8
'''
@author: aitech
@email:
'''
import traditional2Simplified
#繁体中文转化为简体中文
fhout = open("simple_wiki_data.txt","w")
fhin = open("wiki_data.txt","r")

[traditional2Simplified.getChineseSimplified.getSimple(line,fhout) for line in fhin]
fhin.close()
fhout.close()