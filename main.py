import os

import settings
import initialize
import handle_input

import pandas as pd

date = settings.curr_full_date

name_input = 'Amy'
normal_transactions = ([1, 2, 3, 4, 5, 6, 7, 8], True)
sns_transactions = ([8, 7, 6, 5, 4, 3, 2, 1], True)

# df = pd.read_csv('employee data\Lang\Lang_biweekly.csv')
# if date in df['date'].values:
#     print(True)
# else:
#     print(False)

# if not (os.path.exists('employee data\\Lang\\Lang_biweekly.csv')) or date not in df['date'].values:
if not os.path.exists('employee data\\Lang\\Lang_biweekly.csv'):
    initialize.biweekly_update()
else:
    handle_input.employee_input(name_input, normal_transactions, sns_transactions)

# $env:FLASK_APP = "interface.py"
# flask run --debug