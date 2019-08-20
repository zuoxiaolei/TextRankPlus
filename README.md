# TextRankPlus: add more plugins to TextRank algorithm

使用[*word2vec*](https://towardsdatascience.com/introduction-to-word-embedding-and-word2vec-652d0c2060fa)算法计算单词的空间距离进行关键词提取和**单词移动距离**(*RWMD*)算法进行关键句提取,欢迎大家*start*和代码贡献

![NLP](data/text_rank_coin.png)

# python依赖包介绍
[pyltp>=0.1.9.1](https://github.com/HIT-SCIR/ltp)      
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;[哈工大LTP](https://github.com/HIT-SCIR/pyltp) python软件包，用于分词和词性标注  
&#160;[networkx>=1.11](http://networkx.github.io/)  
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;构建单词之间的关系图，计算每个单词的权重  
[gensim>=1.0.1](https://radimrehurek.com/gensim/)   
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;训练word2vec模型  
[numpy>=1.11.3](https://www.numpy.org/)   
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;python矩阵和张量计算  
[pyemd>=0.4.3](https://github.com/wmayner/pyemd)    
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;快速计算单词移动距离  
[python2.7](https://www.python.org/) 或 [python>=3.5](https://www.python.org/)  

## 命令行安装依赖包
```bash
pip install -r requirements.txt
```

# 下载*ltp*分词、词性标注模型和与训练的*word2vec*模型
1. 从百度云下载*ltp_data*模型文件 :&nbsp;&nbsp;http://pan.baidu.com/s/1hsqYX5U  
    下载慢可使用[Pandownloader](https://www.baiduwp.com/)
2. *ltp_data*文件夹放置到TextRankPlus目录
3. 下载word2vec模型文件:&nbsp;&nbsp;http://pan.baidu.com/s/1mhCpm8w
4. 把下载的3个word2vec模型文件放置到 TextRankPlus/word2vec 目录下

# 改进的TextRank算法项目的测试
```
python testTextRankPlus4KeySentence.py
python testTextRankPlus4KeyWord.py
```

# 模型生成的词云
![词云](data/tr.png)

# todo
- 基于bilstm+crf的关键词提取  
- python模块松耦合
