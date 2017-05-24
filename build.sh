#训练word2vec模型 先解析wiki语料xml成txt然后预处理文本然后训练模型
cd ./word2vec
mkdir seg
python traditional2Simple.py
cd ../
mkdir split
python split_file.py
python seg_wiki_data.py
cd ./word2vec
python train.py #word2vec模型文件在word2vec 的wiki_model

#测试改进的TextRank模型
cd ../
python main.py

