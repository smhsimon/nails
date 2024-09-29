import os
import pandas as pd
import calendar
import shutil

import settings

#can be called whenever, but only does something if the year has changed since the last time it was called
def create_archive():
    os.makedirs('archive', exist_ok=True)

    curr_year_folder = os.path.join('archive', str(settings.curr_year))
    os.makedirs(curr_year_folder, exist_ok=True)

    months = list(calendar.month_name)[1:]
    
    for i in range(1,settings.curr_month + 1):
        month_folder = os.path.join(curr_year_folder, str(i) + '_' + months[i - 1])
        os.makedirs(month_folder, exist_ok=True)

        for j in settings.employees:
            employee_folder = os.path.join(month_folder, j)
            os.makedirs(employee_folder, exist_ok=True)

# should be called daily, moves information to archive
def move_data_daily():
    for path, folders, files in os.walk('employee data'):
        if path == 'employee data':
            continue

        name = path.partition('\\')[2]
        source = os.path.join('employee data', name, name + '_today.csv')
        destination_directory = os.path.join('archive', str(settings.curr_year), str(settings.curr_month) + '_' + settings.curr_month_str, name)
        new_file_name = name + '_' + settings.curr_month_str + '_' + str(settings.curr_day) + '.csv' 
        destination = os.path.join(destination_directory, new_file_name)
        shutil.move(source, destination)

# should be called once at the end of each biweekly period based on following line
# if settings.curr_day == 14 or settings.curr_day == calendar.monthrange(settings.curr_year, settings.curr_month)[1]:
def move_data_biweekly():
    for path, folders, files in os.walk('employee data'):
        if path == 'employee data':
            continue
        
        name = path.partition('\\')[2]
        source = os.path.join('employee data', name, name + '_biweekly.csv')
        destination_directory = os.path.join('archive', str(settings.curr_year), str(settings.curr_month) + '_' + settings.curr_month_str, name)
        if settings.curr_day == 14:
            new_file_name = name + '_' + settings.curr_month_str + '_1st_period.csv' 
        elif settings.curr_day == calendar.monthrange(settings.curr_year, settings.curr_month)[1]:
            new_file_name = name + '_' + settings.curr_month_str + '_2nd_period.csv' 
        destination = os.path.join(destination_directory, new_file_name)
        shutil.move(source, destination)