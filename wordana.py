import jieba
from wordcloud import WordCloud
import image
import pandas
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
content=[]
x=1
for line in open('ruan.txt','r'):
    if line[0]!="阮" and line[0]!="张" and line[0]!="[" and line[0]!=" " and line[0]!="\n":
        content.append(line)

# for line in open('ruan.txt','r'):
#     if line[0]=="张":
#         x=0
#     elif line[0]=="阮":
#         x=1
#     elif x==0 and line[0]!="[" and line[0]!="张" and line[0]!="阮" and line[0]!=" " and line[0]!="\n" :
#         content.append(line)
#         x=1


text=""
for i in content:
    text=text+i
segs=jieba.cut(text)
segment = []
for seg in segs:
    if len(seg) > 1 and seg!='\r\n' and seg not in ["不是","觉得","就是","还是","没有","一个","自己","但是","然后","所以","已经","不会","这样","这么","时候","现在","好像","知道"]:
        segment.append(seg)
# print(segment)
print(len(segment))
#去停用词
words_df=pandas.DataFrame({'segment':segment})
words_df.head()
#stopwords=pandas.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'])#quoting=3全不引用
#stopwords.head()
#words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
# ancient_chinese_stopwords=pandas.Series([#'的',
#                                          #'其','或','亦','方','于','即','皆',
#                                          #'因','仍','故','尚','呢','了','的','着',
#                                          '" "'])
# words_df=words_df[~words_df.segment.isin(ancient_chinese_stopwords)]

#统计词频
words_stat=words_df.groupby(by=['segment'])['segment'].agg({"number":np.size})
words_stat=words_stat.reset_index().sort_values(by="number",ascending=False)


from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
bimg=imread('tree.jpg')
# bimg=imread('caihong.jpg')
wordcloud=WordCloud(background_color="black",mask=bimg,font_path='msyh.ttf')
wordcloud=wordcloud.fit_words(words_stat.head(39769).itertuples(index=False))
bimgColors=ImageColorGenerator(bimg)
plt.figure(figsize=(20,15))
plt.axis("off")
plt.imshow(wordcloud.recolor(color_func=bimgColors))
plt.show()

#
# import matplotlib
# zhfont1 = matplotlib.font_manager.FontProperties(fname='msyh.ttf')
# # 设置显示中文
# matplotlib.rcParams['font.sans-serif'] = ['msyh'] #指定默认字体
# matplotlib.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
#
# from matplotlib.font_manager import FontProperties
# font = FontProperties(fname=r"msyh.ttc", size=14)
#
# words_stat[:20].plot(y='number', kind='bar')#x='segment', 中文未能正常显示
#
# words_stat[:20].plot(x='segment', y='number', kind='bar')#中文未能正常显示
