import os

import settings
import initialize
import handle_input

# initialize.biweekly_update()
# handle_input.employee_input()
if not (os.path.exists('employee data\\Lang\\Lang_biweekly.csv')):
    initialize.biweekly_update()
else:
    handle_input.employee_input()