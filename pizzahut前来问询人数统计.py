'''
DSY
2020-04-04
Pray for people fighting against Cov-19
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def main():
    status = input('show or append ? ').lower()
    if status in ['a', 'append']:
        df1 = pd.read_excel('/Users/dengshiyu/Desktop/pizzahut.xlsx', index_col=0)
        print('excel原文件\n',df1)
        # start_date = datetime(2020, 3, 31)
        yr, mon, day = input('Current Date:yyyy-mm-dd').split('-')
        today = datetime(int(yr), int(mon), int(day))
        # morning
        today_morning = eval(input('上午咨询数量: '))
        # afternoon
        today_afternoon = eval(input('下午咨询数量: '))
        # pandas
        df = pd.DataFrame(np.zeros(3).reshape(1, 3))
        df.columns = ['Morning', 'Afternoon', 'Total']
        df.rename({0: today.strftime('%Y-%m-%d')}, axis=0, inplace=True)
        # append pandas
        df.loc[today.strftime('%Y-%m-%d'), 'Morning'] = today_morning
        df.loc[today.strftime('%Y-%m-%d'), 'Afternoon'] = today_afternoon
        df.loc[today.strftime('%Y-%m-%d'), 'Total'] = today_morning + today_afternoon
        df = pd.concat([df1, df])

        df.reset_index(inplace=True)

        ls = list(df['index'])
        for i in range(len(df)):
            if ls.count(df['index'][i]) != 1:
                for j in range(ls.count(df['index'][i]) - 1):
                    df.drop([i], inplace=True,keep='last')
                    ls = list(df['index'])

        df.index = df['index']
        del df['index']

        print(df)

        df.to_excel('/Users/dengshiyu/Desktop/pizzahut.xlsx', encoding='utf-8')

    else:
        print('Show')
        df = pd.read_excel('/Users/dengshiyu/Desktop/pizzahut.xlsx', index_col=0)
        print(df)
        df.reset_index(inplace=True)
        # draw plot
        plt.subplot(2, 1, 1)
        plt.plot(df['index'], df['Morning'], 'o-', label='Morning')
        plt.plot(df['index'], df['Afternoon'], 'o--', label='Afternoon', )
        # legend
        plt.legend()
        # total
        '''plt.bar(df['index'],df['Total'],label='Total')
        for i in zip(df['index'],df['Total']):
            plt.text(df['index'],df['Total']+0.1,df['Total'],ha='center')'''
        # adjust
        plt.xticks(rotation=-10)
        # plt.xlabel('Date')
        plt.ylabel('Number')
        plt.title('Number of people coming to me for pizza')
        plt.grid(b=True)

        # draw pie
        plt.subplot(2, 1, 2)
        data = np.array([df['Morning'].sum(), df['Afternoon'].sum()])
        labels = ['Morning', 'Afternoon']
        labeldistance = 1.1
        plt.pie(data, labels=labels, autopct='%.1f%%', labeldistance=labeldistance)
        plt.savefig('/Users/dengshiyu/Desktop/pizzahut.png', dpi=600)
        plt.show()


'''
            Morning  Afternoon  Total
index                                
2020-03-31      1.0        0.0    1.0
2020-04-01      0.0        1.0    1.0
2020-04-02      0.0        2.0    2.0
2020-04-03      0.0        7.0    7.0
2020-04-04     10.0        0.0   10.0
'''

if __name__ == '__main__':
    main()
