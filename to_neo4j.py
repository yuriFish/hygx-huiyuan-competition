# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 06:17:55 2019

@author: tianchen
"""
import pandas as pd
import numpy as np
import os

def to_neo4j(filelist):
    dfs1=[]
    dfs2=[]
    dfs3=[]
    for file in filelist:
        df = pd.read_csv(file)
        df.replace(r'^\s*$',np.nan,regex=True,inplace=True)                    #将空字符串替换为Na方便后面去除
        df.dropna(subset=['ISBN','PATRON_ID'],inplace=True)
        df.fillna('数据缺失',inplace=True)
        #以下为处理Student节点的代码
        df1=df.copy()
        df1.drop_duplicates(subset=['PATRON_ID'],keep='first',inplace=True)    #学生去重
        PATRON_ID=df1['PATRON_ID']                                             #这里开始三行是改变列PATRON_ID位置
        df1.drop(['PATRON_ID'],axis=1,inplace=True)
        df1.insert(0, 'PATRON_ID', PATRON_ID)
        for feature in df1.keys():
            if feature not in ['PATRON_ID','PATRON_TYPE','PATRON_DEPT','STUDENT_GRADE']:
                df1.drop([feature],axis=1,inplace=True)
        df1.rename(columns={'PATRON_ID':'Student:ID'}, inplace = True)
        schoolname=file.split('图书')[0]
        df1['school']=schoolname
        dfs1.append(df1)
        print('%s学生实体处理完成'%schoolname)
        #以下为处理Book节点的代码
        df2=df.copy()
        df2.drop_duplicates(subset=['ISBN'],keep='first',inplace=True)
        ISBN=df2['ISBN']                                                        #这里开始三行是改变列ISBN位置
        df2.drop(['ISBN'],axis=1,inplace=True)
        df2.insert(0, 'ISBN', ISBN)
        for feature in df2.keys():
            if feature not in ['ISBN','ITEM_CALLNO','PUBLISH_YEAR','AUTHOR','TITLE','PRESS']:
                df2.drop([feature],axis=1,inplace=True)
        df2.rename(columns={'ISBN':'ISBN:ID'}, inplace = True)
        df2['school']=schoolname
        df2.replace(['\n','\r'],'', regex=True,inplace=True)                     #去掉书名里可能有的一些换行符，replace的粒度为单个string，所以要加regex
        dfs2.append(df2)
        print('%s书本实体处理完成'%schoolname)
        #以下为处理借阅关系的代码  
        df3=df.copy()
        ISBN=df3['ISBN']
        df3.drop(['ISBN'],axis=1,inplace=True)
        df3.insert(0, 'ISBN', ISBN)
        PATRON_ID=df3['PATRON_ID']
        df3.drop(['PATRON_ID'],axis=1,inplace=True)
        df3.insert(0, 'PATRON_ID', PATRON_ID)
        for feature in df3.keys():
            if feature not in ['ITEM_ID','SUBLIBRARY','LOAN_DATE','RETURNED_DATE','ISBN','PATRON_ID']:
                df3.drop([feature],axis=1,inplace=True)
        df3.rename(columns={'ISBN':':END_ID','PATRON_ID':':START_ID'}, inplace = True)       
        df3['school']=schoolname
        dfs3.append(df3)
        print('%s借阅关系处理完成'%schoolname)
    #保存到csv文件    
    df_Student = pd.concat(dfs1)
    df_Student.to_csv('to_neo4j\Student.csv',index=False,encoding='utf-8')
    df_Book = pd.concat(dfs2)  
    df_Book.drop_duplicates(subset=['ISBN:ID'],keep='first',inplace=True)
    df_Book.to_csv('to_neo4j\Book.csv',index=False,encoding='utf-8')
    df_Borrow = pd.concat(dfs3)
    df_Borrow.to_csv('to_neo4j\Borrow.csv',index=False,encoding='utf-8')
    df_School=df_Student.copy()
    for feature in df_School.keys():
        if feature not in ['Student:ID','school']:
            df_School.drop([feature],axis=1,inplace=True)
    df_School.rename(columns={'Student:ID':':START_ID','school':':END_ID'}, inplace = True)   
    df_School.to_csv('to_neo4j\School_rel.csv',index=False,encoding='utf-8')
    df_School=df_School.rename(columns={':END_ID':'School:ID'}).drop_duplicates(subset=['School:ID'],keep='first')
    df_School=df_School['School:ID']
    df_School.to_csv('to_neo4j\School_entity.csv',index=False,encoding='utf-8') 
        
if __name__ == "__main__":
    if not os.path.exists('to_neo4j'):
        os.makedirs('to_neo4j') 
    to_neo4j(['10246复旦大学图书外借数据.csv','10247同济大学图书外借数据.csv','10272上海财经大学图书外借数据.csv','10256上海电力大学图书外借数据.csv','10264上海海洋大学图书外借数据.csv'])