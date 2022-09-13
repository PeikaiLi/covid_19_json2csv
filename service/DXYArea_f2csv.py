# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:25:15 2022

@author: Peikai_Li
"""


import os
import json
import datetime
import pandas as pd
from tqdm import tqdm


def dict_parser_Asym(document: dict, city_dict: dict = None) -> dict:
    result = dict()

    try:
        result['continentName'] = document['continentName']
        result['continentEnglishName'] = document['continentEnglishName']
    except KeyError:
        result['continentName'] = None
        result['continentEnglishName'] = None

    result['countryName'] = document['countryName']

    try:
        result['countryEnglishName'] = document['countryEnglishName']
    except KeyError:
        result['countryEnglishName'] = None

    result['provinceName'] = document['provinceName']
    result['provinceEnglishName'] = document.get('provinceEnglishName')
    result['province_zipCode'] = document.get('locationId')
    result['province_confirmedCount'] = document['confirmedCount']
    # result['province_suspectedCount'] = document['suspectedCount']
    result['province_yesterdayLocalConfirmedCount'] = document.get('yesterdayLocalConfirmedCount')
    result['province_yesterdayAsymptomaticCount'] = document.get('yesterdayAsymptomaticCount')
    result['province_currentConfirmedCount'] = document.get('currentConfirmedCount')
    result['province_dangerCountIncr'] = document['dangerCountIncr']
    result['province_currentDangerCount'] = document['currentDangerCount']
 

    if city_dict:
        result['cityName'] = city_dict['cityName']
        result['cityEnglishName'] = city_dict.get('cityEnglishName')
        result['city_zipCode'] = city_dict.get('locationId')
        result['city_confirmedCount'] = city_dict['confirmedCount']
        # result['city_suspectedCount'] = city_dict['suspectedCount']
        result['city_yesterdayLocalConfirmedCount'] = city_dict.get('yesterdayLocalConfirmedCount')
        result['city_yesterdayAsymptomaticCount'] = city_dict.get('yesterdayAsymptomaticCount')
        result['city_currentConfirmedCount'] = city_dict['currentConfirmedCount']
        result['city_dangerCountIncr'] = city_dict['dangerCountIncr']
        result['city_currentDangerCount'] = city_dict['currentDangerCount']

    result['updateTime'] = datetime.datetime.fromtimestamp(int(document['updateTime']/1000))

    return result   



def Asymj2c(DXYArea_f_dict:list,dirs:str = os.path.split(os.path.realpath(__file__))[0]):     
    '''
    

    Parameters
    ----------
    DXYArea_f_dict : list
        这里是把json读入后变成list

    Returns
    -------
    None.

    '''
    structured_results = list()
    for document in tqdm(DXYArea_f_dict):
        if document.get('cities', None):
            for city_counter in range(len(document['cities'])):
                city_dict = document['cities'][city_counter]
                structured_results.append(dict_parser_Asym(document=document, city_dict=city_dict))
        else:
            structured_results.append(dict_parser_Asym(document=document))

    df = pd.DataFrame(structured_results)
    df.to_csv(
        path_or_buf=os.path.join(
            dirs, 'DXYArea_f.csv'),
        index=False, encoding='utf_8_sig', float_format="%i"
    )
    

if __name__ == "__main__":
    with open("datas/DXYArea_f.json",'r',encoding = "utf-8") as load_f:
        DXYArea_f_dict = json.load(load_f)
        
    print(type(DXYArea_f_dict))
    Asymj2c(DXYArea_f_dict)
    
    
    








