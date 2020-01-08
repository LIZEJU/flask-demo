import pandas as pd


def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    # print(data.groupby('Date').sum())
    # 重新定义index和value
    s = data.Volume
    # print(s)
    s.index = pd.to_datetime(data.Date)
    # print(s.index)
    print(s)
    import  matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.set_xlabel('jidu')
    ax.set_ylabel('volume')
    ax.set_title('zongji')

    second_volume = s.resample('Q').sum().sort_values()
    '''
    补充代码：
    1. 使用 Pandas 选择数据
    2. 转换为时间序列
    3. 按季度重采样并排序
    '''
    ax.plot(s.index, s)
    plt.savefig('4.png')
    plt.show()
    print(second_volume)
    return second_volume[-2]

if __name__ == '__main__':
    second_volume = quarter_volume()
    print(second_volume)