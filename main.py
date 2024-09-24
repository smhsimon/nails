import os

import settings
import initialize
import handle_input

import pandas as pd

date = settings.curr_full_date

name_input = 'Ruby'
sns_input = 'SNS'
price_input = 35

# df = pd.read_csv('employee data\Lang\Lang_biweekly.csv')
# if date in df['date'].values:
#     print(True)
# else:
#     print(False

if not (os.path.exists('employee data\\Lang\\Lang_biweekly.csv')) or date not in df['date'].values:
    initialize.biweekly_update()
else:
    handle_input.employee_input(name_input, sns_input, price_input)