import  numpy as np
from pandas import  Series,DataFrame
import pandas as pd
import  matplotlib.pyplot as plt
import  os , json
def read_file(file):


    df = pd.read_json(file)
    data = df.groupby('user_id').sum().head(100)
    print(data)
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.set_title('StudyData')
    ax.plot(data.index, data.minutes)
    plt.savefig('2.png')
    plt.show()
    return ax
if __name__ == '__main__':
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'user_study.json')
    print(path)
    read_file(path)