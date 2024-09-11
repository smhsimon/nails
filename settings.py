import datetime

curr_month = int(datetime.datetime.today().strftime('%m'))
curr_day = int(datetime.datetime.today().strftime('%d'))
curr_year = int(datetime.datetime.today().strftime('%Y'))
curr_full_date = (datetime.datetime.today().strftime('%B') + ' ' + datetime.datetime.today().strftime('%d') + ', ' + datetime.datetime.today().strftime('%Y') )

# employees = sorted(['Lang', 'Dennis', 'Linda'])
employees = sorted(['Lang', 'Dennis', 'Linda', 'Tamy', 'Mindy', 'Amy', 'May', 'Ruby', 'Lucy', 'Holly', 'Kelly', 'Thanh'])
employees_full = sorted(['Lang', 'Dennis', 'Linda', 'Tamy', 'Mindy', 'Amy', 'May', 'Ruby', 'Lucy', 'Holly', 'Kelly', 'Thanh'])