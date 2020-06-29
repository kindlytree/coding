#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pandas as pd

'''
pip3 install pandas -i https://pypi.douban.com/simple
pip3 install ipython -i https://pypi.douban.com/simple
'''

if __name__ == "__main__":
    df = pd.read_csv('/home/lsxu/Documents/clobotics/val/debug_results.csv', encoding='utf-8')
    #df = pd.read_csv('/home/lsxu/Documents/clobotics/val/sku_classification_ccth-sku_20200430_eval_val20200430_only_newchannels_sku0430_sb0430_unit0329_rtd0424_e2e_retail_validation_debug_results.csv', encoding='utf-8')
    #df.describe()
    import IPython
    IPython.embed(colors="Linux")

    #df.describe()
    #df.head()
    #df.columns
