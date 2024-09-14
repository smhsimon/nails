import os

import settings
import initialize
import handle_input

date = settings.curr_day

if not (os.path.exists('employee data\\Lang\\Lang_biweekly.csv')):
    initialize.biweekly_update()
else:
    handle_input.employee_input()