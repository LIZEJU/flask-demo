# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/1/9 1:31 PM
# Project: flask-demo

import  pandas as pd


def co2():

    # 入去世界银行气候变化数据集
    df_climate = pd.read_excel('climatechange.xlsx',sheet_name='Country')

    s = df_climate['Income group']
    s.index = df_climate['Country name']
    print(s.head(10))


if __name__ == '__main__':
    co2()