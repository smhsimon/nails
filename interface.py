from flask import Flask, render_template
import pandas as pd

import settings

app = Flask(__name__)

@app.route('/')
def employee_input():
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