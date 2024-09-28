from flask import Flask, request, redirect, flash, render_template
import os
import pandas as pd


import settings
import handle_input

app = Flask(__name__)
app.secret_key = 'a;lsdkfj;alsjh_'

@app.route('/', methods=['GET', 'POST'])
def employee_input():
    if request.method == 'POST':
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

        flash('Input recorded!')
    return render_template('index.html', employees=settings.employees, date=settings.curr_full_date)

@app.route('/biweekly')
def biweekly():
    tables = []

    for employee in settings.employees:
        data = pd.read_csv('employee data\\' + employee + '\\' + employee + '_biweekly.csv')
        tables.append((data.to_html(classes='data', index=False), employee))

    return render_template('biweekly.html', tables=tables)


@app.route('/today') 
def today(): 
    tables = []

    for employee in settings.employees:
        data = pd.read_csv('employee data\\' + employee + '\\' + employee + '_today.csv')
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