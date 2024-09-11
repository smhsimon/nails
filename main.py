import calendar
import os

import settings
import initialize
import handle_input

# initialize.biweekly_update()
if not (os.path.exists('Lang.csv')):
    initialize.biweekly_update()
else:
    handle_input.employee_input()