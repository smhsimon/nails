from flask import Flask, request, redirect, flash, render_template
import pandas as pd

import settings
import handle_input

app = Flask(__name__)
app.secret_key = 'a;lsdkfj;alsjh_'

@app.route('/', methods=['GET', 'POST'])
def employee_input():
    if request.method == 'POST':
        name = request.form.get('employee')
        normal_or_SNS = request.form.get('normal_or_SNS')
        price = request.form.get('price')
        handle_input.employee_input(name, normal_or_SNS, int(price))
        
        flash('Thanks, ' + name + '!')
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


if __name__ == '__main__':
    app.run(debug=True)