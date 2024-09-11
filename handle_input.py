import pandas as pd
import numpy as np
import os

import settings

def update_calc(df, name, biweekly):
    subdirectory = os.path.join('employee data', name)

    if biweekly:
        csv_name = name + '_biweekly.csv'
        filepath = os.path.join(subdirectory, csv_name)
        df['total'] = df['normal'] + df['sns']
        df.to_csv(filepath, index = True)
    elif not biweekly:
        csv_name2 = name + '_today.csv'
        filepath2 = os.path.join(subdirectory, csv_name2)
        df['total'] = df['normal'] + df['sns']
        df_sumless = df.drop(0)
        df.loc[0]['normal'] = df_sumless['normal'].sum()
        df.loc[0]['sns'] = df_sumless['sns'].sum()
        df.loc[0]['total'] = df_sumless['total'].sum()
        df.to_csv(filepath2, index = False)

def employee_input():
    name_input = 'Lang'
    sns_input = 'Normal'
    price_input = 35

    # name_input = input('Name?\n')
    # sns_input = input('Normal or SNS?\n')
    # price_input = int(input('Price?\n'))
    
    name_input_today = name_input + '_today'

    csv_name = name_input + '_biweekly.csv'
    csv_name2 = name_input + '_today.csv'

    subdirectory = os.path.join('employee data', name_input)

    filepath = os.path.join(subdirectory, csv_name)
    filepath2 = os.path.join(subdirectory, csv_name2)
    
    df = pd.read_csv(filepath, index_col=0)
    row = df.loc[settings.curr_full_date]

    df2 = pd.read_csv(filepath2, index_col=False)
    
    if sns_input == 'Normal':
        row['normal'] += np.int64(price_input)
        new_row = pd.DataFrame([[price_input, 0, price_input]], columns=df2.columns)
        df2 = pd.concat([df2, new_row], axis=0, ignore_index=True)

    elif sns_input == 'SNS':
        row['sns'] += np.int64(price_input)
        new_row = pd.DataFrame([[0, price_input, price_input]], columns=df2.columns)
        df2 = pd.concat([df2, new_row], axis=0, ignore_index=True)

    update_calc(df, name_input, True)
    update_calc(df2, name_input, False)