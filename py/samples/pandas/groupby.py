#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pandas as pd

'''
pip3 install pandas -i https://pypi.douban.com/simple
pip3 install ipython -i https://pypi.douban.com/simple
'''

if __name__ == "__main__":
    #df = pd.read_csv('/home/lsxu/Documents/clobotics/val/debug_results.csv', encoding='utf-8')
    #df = pd.read_csv('/home/lsxu/Documents/clobotics/val/sku_classification_ccth-sku_20200430_eval_val20200430_only_newchannels_sku0430_sb0430_unit0329_rtd0424_e2e_retail_validation_debug_results.csv', encoding='utf-8')
    #df.describe()
    
    df = pd.DataFrame({'url': 
                ['http://localhost/a',
                 'http://localhost/b',
                 'http://localhost/a',
                 'http://localhost/c',
                 'http://localhost/b',
                 'http://localhost/d',
                  ], 
                'clicked': [
                    3, 
                    4, 
                    5,
                    6,
                    3,
                    4]})


    test = df.groupby('url').apply(lambda x: x['clicked'])

    df_b = df.copy(deep=True)


    # df_b.add_suffix('_b')
    # df_b.add_suffix('_b')
    df_b = df_b.add_suffix('_b')
    df_b.rename(columns={'url_b':'url'}, inplace=True)
    df_c = df.append(df_b)

    print(df_c)

    # import IPython
    # IPython.embed(colors="Linux")


    #test.loc['http://localhost/a']
    '''
In [34]: test2                                                                                                                                
Out[34]: 
url                  
http://localhost/a  0    3
                    2    5
http://localhost/b  1    4
                    4    3
http://localhost/c  3    6
http://localhost/d  5    4
Name: clicked, dtype: int64

    
In [35]: test2.index                                                                                                                          
Out[35]: 
MultiIndex([('http://localhost/a', 0),
            ('http://localhost/a', 2),
            ('http://localhost/b', 1),
            ('http://localhost/b', 4),
            ('http://localhost/c', 3),
            ('http://localhost/d', 5)],
           names=['url', None])

In [37]: test2.loc['http://localhost/a']                                                                                                      
Out[37]: 
0    3
2    5
Name: clicked, dtype: int64

index.get_level_values(0).unique()

In [38]: test2.index.get_level_values(0).unique()                                                                                             
Out[38]: 
Index(['http://localhost/a', 'http://localhost/b', 'http://localhost/c',
       'http://localhost/d'],
      dtype='object', name='url')


In [39]: test2.index.get_level_values(0).unique()[0]                                                                                          
Out[39]: 'http://localhost/a'
    '''
    #df.describe()
    #df.head()
    #df.columns
