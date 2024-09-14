import os

import settings
import initialize
import handle_input

date = settings.curr_day

name_input = 'Tamy'
sns_input = 'SNS'
price_input = 35

if not (os.path.exists('employee data\\Lang\\Lang_biweekly.csv')):
    initialize.biweekly_update()
else:
    handle_input.employee_input(name_input, sns_input, price_input)