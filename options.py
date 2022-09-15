#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:29:06 2022

@author: hosammahmoud
"""


import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import os
from datetime import datetime
import requests


def get_spot_derivatives(query):
    path_to_credentials = ('er-poc-341310-47a95b9a5258.json')
    print(path_to_credentials)
    bq = create_engine('bigquery://', credentials_path=path_to_credentials)
    df = pd.read_sql(query, bq)
    return df



if __name__ == '__main__':
 
    ## Get Options volume by expiry 
    
    # df_options_expiry = get_spot_derivatives(
    #     """
    #     SELECT  * 
    #     FROM `er-poc-341310.derivatives.ohlcv` 
    #     where product_type = 'option'
    #     and exchange_name = 'deribit_derivatives'
    #     and underlying_asset = 'ETH'
    #     and date between '2022-09-01' and '2022-09-12'
    #     """
    #     )
    # pivot_options = df_options_expiry.pivot_table(
    #     columns=['call_or_put'],index = 'expiry' ,values='volume_usd' , aggfunc= 'sum' )
    # pivot_options.index = pd.to_datetime(pivot_options.index, format='%Y-%m-%d')
    # # pivot_options = pivot_options.resample('M').sum()

    # pivot_options['ratio'] = pivot_options['call']/pivot_options['put']




    # df_options_volume = get_spot_derivatives(
    #     """
    #     SELECT  * 
    #     FROM `er-poc-341310.derivatives.ohlcv` 
    #     where product_type = 'option'
    #     and exchange_name = 'deribit_derivatives'
    #     and underlying_asset in ('ETH','BTC')
    #     and date between '2022-01-01' and '2022-09-12'
    #     """
    #     )
    # pivot_options = df_options_volume.pivot_table(
    #     columns=['call_or_put', 'underlying_asset'],index = 'date' ,values='volume_usd' , aggfunc= 'sum' )
    # pivot_options.index = pd.to_datetime(pivot_options.index, format='%Y-%m-%d')
    # pivot_options = pivot_options.resample('M').sum()
    # pivot_options.to_excel('binance_ETH_opt.xlsx')    
 

