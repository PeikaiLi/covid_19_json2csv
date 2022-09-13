# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:48:40 2022

@author: Peikai_Li
"""

# import os
# import pandas as pd

# ['csv/DXYArea.csv','DXYArea_dangerAreas.csv','csv/DXYArea_f.csv','csv/DXYOverall.csv']
# ['csv/DXYNews.csv', 'csv/DXYRumors.csv']


#     cursor = self.db.dump(collection=collection)
#     self.csv_dumper(collection=collection, cursor=cursor)
#     logger.info(collection + '.csv dumped!')
        

    # def csv_dumper(self, collection: str, cursor):
        
        # if collection == 'DXYArea':
            
        #     structured_area_results = list()
        #     structured_results = list()
            
        #     for document in cursor:
        #         # datas
        #         if document.get('cities', None):
        #             # get() 方法和 [key] 方法的主要区别在于，
        #             # [key] 在遇到不存在的 key 时会抛出 KeyError 错误
        #             for city_counter in range(len(document['cities'])):
        #                 city_dict = document['cities'][city_counter]
        #                 structured_results.append(self.dict_parser(document=document, city_dict=city_dict))
        #         else:
        #             structured_results.append(self.dict_parser(document=document))
                    
        #                 # 对于有城市的
        #         if document.get('dangerAreas', None):
        #             for dangerAreas_counter in range(len(document['dangerAreas'])):
        #                 dangerAreas_dict = document['dangerAreas'][dangerAreas_counter]
        #                 structured_area_results.append(self.dict_dangerAreas(document=document, dangerAreas_dict=dangerAreas_dict))
        


        #     df = pd.DataFrame(structured_results)
        #     df.to_csv(
        #         path_or_buf=os.path.join(
        #             os.path.split(os.path.realpath(__file__))[0], 'csv', collection + '.csv'),
        #         # os.path.split(os.path.realpath(__file__))[0] 当前文件夹 == pwd
        #         index=False, encoding='utf_8_sig', float_format="%i"
        #     )
            
            
        #     df = pd.DataFrame(structured_area_results)
        #     df.to_csv(
        #         path_or_buf=os.path.join(
        #             os.path.split(os.path.realpath(__file__))[0], 'csv', collection + '_dangerAreas.csv'),
        #         # os.path.split(os.path.realpath(__file__))[0] 当前文件夹 == pwd
        #         index=False, encoding='utf_8_sig', float_format="%i"
        #     )


        # elif collection == 'DXYArea_f':
        #     structured_results = list()
        #     for document in cursor:
        #         if document.get('cities', None):
        #             for city_counter in range(len(document['cities'])):
        #                 city_dict = document['cities'][city_counter]
        #                 structured_results.append(self.dict_parser_Asym(document=document, city_dict=city_dict))
        #         else:
        #             structured_results.append(self.dict_parser_Asym(document=document))

        #     df = pd.DataFrame(structured_results)
        #     df.to_csv(
        #         path_or_buf=os.path.join(
        #             os.path.split(os.path.realpath(__file__))[0], 'csv', collection + '.csv'),
        #         index=False, encoding='utf_8_sig', float_format="%i"
        #     )


        # elif collection == 'DXYOverall':
        #     df = pd.DataFrame(data=cursor)
        #     for time_type in time_types:
        #         if time_type in df.columns:
        #             df[time_type] = df[time_type].apply(lambda x: datetime.datetime.fromtimestamp(x / 1000) if not pd.isna(x) else '')
        #     del df['_id']
        #     del df['infectSource']
        #     del df['passWay']
        #     del df['virus']
        #     df.to_csv(
        #         path_or_buf=os.path.join(
        #             os.path.split(os.path.realpath(__file__))[0], 'csv', collection + '.csv'),
        #         index=False, encoding='utf_8_sig', date_format="%Y-%m-%d %H:%M:%S"
        #     )
        # else:
        #     df = pd.DataFrame(data=cursor)
        #     for time_type in time_types:
        #         if time_type in df.columns:
        #             df[time_type] = df[time_type].apply(lambda x: datetime.datetime.fromtimestamp(x / 1000) if not pd.isna(x) else '')
        #     df.to_csv(
        #         path_or_buf=os.path.join(
        #             os.path.split(os.path.realpath(__file__))[0], 'csv', collection + '.csv'),
        #         index=False, encoding='utf_8_sig', date_format="%Y-%m-%d %H:%M:%S"
        #     )