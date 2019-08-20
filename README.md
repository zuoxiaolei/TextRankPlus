# TextRankPlus: add more plugins to TextRank algorithm

使用**word2vec**算法计算单词的空间距离进行关键词提取和**单词移动距离(RWMD)算法**进行关键句提取

![Image](https://aip.bdstatic.com/portal/dist/1565867323646/ai_images/secondary/nlp_apply/introduction/6.png)

# 项目的编译
```
pip install -r requirements.txt
```

1. download ltp_data from :http://pan.baidu.com/s/1hsqYX5U
2. put ltp_data into TextRankPlus directory
3. download word2vec model from:http://pan.baidu.com/s/1mhCpm8w
4. put the three file into TextRankPlus/word2vec directory

# 改进的TextRank算法项目的测试
```
python testTextRankPlus4KeySentence.py
python testTextRankPlus4KeyWord.py
```
