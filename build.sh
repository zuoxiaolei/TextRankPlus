#download data
mkdir ltp_data
echo "please download ltp_data from :http://pan.baidu.com/s/1hsqYX5U"
echo "please put ltp_data into TextRankPlus directory"
echo "***************"
echo "please download word2vec model from:http://pan.baidu.com/s/1mhCpm8w"
echo "please put the three file into TextRankPlus/word2vec directory"
#测试改进的TextRank模型
python testTextRankPlus4KeySentence.py
python testTextRankPlus4KeyWord.py

