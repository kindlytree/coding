#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
'''
pip3 install pandas -i https://pypi.douban.com/simple
pip3 install ipython -i https://pypi.douban.com/simple
'''

def test_f(x):
  return np.random.rand(1)


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
    df_d = df.append(df_b).reset_index()

    df_e = df_d[['url','clicked_b']].dropna()

    print(df_c, '\n', df_d, '\n', df_e)

    df_h = df_d['clicked_b'].dropna()

    print('df_h is :', df_h)

    df_hh = df_d[['clicked_b']].dropna()
    print('df_hh is :', df_hh)
    #xx = df_h.apply(lambda v: print(v))
    xx = df_h.apply(lambda v: max(3.0, v))

    print('xx is: ', xx)

    test2 = df.groupby('url').apply(lambda x: test_f(x))

    #test2 = test2.reset_index().sort_values(by=0)

    import IPython
    IPython.embed(colors="Linux")

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
