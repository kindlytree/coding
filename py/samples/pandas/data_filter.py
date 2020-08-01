#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import argparse



if __name__ == "__main__":
    #df = pd.read_csv('/home/lsxu/Documents/clobotics/val/debug_results.csv', encoding='utf-8')
    #df = pd.read_csv('/home/lsxu/Documents/clobotics/val/sku_classification_ccth-sku_20200430_eval_val20200430_only_newchannels_sku0430_sb0430_unit0329_rtd0424_e2e_retail_validation_debug_results.csv', encoding='utf-8')
    #df.describe()
    p = argparse.ArgumentParser(description = 'For function use')
    # p.add_argument('Intergers',help = 'one or more intergers is need',nargs = '+',metavar = 'N',type = int)
    p.add_argument('--ine_sku_metadata',help = 'ine_sku_metadata',type = str)
    p.add_argument('--sku_labels',help = 'sku labels',type = str)
    p.add_argument('--ine_performance_report',help = 'ine_performance_report',type = str)
    p.add_argument('--data_folder',help = 'data folder',type = str)
    
    args = p.parse_args()

    csv_path_list = glob.glob(os.path.join(args.data_folder, '*.csv'))
    df = pd.DataFrame()
    for csv_path in csv_path_list:
      logging.info('csv_path is:....{}'.format(csv_path))
      df=df.append(pd.read_csv(csv_path, index_col=False, encoding='utf-8'))

    ine_sku_metadata_file = args.ine_sku_metadata
    sku_labels_file = args.sku_labels
    ine_performance_report_file = args.ine_performance_report
    