# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:57:15 2022

@author: Peikai_Li
"""


import os
import json
import datetime
import pandas as pd


time_types = ('pubDate', 'createTime', 'modifyTime', 'dataInfoTime', 'crawlTime', 'updateTime')


def DXYOverallj2c(DXYOverall_dict:list,dirs):
    # dirs = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'csv')
    df = pd.DataFrame(DXYOverall_dict)
    for time_type in time_types:
        if time_type in df.columns:
            df[time_type] = df[time_type].apply(lambda x: datetime.datetime.fromtimestamp(x / 1000) if not pd.isna(x) else '')
    # del df['_id']
    del df['infectSource']
    del df['passWay']
    del df['virus']
    df.to_csv(
        path_or_buf=os.path.join(dirs,'DXYOverall.csv'),
        index=False, encoding='utf_8_sig', date_format="%Y-%m-%d %H:%M:%S"
    )
  
    
def otherj2c(other_list:list,name,dirs):
    # dirs = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'csv')
    df = pd.DataFrame(other_list)
    for time_type in time_types:
        if time_type in df.columns:
            df[time_type] = df[time_type].apply(lambda x: datetime.datetime.fromtimestamp(x / 1000) if not pd.isna(x) else '')
    df.to_csv(
        path_or_buf=os.path.join(dirs,name + '.csv'),
        index=False, encoding='utf_8_sig', date_format="%Y-%m-%d %H:%M:%S"
     )
        

if __name__ == "__main__":
    # dirs = os.path.join('../'+os.path.split(os.path.realpath(__file__))[0], 'csv')
    dirs ='../csv'
    with open("../datas/DXYOverall.json",'r',encoding = "utf-8") as load_f:
        DXYOverall_dict = json.load(load_f)
    DXYOverallj2c(DXYOverall_dict,dirs)
    print("DXYOverallj2c finished")
    
    for j_file in ['DXYNews.json', 'DXYRumors.json']:
        with open(f"../datas/{j_file}",'r',encoding = "utf-8") as load_f:
            DXYOverall_dict = json.load(load_f)
        otherj2c(DXYOverall_dict,j_file[:-5],dirs)
        print(f"{j_file[:-5]} finish")
        
    
    
    
    
    
    
            