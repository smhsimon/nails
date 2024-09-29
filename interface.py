import os
import pandas as pd
from flask import Flask, request, redirect, flash, render_template
import calendar

import settings
import handle_input
import initialize
import archive

app = Flask(__name__)
app.secret_key = 'a;lsdkfj;alsjh_'

def handle_employee_input():
    name = request.form.get('employee')
    
    csv_name = name + '_today.csv'
    subdirectory = os.path.join('employee data', name)
    filepath = os.path.join(subdirectory, csv_name)
    df = pd.read_csv(filepath, index_col=False)

    if len(df) == 1:
        batch = 1
    else:
        batch = df.iloc[-1]['batch'] + 1

    normal = ''
    normal_raw = request.form.get('normal')
    if normal_raw != '':
        normal = [int(x) for x in normal_raw.strip(', ').split(',')]
    proceed_normal = (normal, normal != '' and type(normal) != str)

    sns = ''
    sns_raw = request.form.get('sns')
    if sns_raw != '':
        sns = [int(x) for x in sns_raw.strip(', ').split(',')]
    proceed_sns = (sns, sns != '' and type(sns) != str)

    handle_input.employee_input(name, (normal, proceed_normal), (sns, proceed_sns), batch)

    flash('Input recorded!', 'dog')

def daily_archive():
    archive.move_data_daily()
    initialize.initialize(False)
    flash('test!', 'cat')

def biweekly_archive():
    archive.move_data_biweekly()
    initialize.initialize(True)
    flash('test 2!', 'rat')
    
@app.route('/', methods=['GET', 'POST'])
def handle_buttons():  
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'Submit':
            handle_employee_input()
        elif action == 'daily archive':
            daily_archive()
            settings.cycle_day()
        elif action == 'biweekly archive':
            if settings.curr_day == 14 or settings.curr_day == calendar.monthrange(settings.curr_year, settings.curr_month)[1]:
                daily_archive()
                biweekly_archive()
                settings.cycle_day()
                print(settings.curr_full_date)
                initialize.initialize(True)
                archive.create_archive()
            else:                
                flash('it isn\'t the end of the biweekly period.', 'rat')

        elif action == 'cycle day':
            settings.cycle_day()

        elif action == 'reset date':
            settings.reset_date()
        elif action == 'initializer':
            initialize.initialize(True)
            archive.create_archive()


        return redirect('/')
    print(f"Current date: {settings.curr_full_date}")
    return render_template('index.html', employees=settings.employees, date=settings.curr_full_date)

@app.route('/biweekly')
def biweekly():
    tables = []

    for employee in settings.employees:
        data = pd.read_csv(os.path.join('employee data', employee, employee + '_biweekly.csv'))
        tables.append((data.to_html(classes='data', index=False), employee))

    return render_template('biweekly.html', tables=tables)


@app.route('/today') 
def today(): 
    tables = []

    for employee in settings.employees:
        data = pd.read_csv(os.path.join('employee data', employee, employee + '_today.csv'))
        tables.append((data.to_html(classes='data', index=False), employee))

    return render_template('today.html', tables=tables)

@app.route('/deletion', methods=['GET', 'POST']) 
def deletion(): 
    if request.method == 'POST':
        name = request.form.get('employee')
        batch = int(request.form.get('batch'))
        
        handle_input.deletion(name, batch)
        flash('Input recorded!')
    return render_template('deletion.html', employees=settings.employees)

if __name__ == '__main__':
    app.run(debug=True)