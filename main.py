import pandas as pd
import numpy as np
from datetime import datetime
import calendar
import os

curr_month = int(datetime.today().strftime('%m'))
curr_day = int(datetime.today().strftime('%d'))
curr_year = int(datetime.today().strftime('%Y'))
curr_full_date = (datetime.today().strftime('%B') + ' ' + datetime.today().strftime('%d') + ', ' + datetime.today().strftime('%Y') )

def period_initializer(curr_day, name):
    if curr_day < 14:
        start_day = '01'
        end_day = '14'
    else:
        start_day = '15'
        end_day = calendar.monthrange(curr_year, curr_month)[1]

    start_date = '-'.join([str(curr_month),str(start_day),str(curr_year)])
    end_date = '-'.join([str(curr_month),str(end_day),str(curr_year)])

    period = pd.date_range(start = start_date, end = end_date, freq = 'D').strftime('%B %d, %Y')
    cols = ['normal', 'sns', 'total'] 

    df = pd.DataFrame(index = period, columns = cols) 
    df.fillna(0, inplace=True)
    
    csv_name = name + '.csv'
    df.to_csv(csv_name, index=True)

def individual_initializer(name):
    cols = ['normal', 'sns', 'total'] 
    df = pd.DataFrame([[0, 0, 0]], columns=cols)
    csv_name = name + '_i.csv'
    df.to_csv(csv_name, index = False)

def update_calc(df, name):
    if name in employees_full:
        df['total'] = df['normal'] + df['sns']
        df.to_csv(name + '.csv', index = True)
    else:
        df['total'] = df['normal'] + df['sns']
        df.loc[0]['normal'] = df['normal'].sum()
        df.loc[0]['sns'] = df['sns'].sum()
        df.loc[0]['total'] = df['total'].sum()
        df.to_csv(name + '.csv', index = False)

employees_full = ['Lang', 'Dennis', 'Linda', 'Tamy', 'Mindy', 'Amy', 'May', 'Ruby', 'Lucy', 'Holly', 'Kelly', 'Thanh']
employees = ['Lang', 'Dennis', 'Linda']

def handle_input():
    name_input = 'Lang'
    sns_input = 'Normal'
    price_input = 35

    name_input_i = name_input + '_i'
    
    df = pd.read_csv(name_input + '.csv', index_col=0)
    row = df.loc[curr_full_date]

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
    print(df2.loc[0])

def biweekly_update():
    for employee in employees:
        period_initializer(curr_day, employee)
        individual_initializer(employee)

if not (os.path.exists('Lang.csv')):
    biweekly_update()
else:
    handle_input()