import os
import pandas as pd

import settings
import initialize
import handle_input

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
# if not os.path.exists('employee data\\Lang\\Lang_biweekly.csv'):

initialize.initialize(True)

# else:
#     handle_input.employee_input(name_input, normal_transactions, sns_transactions)

# $env:FLASK_APP = "interface.py"
# flask run --debug

# handle_input.employee_input('Amy', ([1], True), (0, False), 1)
# handle_input.employee_input('Dennis', ([2], True), (0, False), 1)
# handle_input.employee_input('Holly', ([3], True), (0, False), 1)
# handle_input.employee_input('Kelly', ([4], True), (0, False), 1)
# handle_input.employee_input('Lang', ([5], True), (0, False), 1)
# handle_input.employee_input('Linda', ([6], True), (0, False), 1)
# handle_input.employee_input('Lucy', ([7], True), (0, False), 1)
# handle_input.employee_input('May', ([8], True), (0, False), 1)
# handle_input.employee_input('Mindy', ([9], True), (0, False), 1)
# handle_input.employee_input('Ruby', ([10], True), (0, False), 1)
# handle_input.employee_input('Tamy', ([11], True), (0, False), 1)
# handle_input.employee_input('Thanh', ([12], True), (0, False), 1)

# handle_input.employee_input('Amy', ([12], True), (0, False), 1)
# handle_input.employee_input('Dennis', ([11], True), (0, False), 1)
# handle_input.employee_input('Holly', ([10], True), (0, False), 1)
# handle_input.employee_input('Kelly', ([9], True), (0, False), 1)
# handle_input.employee_input('Lang', ([8], True), (0, False), 1)
# handle_input.employee_input('Linda', ([7], True), (0, False), 1)
# handle_input.employee_input('Lucy', ([6], True), (0, False), 1)
# handle_input.employee_input('May', ([5], True), (0, False), 1)
# handle_input.employee_input('Mindy', ([4], True), (0, False), 1)
# handle_input.employee_input('Ruby', ([3], True), (0, False), 1)
# handle_input.employee_input('Tamy', ([2], True), (0, False), 1)
# handle_input.employee_input('Thanh', ([1], True), (0, False), 1)