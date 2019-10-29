# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:15:05 2019

@author: alienware
"""
import re
import pandas as pd
import os
import time
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from operator import itemgetter


def get_book_num(file, schoolname):
    
    starttime = time.time()
    df = pd.read_csv(file)
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime)) 
    
    df_title = df['TITLE']
    df_title.to_csv('df_%s_title.txt' % schoolname, sep='\n', index=False)
    print("提取%s数据集完成" % schoolname)
    
    
def get_word_cloud(schoolname):
#    schoolname = '10270上海师范大学'
    book_name = 'df_' + schoolname + '_title.txt'
    print("正在提取%s的词云数据" % schoolname)
    
    book = {}
    with open(book_name,'r', encoding='utf-8') as f:
        for name in f:
            name = name.replace('\n', '')
            if name not in book:
                book[name] = 1
            else:
                book[name] += 1
    print('数据提取完毕')
    book_order = sorted(book.items(),key=itemgetter(1),reverse=True)[:150] # 提取排名前150做词云
    book_dict = dict(book_order)
    
    image= Image.open('./book.jpg')
    graph = np.array(image)
    wordcloud = WordCloud(
    # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
    font_path="C:/Windows/Fonts/simhei.ttf",
    background_color="white",
    # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
    mask=graph,
    max_words=150, # 最多显示词数
    max_font_size=100 # 字体最大值
    )
    wordcloud.generate_from_frequencies(book_dict)  # 根据给定词频生成词云
    print('词云处理完毕')
    image_colors = ImageColorGenerator(graph)
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wordcloud.to_file('%s_wordcloud.jpg' % schoolname)
    
    
if __name__ == "__main__":
    os.chdir("D:\\study\\program\\python\\workspace\\hygx")
    
    """ 词云 - 阅读书籍统计 """
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if "图书外借数据" in file:
                schoolname=file.split('图书')[0]
                print((root+'\\'+file,schoolname))
                get_book_num(root+'\\'+file, schoolname)
                get_word_cloud(schoolname)
    
    
