import datetime

actual = datetime.date.today()
new = datetime.date.today()
curr_month = int(datetime.datetime.today().strftime('%m'))
curr_month_str = datetime.datetime.today().strftime('%B')
curr_day = int(datetime.datetime.today().strftime('%d'))
curr_year = int(datetime.datetime.today().strftime('%Y'))
curr_full_date = (datetime.datetime.today().strftime('%B') + ' ' + datetime.datetime.today().strftime('%d') + ', ' + datetime.datetime.today().strftime('%Y'))

def cycle_day():
    global new, curr_month, curr_month_str, curr_day, curr_year, curr_full_date
    
    new += datetime.timedelta(days=1)

    curr_month = int(new.strftime('%m'))
    curr_month_str = new.strftime('%B')
    curr_day = int(new.strftime('%d'))
    curr_year = int(new.strftime('%Y'))
    curr_full_date = (new.strftime('%B') + ' ' + new.strftime('%d') + ', ' + new.strftime('%Y'))

def reset_date():
    global new, curr_month, curr_month_str, curr_day, curr_year, curr_full_date
    
    new = actual
    curr_month = int(new.strftime('%m'))
    curr_month_str = new.strftime('%B')
    curr_day = int(new.strftime('%d'))
    curr_year = int(new.strftime('%Y'))
    curr_full_date = (new.strftime('%B') + ' ' + new.strftime('%d') + ', ' + new.strftime('%Y'))

employees = sorted(['Lang', 'Dennis', 'Linda', 'Tamy', 'Mindy', 'Amy', 'May', 'Ruby', 'Lucy', 'Holly', 'Kelly', 'Thanh'])