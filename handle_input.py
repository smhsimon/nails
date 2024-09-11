import pandas as pd
import numpy as np

import settings

def update_calc(df, name):
    if name in settings.employees_full:
        df['total'] = df['normal'] + df['sns']
        df.to_csv(name + '.csv', index = True)
    else:
        df['total'] = df['normal'] + df['sns']
        df_sumless = df.drop(0)
        df.loc[0]['normal'] = df_sumless['normal'].sum()
        df.loc[0]['sns'] = df_sumless['sns'].sum()
        df.loc[0]['total'] = df_sumless['total'].sum()
        df.to_csv(name + '.csv', index = False)

def employee_input():
    name_input = 'Lang'
    sns_input = 'Normal'
    price_input = 45

    # name_input = input('Name?\n')
    # sns_input = input('Normal or SNS?\n')
    # price_input = int(input('Price?\n'))
    
    name_input_i = name_input + '_i'
    
    df = pd.read_csv(name_input + '.csv', index_col=0)
    row = df.loc[settings.curr_full_date]

    df2 = pd.read_csv(name_input_i + '.csv', index_col=False)
    
    if sns_input == 'Normal':
        row['normal'] += np.int64(price_input)
        new_row = pd.DataFrame([[price_input, 0, price_input]], columns=df2.columns)
        df2 = pd.concat([df2, new_row], axis=0, ignore_index=True)

    elif sns_input == 'SNS':
        row['sns'] += np.int64(price_input)
        new_row = pd.DataFrame([[0, price_input, price_input]], columns=df2.columns)
        df2 = pd.concat([df2, new_row], axis=0, ignore_index=True)

    update_calc(df, name_input)
    update_calc(df2, name_input_i)