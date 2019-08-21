# -*- coding: utf-8 -*-
from __future__ import absolute_import
import wordcloud
import matplotlib.pyplot as plt
import csv

def load_data(filename):
    '''
    读入csv文件
    '''
    with open(filename) as fh:
        csvwritter = csv.reader(fh)
        result = {}
        for line in csvwritter:
            #print line[0]
            result[line[1].decode('utf8')] = int(float(line[0])*10000)
    return result

data = load_data("./wor2vecKW.csv")
backgroud_Image = plt.imread('girl1.jpg')
wc = wordcloud.WordCloud( background_color = 'white',    # 设置背景颜色
                mask = backgroud_Image,        # 设置背景图片
                max_words = 2000,            # 设置最大现实的字数
                font_path = './msyh.ttf',# 设置字体格式，如不设置显示不了中文
                max_font_size = 200,            # 设置字体最大值
                random_state = 5,            # 设置有多少种随机生成状态，即有多少种配色方案
                )
wc.generate_from_frequencies(data)
image_colors = wordcloud.ImageColorGenerator(backgroud_Image)
wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.savefig("word2vec.png",dpi=800)
plt.show()
