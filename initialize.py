import pandas as pd
import os

import settings

directory = 'employee data'

def period_initializer(name):
    if settings.curr_day < 14:
        start_day = '01'
        end_day = '14'
    else:
        start_day = '15'
        end_day = calendar.monthrange(settings.curr_year, settings.curr_month)[1]

    start_date = '-'.join([str(settings.curr_month),str(start_day),str(settings.curr_year)])
    end_date = '-'.join([str(settings.curr_month),str(end_day),str(settings.curr_year)])

    period = pd.date_range(start = start_date, end = end_date, freq = 'D').strftime('%B %d, %Y')
    cols = ['normal', 'sns', 'total'] 

    df = pd.DataFrame(index = period, columns = cols) 
    df.fillna(0, inplace=True)
    
    csv_name = name + '_biweekly.csv'
    subdirectory = os.path.join(directory, name)
    filepath = os.path.join(subdirectory, csv_name)
    df.to_csv(filepath, index=True)

def individual_initializer(name):
    cols = ['normal', 'sns', 'total'] 
    df = pd.DataFrame([[0, 0, 0]], columns=cols)

    csv_name = name + '_today.csv'
    subdirectory = os.path.join(directory, name)
    filepath = os.path.join(subdirectory, csv_name)
    df.to_csv(filepath, index = False)

def folder_initializer():
    for employee in settings.employees:
        if not os.path.isdir('employee data/' + employee):
            os.makedirs('employee data/' + employee)

def biweekly_update():
    for employee in settings.employees:
        if not os.path.isdir(os.path.join('employee data', employee)):
            folder_initializer()

        period_initializer(employee)
        individual_initializer(employee)