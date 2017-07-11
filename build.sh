#训练word2vec模型 先解析wiki语料xml成txt然后预处理文本然后训练模型
mkdir ltp_data
cd ./word2vec
mkdir seg
python seg_wiki_data.py
python train.py #word2vec模型文件在word2vec 的wiki_model

#测试改进的TextRank模型
cd ../
python main.py

