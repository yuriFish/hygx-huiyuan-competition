# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:08:17 2019

@author: alienware
"""

import pandas as pd
import os
import time


""" 处理图书外借数据，从excel转换成csv """
def borrow2csv(file, schoolname):
    starttime = time.time()
    df = pd.read_excel(file, sheet_name=None, dtype=str, encoding='utf-8')
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime))
    
    starttime = time.time()
    if not os.path.exists('图书外借数据集'):
        os.makedirs('图书外借数据集')    
    for sheet in df.keys():
        df_sheet = df[sheet]
        del df_sheet['AUTHOR']
        df_sheet.to_csv('图书外借数据集\%s图书外借数据.csv'%(schoolname),index=False,encoding='utf-8',mode='a')        
    endtime = time.time()
    dtime = endtime - starttime    
    print("%s图书外借数据输出完成，用时%.8s s"%(schoolname,dtime))
    
    
""" 处理图书预约数据，从excel转换成csv """
def order2csv(file, schoolname):
    starttime = time.time()
    df = pd.read_excel(file, sheet_name=None, dtype=str, encoding='utf-8')
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime))
    
    starttime = time.time()
    for sheet in df.keys():
        df_sheet = df[sheet]
        if not os.path.exists('图书预约数据集'):
            os.makedirs('图书预约数据集')
        df_sheet.to_csv('图书预约数据集\%s图书预约数据.csv'%(schoolname),index=False,encoding='utf-8')
        
    endtime = time.time()
    dtime = endtime - starttime    
    print("%s图书预约数据输出完成，用时%.8s s"%(schoolname,dtime))
    
    
""" 处理图书入馆数据，从excel转换成csv, 只有上海电力大学是xlsx文件 """
def nyukan2csv(file, schoolname):
    starttime = time.time()
    df = pd.read_excel(file, sheet_name=None, dtype=str, encoding='utf-8')
    endtime = time.time()
    dtime = endtime - starttime
    print("读取%s数据集完成，用时%.8s s" % (schoolname,dtime))
    
    starttime = time.time()
    if not os.path.exists('读者入馆数据集'):
        os.makedirs('读者入馆数据集')
    for sheet in df.keys():
        df_sheet = df[sheet]
        df_sheet.to_csv('读者入馆数据集\\3读者入馆数据_%s.csv'%(schoolname),index=False,encoding='utf-8',mode='a')        
    endtime = time.time()
    dtime = endtime - starttime    
    print("%s读者入馆数据输出完成，用时%.8s s"%(schoolname,dtime))


if __name__ == "__main__":
#    os.chdir("D:\study\program\\bigdata\competition\惠源共享\dataset\library")
    
    """ 测试单例 """
#    file = "D:\\study\\program\\bigdata\\competition\\惠源共享\\dataset\\library\\10246复旦大学图书馆业务数据集\\1图书外借数据_复旦大学.xlsx"
#    file_csv = "D:\\study\\program\\bigdata\\competition\\惠源共享\\dataset\\library\\extract_test\\复旦大学\\复旦大学2013年dataset.csv"
#    schoolname = "复旦大学"
#    excel2csv(file, schoolname)
    
    """ 处理图书外借数据，从excel转换成csv """
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if "1图书外借数据" in file and "xlsx" in file:
                schoolname=root.split('\\')[-1].split('图书馆')[0]  
                print("正在处理数据集:", root+'\\'+file, ", 来自学校:", schoolname)
                borrow2csv(root+'\\'+file, schoolname)
    
    """ 处理图书预约数据，从excel转换成csv """
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if "2图书预约数据" in file and "xlsx" in file:
                schoolname=root.split('\\')[-1].split('图书馆')[0]  
                print("正在处理数据集:", root+'\\'+file, ", 来自学校:", schoolname)
                order2csv(root+'\\'+file, schoolname)
                
    """ 处理图书入馆数据，从excel转换成csv 只有上海电力大学是xlsx文件 """
    file = '10256上海电力大学图书馆业务数据集\\3读者入馆数据_上海电力大学.xlsx'
    schoolname = '上海电力大学'
    nyukan2csv(file, schoolname)
    
    
    