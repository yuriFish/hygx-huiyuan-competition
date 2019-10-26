# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:08:17 2019

@author: alienware
"""

import pandas as pd
import os
import time

""" 外借数据提取 各学科图书种类外借次数统计,不分类读者导出csv """
def extract_borrow(file,schoolname):
    if not os.path.exists('数据分析\\外借数据\\%s'%schoolname):
        os.makedirs('数据分析\\外借数据\\%s'%schoolname)    
    starttime = time.time()
    df = pd.read_csv(file)
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime)) 
    starttime = time.time()
    index={
            'A':'马克思主义、列宁主义、毛泽  东思想、邓小平理论',
            'B':'哲学、宗教',
            'C':'社会科学总论',
            'D':'政治',
            'E':'军事',
            'F':'经济',
            'G':'文化、科学、教育、体育',
            'H':'语言、文字',
            'I':'文学',
            'J':'艺术',
            'K':'历史、地理',
            'N':'自然科学总论',
            'O':'数理科学和化学',
            'P':'天文学、地球科学',
            'Q':'生物科学',
            'R':'医药、卫生',
            'S':'农业科学',
            'T':'工业技术',
            'U':'交通运输',
            'V':'航空、航天',
            'X':'环境科学、安全科学',
            'Z':'综合性图书',
            'C8':'统计学',
            'P2':'测绘学',
            'S9':'水产、渔业',
            'TK':'能源与动力工程',
            'TM':'电工技术',
            'TP':'自动化技术、计算机技术',
            'TP3':'计算技术、计算机技术',
            'TS1':'纺织工业、染整工业',
            'TU':'建筑科学',
            'I0':'文学理论',
            'I1':'世界文学',
            'I2':'中国文学',
            'K2':'中国史',
            'TB3':'工程材料学',
            'H0':'语言学',
            }
    years = [2013, 2014, 2015, 2016, 2017]
#    df_year_item = df[['LOAN_DATE','ITEM_CALLNO']]

    data={
                '索引号':list(index.keys()),
                '类别':list(index.values()),
                }
#    df.dropna(subset=['ISBN'],inplace=True)                                    #数据清洗
    for year in years:
        print(year)
        count=[]
        count0=[]
        year=str(year)
        for key in index:
            print(key)
            if '财经大学' in file:
                temp_item = df[df['LOAN_DATE'].astype(str).str.endswith(year)] #财大年份在最后
                
            else:
                temp_item = df[df['LOAN_DATE'].astype(str).str.startswith(year)]
                    
            temp_item=temp_item[temp_item['ITEM_CALLNO'].astype(str).str.startswith(key)]
#            temp_count = temp_item['ITEM_CALLNO'].str.startswith(key).value_counts()
            temp_count =temp_item.shape[0]
            temp_item_0=temp_item.drop_duplicates(subset=['PATRON_ID'],keep='first')#去重
            temp_count_0 = temp_item_0.shape[0]
#            if len(temp_count)==1:                                             #对应有些学校没有特定种类的书
#                temp_count=0
#   
#            else:
#                temp_count=temp_count[1]
#
#            if len(temp_count_0)==1:                                             #对应有些学校没有特定种类的书
#                temp_count_0=0 
#            else:
#                temp_count_0=temp_count_0[1]           
            count.append(temp_count)
            count0.append(temp_count_0)

        data[year]=count
#        data[year+'本专科生']=count1
#        data[year+'硕博生']=count2
        data[year+'去重']=count0
#        data[year+'去重'+'本专科生']=count3
#        data[year+'去重'+'硕博生']=count4      
    temp_df=pd.DataFrame(data)
    temp_df.to_excel('数据分析\外借数据\%s\%s各学科图书种类外借次数统计(终极版).xlsx'%(schoolname,schoolname),index=False,encoding='utf-8')            
    endtime = time.time()
    dtime = endtime - starttime    
    print("%s各学科图书种类外借次数统计输出完成，用时%.8s s"%(schoolname,dtime)) 
#    
#    for sheet in df.keys():
#            count=[]
#            for key in index:
#                temp_count=df[sheet]['ITEM_CALLNO'].str.startswith(key).value_counts()[1]
#                count.append(temp_count)
#            data={'索引号':list(index.keys()),
#                      '类别':list(index.values()),
#                      '外借数据':count
#                      }
#            temp_df=pd.DataFrame(data)
#            if not os.path.exists('外借数据\%s'%schoolname):
#                os.makedirs('外借数据\%s'%schoolname)
#            temp_df.to_excel('外借数据\%s\%s外借数据.xlsx'%(schoolname,schoolname+sheet),index=False)
#            
#    endtime = time.time()
#    dtime = endtime - starttime    
#    print("%s外借数据输出完成，用时%.8s s"%(schoolname,dtime)) 

""" 到馆数据提取 抽取各学校图书馆入馆数量统计,不分类读者导出csv """
def extract_enter(file,schoolname):
    if not os.path.exists('数据分析\\到馆数据'):
        os.makedirs('数据分析\\到馆数据')    
    starttime = time.time()
    df = pd.read_csv(file)
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime)) 
    starttime = time.time()
    if 'visit_time' in df.keys():                                              #处理数据格式不一致
        df['VISIT_TIME']=df['visit_time']
#    schoollist=[]
    years = [2013, 2014, 2015, 2016, 2017]
#    data={
#                '学校':schoollist,
#                '类别':years,
#                }
    temp_df=pd.DataFrame(index=list(range(1,13)))
    if '财经大学' in file:                                                      #财大年份在最后
#        df['VISIT_TIME']=pd.to_datetime(df['VISIT_TIME'],format='%m/%d/%Y %H:%M:%S')
#        df['VISIT_TIME']=pd.to_datetime(df['VISIT_TIME']).dt.normalize()
#        df['VISIT_TIME'] = pd.to_datetime(df['VISIT_TIME'],infer_datetime_format=True)
#        df['VISIT_TIME']=pd.to_datetime(df['VISIT_TIME'], format = "%m/%d/%Y  %H:%M:%S", errors = 'coerce')
        df['VISIT_TIME'] =df['VISIT_TIME'].astype(str).str.split(' ',expand=True)[0] 
        df['VISIT_TIME']=pd.to_datetime(df['VISIT_TIME'],format='%m/%d/%Y',errors = 'coerce')
        print("财大预处理完毕")    
    for year in years:
        print(year)
        year=str(year)
        temp_item = df[df['VISIT_TIME'].astype(str).str.startswith(year)]
        count=[]
        for month in range(1,13):
            year_month=year+'-'+str(month).zfill(2)
            if '东华大学' in file:
                year_month=year+'/'+str(month).zfill(2)
            if '复旦大学' in file:
                year_month=year+'/'+str(month) 
            temp_count = temp_item['VISIT_TIME'].astype(str).str.startswith(year_month).value_counts()
            if len(temp_count)==1:                                              #有些学校当前月份无入馆
                temp_count=0
            else:
                temp_count=temp_count[1]            
            count.append(temp_count)
        temp_df[year]=count
#    temp_df.loc[schoolname]=count                                             #插行
    temp_df.to_excel('数据分析\到馆数据\%s图书馆入馆数量统计.xlsx'%schoolname,encoding='utf-8')            
    endtime = time.time()
    dtime = endtime - starttime    
    print("%s图书馆入馆数量统计输出完成，用时%.8s s"%(schoolname,dtime)) 
    
""" 到馆数据提取 抽取各学校图书馆入馆数量统计,分类读者导出txt """
def extract_enter_plus(file,schoolname):
    if not os.path.exists('数据分析\\到馆数据'):
        os.makedirs('数据分析\\到馆数据')    
    starttime = time.time()
    df = pd.read_csv(file)
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime)) 
    starttime = time.time()
    if 'visit_time' in df.keys():                                              #处理数据格式不一致
        df['VISIT_TIME']=df['visit_time']
    if 'patron_type' in df.keys():                                              #处理数据格式不一致
        df['PATRON_TYPE']=df['patron_type']
    years = [2013, 2014, 2015, 2016, 2017]

    if '财经大学' in file:                                                      #财大年份在最后
        df['VISIT_TIME'] =df['VISIT_TIME'].astype(str).str.split(' ',expand=True)[0] 
        df['VISIT_TIME']=pd.to_datetime(df['VISIT_TIME'],format='%m/%d/%Y',errors = 'coerce')
        print("财大预处理完毕")    
    f=open('数据分析\到馆数据\%s图书馆入馆数量统计(读者分类).txt'%schoolname,'w+')
    for year in years:
        print(year)
        year=str(year)
        f.write(year+'\n')
        temp_item = df[df['VISIT_TIME'].astype(str).str.startswith(year)]
        for month in range(1,13):
            year_month=year+'-'+str(month).zfill(2)
            if '东华大学' in file:
                year_month=year+'/'+str(month).zfill(2)
            if '复旦大学' in file:
                year_month=year+'/'+str(month) 
            temp_item_0=temp_item[temp_item['VISIT_TIME'].astype(str).str.startswith(year_month)]
            txt=temp_item_0['PATRON_TYPE'].value_counts()
            f.write(year_month+'----------------------\n')
            for i in txt.index:
                f.write(str(i)+':'+str(txt[i])+'\n')

    f.close()       
    endtime = time.time()
    dtime = endtime - starttime    
    print("%s图书馆入馆数量统计输出完成，用时%.8s s"%(schoolname,dtime)) 

""" 外借数据提取 抽取各学校最热门外借文献资源,不分类读者导出txt """
def extract_topbook(file,schoolname):
    if not os.path.exists('数据分析\\外借数据\\%s'%schoolname):
        os.makedirs('数据分析\\外借数据\\%s'%schoolname)     
    starttime = time.time()
    df = pd.read_csv(file)
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime)) 
    starttime = time.time()
    if 'visit_time' in df.keys():                                              #处理数据格式不一致
        df['VISIT_TIME']=df['visit_time']
    if 'title' in df.keys():                                              #处理数据格式不一致
        df['TITLE']=df['title']
    years = [2013, 2014, 2015, 2016, 2017]

 
    f=open('数据分析\外借数据\%s\%s图书馆热门外借文献资源.txt'%(schoolname,schoolname),'w+',encoding='utf-8')
    txt=df['TITLE'].value_counts()[:10]
    f.write('2013~2017最热门外借文献资源:-------------------------------\n')
    for i in txt.index:
        f.write(str(i)+':'+str(txt[i])+'\n')    
    for year in years:
        print(year)
        year=str(year)
        f.write(year+'最热门外借文献资源:-------------------------------\n')
        if '财经大学' in file:
            temp_item = df[df['LOAN_DATE'].astype(str).str.endswith(year)] #财大年份在最后
        else:
            temp_item = df[df['LOAN_DATE'].astype(str).str.startswith(year)]  

        txt=temp_item['TITLE'].value_counts()[:10]
        for i in txt.index:
            f.write(str(i)+':'+str(txt[i])+'\n')

    f.close()       
    endtime = time.time()
    dtime = endtime - starttime    
    print("%s各学校最热门外借文献资源输出完成，用时%.8s s"%(schoolname,dtime))

""" 外借数据提取 各学科图书种类外借次数统计,分类读者导出txt """
def extract_borrow_plus(file,schoolname):
    if not os.path.exists('数据分析\\外借数据\\%s'%schoolname):
        os.makedirs('数据分析\\外借数据\\%s'%schoolname)    
    starttime = time.time()
    df = pd.read_csv(file)
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime)) 
    starttime = time.time()
    index={
            'A':'马克思主义、列宁主义、毛泽  东思想、邓小平理论',
            'B':'哲学、宗教',
            'C':'社会科学总论',
            'D':'政治',
            'E':'军事',
            'F':'经济',
            'G':'文化、科学、教育、体育',
            'H':'语言、文字',
            'I':'文学',
            'J':'艺术',
            'K':'历史、地理',
            'N':'自然科学总论',
            'O':'数理科学和化学',
            'P':'天文学、地球科学',
            'Q':'生物科学',
            'R':'医药、卫生',
            'S':'农业科学',
            'T':'工业技术',
            'U':'交通运输',
            'V':'航空、航天',
            'X':'环境科学、安全科学',
            'Z':'综合性图书',
            'C8':'统计学',
            'P2':'测绘学',
            'S9':'水产、渔业',
            'TK':'能源与动力工程',
            'TM':'电工技术',
            'TP':'自动化技术、计算机技术',
            'TP3':'计算技术、计算机技术',
            'TS1':'纺织工业、染整工业',
            'TU':'建筑科学',
            'I0':'文学理论',
            'I1':'世界文学',
            'I2':'中国文学',
            'K2':'中国史',
            'TB3':'工程材料学',
            'H0':'语言学',
            }
    years = [2013, 2014, 2015, 2016, 2017]
#    df_year_item = df[['LOAN_DATE','ITEM_CALLNO']]

#    data={
#                '索引号':list(index.keys()),
#                '类别':list(index.values()),
#                }
#    df.dropna(subset=['ISBN'],inplace=True)                                    #数据清洗
    f=open('数据分析\外借数据\%s\%s各学科图书种类外借次数统计(读者分类).txt'%(schoolname,schoolname),'w+')
    for year in years:
        print(year)
        year=str(year)
        f.write(year+'\n')
        for key in index:
            print(key)
            f.write(key+'\n')
            if '财经大学' in file:
                temp_item = df[df['LOAN_DATE'].astype(str).str.endswith(year)] #财大年份在最后
                
            else:
                temp_item = df[df['LOAN_DATE'].astype(str).str.startswith(year)]
                    
            temp_item=temp_item[temp_item['ITEM_CALLNO'].astype(str).str.startswith(key)]
            txt=temp_item['PATRON_TYPE'].value_counts()
            f.write('不去重:\n')
            for i in txt.index:
                f.write(str(i)+':'+str(txt[i])+'\n')
            temp_item_0=temp_item.drop_duplicates(subset=['PATRON_ID'],keep='first')#去重
            txt=temp_item_0['PATRON_TYPE'].value_counts()
            f.write('去重:\n')
            for i in txt.index:
                f.write(str(i)+':'+str(txt[i])+'\n')
    f.close()            
    endtime = time.time()
    dtime = endtime - starttime    
    print("%s各学科图书种类外借次数统计输出完成，用时%.8s s"%(schoolname,dtime)) 

""" 外借数据提取 抽取各学校图书外借次数(不分学科),不分类读者导出csv """
def extract_borrow_sum(file,schoolname):
    if not os.path.exists('数据分析\\外借数据\\%s'%schoolname):
        os.makedirs('数据分析\\外借数据\\%s'%schoolname)    
    starttime = time.time()
    df = pd.read_csv(file)
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime)) 
    starttime = time.time()
    years = [2013, 2014, 2015, 2016, 2017]

#    df.dropna(subset=['ISBN'],inplace=True)                                    #数据清洗
    data={}
    for year in years:
        print(year)
        count=[]
        year=str(year)
        if '财经大学' in file:
            temp_item = df[df['LOAN_DATE'].astype(str).str.endswith(year)] #财大年份在最后
                
        else:
            temp_item = df[df['LOAN_DATE'].astype(str).str.startswith(year)]
                    

        temp_count =temp_item.shape[0]
        temp_item_0=temp_item.drop_duplicates(subset=['PATRON_ID'],keep='first')#去重
        temp_count_0 = temp_item_0.shape[0]
      
        count.append(temp_count)
        count.append(temp_count_0)
        data[year]=count

  
    temp_df=pd.DataFrame(data)
    temp_df.index = pd.Series(['总计', '按学生去重'])
    temp_df.to_excel('数据分析\外借数据\%s\%s图书外借次数统计.xlsx'%(schoolname,schoolname),index=True,encoding='utf-8')            
    endtime = time.time()
    dtime = endtime - starttime    
    print("%s图书外借次数统计输出完成，用时%.8s s"%(schoolname,dtime)) 
     
    
if __name__ == "__main__":

        
 
    """ 抽取各学校各学科图书种类外借次数统计,不分类读者导出csv"""
    for root, dirs, files in os.walk(os.path.join(os.getcwd(),"图书外借数据集")):
        for file in files:
                schoolname=file.split('图书外借数据')[0]
                print("正在处理数据集:", root+'\\'+file, ", 来自学校:", schoolname)
                extract_borrow(root+'\\'+file,schoolname)  

    """ 抽取各学校图书外借次数(不分学科),不分类读者导出csv"""
    for root, dirs, files in os.walk(os.path.join(os.getcwd(),"图书外借数据集")):
        for file in files:
                schoolname=file.split('图书外借数据')[0]
                print("正在处理数据集:", root+'\\'+file, ", 来自学校:", schoolname)
                extract_borrow_sum(root+'\\'+file,schoolname)  

    """ 抽取各学校最热门外借文献资源,不分类读者导出txt"""
    for root, dirs, files in os.walk(os.path.join(os.getcwd(),"图书外借数据集")):
        for file in files:
                schoolname=file.split('图书外借数据')[0]
                print("正在处理数据集:", root+'\\'+file, ", 来自学校:", schoolname)
                extract_topbook(root+'\\'+file,schoolname)  
                
    """ 抽取各学校各学科图书种类外借次数统计,分类读者导出txt"""
    for root, dirs, files in os.walk(os.path.join(os.getcwd(),"图书外借数据集")):
        for file in files:
                schoolname=file.split('图书外借数据')[0]
                print("正在处理数据集:", root+'\\'+file, ", 来自学校:", schoolname)
                extract_borrow_plus(root+'\\'+file,schoolname)          
 
    """ 抽取各学校图书馆入馆数量统计,不分类读者导出csv"""
    for root, dirs, files in os.walk(os.path.join(os.getcwd(),"读者入馆数据集")):
        for file in files:
                schoolname=file.split('_')[1].split('.')[0]
                print("正在处理数据集:", root+'\\'+file, ", 来自学校:", schoolname)
                extract_enter(root+'\\'+file,schoolname)         
   
    """ 抽取各学校图书馆入馆数量统计,,分类读者导出txt"""
    for root, dirs, files in os.walk(os.path.join(os.getcwd(),"读者入馆数据集")):
        for file in files:
                schoolname=file.split('_')[1].split('.')[0]
                print("正在处理数据集:", root+'\\'+file, ", 来自学校:", schoolname)
                extract_enter_plus(root+'\\'+file,schoolname)                 
        
        