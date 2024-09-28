import datetime

curr_month = int(datetime.datetime.today().strftime('%m'))
curr_month_str = datetime.datetime.today().strftime('%B')
curr_day = int(datetime.datetime.today().strftime('%d'))
curr_year = int(datetime.datetime.today().strftime('%Y'))
curr_full_date = (datetime.datetime.today().strftime('%B') + ' ' + datetime.datetime.today().strftime('%d') + ', ' + datetime.datetime.today().strftime('%Y'))

curr_month = 10
curr_month_str = 'September'
curr_day = 1
curr_year = 2024
curr_full_date = 'October 1, 2024'


employees = sorted(['Lang', 'Dennis', 'Linda', 'Tamy', 'Mindy', 'Amy', 'May', 'Ruby', 'Lucy', 'Holly', 'Kelly', 'Thanh'])
#employees_full = sorted(['Lang', 'Dennis', 'Linda', 'Tamy', 'Mindy', 'Amy', 'May', 'Ruby', 'Lucy', 'Holly', 'Kelly', 'Thanh'])