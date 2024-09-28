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
        
    if not biweekly:
        csv_name2 = name + '_today.csv'
        filepath2 = os.path.join(subdirectory, csv_name2)
        df['total'] = df['normal'] + df['sns']
        df_sumless = df.drop(0
        )
        df.loc[0, 'normal'] = df_sumless['normal'].sum()
        df.loc[0, 'sns'] = df_sumless['sns'].sum()
        df.loc[0, 'total'] = df_sumless['total'].sum()
        df['total'] = df['normal'] + df['sns']
        df.to_csv(filepath2, index = False)

def employee_input(name_input, normal_transactions, sns_transactions, batch):
    csv_name = name_input + '_biweekly.csv'
    csv_name2 = name_input + '_today.csv'

    subdirectory = os.path.join('employee data', name_input)

    filepath = os.path.join(subdirectory, csv_name)
    filepath2 = os.path.join(subdirectory, csv_name2)
    
    df = pd.read_csv(filepath, index_col=0)
    row = df.loc[settings.curr_full_date]

    df2 = pd.read_csv(filepath2, index_col=False)
    
    if normal_transactions[1]:
        for i in normal_transactions[0]:
            row['normal'] += np.int64(i)
            new_row = pd.DataFrame([[i, 0, i, batch]], columns=df2.columns)
            df2 = pd.concat([df2, new_row], axis=0, ignore_index=True)

    if sns_transactions[1]:
        for i in sns_transactions[0]:
            row['sns'] += np.int64(i)
            new_row = pd.DataFrame([[0, i, i, batch]], columns=df2.columns)
            df2 = pd.concat([df2, new_row], axis=0, ignore_index=True)

    update_calc(df, name_input, True)
    update_calc(df2, name_input, False)

def deletion(name_input, batch):
    csv_name = name_input + '_biweekly.csv'
    csv_name2 = name_input + '_today.csv'

    subdirectory = os.path.join('employee data', name_input)

    filepath = os.path.join(subdirectory, csv_name)
    filepath2 = os.path.join(subdirectory, csv_name2)
    
    df = pd.read_csv(filepath, index_col=0)

    df2 = pd.read_csv(filepath2, index_col=False)

    result = df2.loc[df2['batch'] == batch]

    sum_normal = result['normal'].sum()
    sum_sns = result['sns'].sum()
    sum_total = result['total'].sum()

    df2 = df2.drop(result.index)

    row = df.loc[settings.curr_full_date]
    row['normal'] -= sum_normal
    row['sns'] -= sum_sns

    update_calc(df, name_input, True)
    update_calc(df2, name_input, False)