# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/1/9 1:31 PM
# Project: flask-demo

import  pandas as pd


def co2():
    '''co2() 函数用于数据统计，大致步骤如下：
        1. 使用 grouby 按题目规则求和
        2. 对数据进行排序并得到目标 DataFrame
        '''
    # 读取清洁后数据
    df = data_clean()


    # 按收入群体对数据进行求和
    df_sum = df.groupby('Income group').sum()
    # print(df_sum.head(5))

    df_max = df.sort_values(by='Sum emissions', ascending=False).groupby(
        'Income group').head(1).set_index('Income group')
    df_max.columns = ['Highest emissions', 'Highest emission country']
    df_max = df_max.reindex(
        columns=['Highest emission country', 'Highest emissions'])

    df_min = df.sort_values(by='Sum emissions').groupby(
        'Income group').head(1).set_index('Income group')
    df_min.columns = ['Lowest emissions', 'Lowest emission country']
    df_min = df_min.reindex(
        columns=['Lowest emission country', 'Lowest emissions'])

    result = pd.concat([df_sum, df_max, df_min], axis=1)

    return result

def data_clean():
    data = pd.read_excel("climatechange.xlsx", sheet_name='Data')
    # 处理 data 数据表 # 选取 EN.ATM.CO2E.KT 数据，并将国家代码设置为索引
    # Series code 数据类别  'EN.ATM.CO2E.KT 二氧化碳排放量  Country code 国家编码
    data = data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    # print(data.head(5))
    # 剔除不必要的数据列 ,剩下year和对应的数据
    data.drop(labels=['Country name', 'Series code',
                      'Series name', 'SCALE', 'Decimals'], axis=1, inplace=True)

    # print(data.head(5))
    # 将原数据集中不规范的空值替换为 NaN 方便填充
    data.replace({'..': pd.np.NaN}, inplace=True)
    # print(data.head(5))
    # 对 NaN 空值进行向前和向后填充
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    # print(data.head(5))
    # 对填充后依旧全部为空值的数据行进行剔除
    data.dropna(how='all', inplace=True)
    data['Sum emissions'] = data.sum(axis=1)
    data = data['Sum emissions']
    # print(data.head(5))

    # 处理 Country 数据表
    # 将国家代码设置为索引
    countries = pd.read_excel("climatechange.xlsx", sheet_name='Country')
    countries.set_index('Country code', inplace=True)
    # 剔除不必要的数据列
    countries.drop(labels=['Capital city', 'Region',
                           'Lending category'], axis=1, inplace=True)

    # 合并数据表
    # 对 Data 和 Country 表按照索引进行合并
    return pd.concat([data, countries], axis=1)
    # return pd.merge(pd.DataFrame(data), countries, left_index=True, right_index=True)

if __name__ == '__main__':
    result = co2()
    print(result.head(5))
    # data_clean()