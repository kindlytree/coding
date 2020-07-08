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

def test2(row):
  print(row)
  return row['url']


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

    df2 = pd.DataFrame({'url': 
                ['http://localhost/a',
                 'http://localhost/b',
                 'http://localhost/a',
                 'http://localhost/c',
                 'http://localhost/b',
                 'http://localhost/d',
                  ], 
                'viewed': [
                    3, 
                    4, 
                    5,
                    6,
                    3,
                    4]})
    
    df3 = df.append(df2)

    df['url_copy'] = df.apply(lambda row: test2(row), axis=1)

    # rows_count = df.count()
    rows_count = len(df.index)

    row_0 = df.loc[0]


    df_sampeled = None
    product_ids = df_filtered['ProductId'].unique().tolist()
    for product_id in product_ids:
      df_product = df_filtered[df_filtered['ProductId'] == product_id]
      df_product_count = len(df_product.index)
      if df_product_count > args.max_sample_count:
        df_product = df_product.sample(n= args.max_sample_count, random_state=1)
      df_sampeled = pd.concat([df_sampeled, df_product])

    df_sampeled.to_csv(dest_csv_file)

    df_skuid_skuname = df_ine_performance[df_ine_performance['SkuId'].isin(product_ids)][['SkuId', 'SkuName']]
    dest_skuid_name_file = os.path.join(dest_csv_folder, 'filterd_sku.csv')
    df_skuid_skuname.to_csv(dest_skuid_name_file, index=False)


'''
df_rare_sku_collections = pd.DataFrame()
df_rare_sku_collections = df_rare_sku_collections.append(df_sampled_rare_sku)
not_in_sku_labels_skus = df_ground_truth[~df_ground_truth['ProductId'].isin(sku_labels)]['ProductId'].unique().tolist()
df_sampled_rare_sku = df_rare_sku.sample(n= max_sampler_size, random_state=1)

'''
    import IPython
    IPython.embed(colors="Linux")