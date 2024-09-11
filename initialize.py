import pandas as pd

import settings

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
    
    csv_name = name + '.csv'
    df.to_csv(csv_name, index=True)

def individual_initializer(name):
    cols = ['normal', 'sns', 'total'] 
    df = pd.DataFrame([[0, 0, 0]], columns=cols)
    csv_name = name + '_i.csv'
    df.to_csv(csv_name, index = False)

def biweekly_update():
    for employee in settings.employees:
        period_initializer(employee)
        individual_initializer(employee)