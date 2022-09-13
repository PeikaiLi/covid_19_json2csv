# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:17:14 2022

@author: Peikai_Li
"""

import os
import json
from service.DXYArea2csv import historyj2c,history_dangerAreas
from service.DXYArea_f2csv import Asymj2c
from service.otherall2csv import DXYOverallj2c,otherj2c

if __name__ == "__main__":
    # 在当前目录创建文件夹
    for save_dir in ['csv']:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        # else:
        #     os.rename(save_dir, save_dir+f"backup_{time.strftime('%Y%m%d_%H_%M')}")
        #     os.makedirs(save_dir)

    in_dirs = 'json/'
    out_dirs = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'csv')
    # dirs ='../csv'
    
    
    with open(f"{in_dirs}DXYArea.json",'r',encoding = "utf-8") as load_f:
        history_dict = json.load(load_f)
    historyj2c(history_dict,out_dirs)
    history_dangerAreas(history_dict,out_dirs)
    
   
    
    with open(f"{in_dirs}DXYArea_f.json",'r',encoding = "utf-8") as load_f:
        DXYArea_f_dict = json.load(load_f)
    Asymj2c(DXYArea_f_dict,out_dirs)
    
    
    with open(f"{in_dirs}DXYOverall.json",'r',encoding = "utf-8") as load_f:
        DXYOverall_dict = json.load(load_f)
    DXYOverallj2c(DXYOverall_dict,out_dirs)
    
    
    for j_file in ['DXYNews.json', 'DXYRumors.json']:
        with open(f"{in_dirs}{j_file}",'r',encoding = "utf-8") as load_f:
            DXYOverall_dict = json.load(load_f)
        otherj2c(DXYOverall_dict,j_file[:-5],out_dirs)
        print(f"{j_file[:-5]} finish")
    
    
 
    
    
    
 


 