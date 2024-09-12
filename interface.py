from flask import Flask, render_template
import pandas as pd

import settings

app = Flask(__name__)

@app.route('/')
def employee_input():
    return render_template('index.html', employees=settings.employees, date=settings.curr_full_date)

@app.route('/second')
def second_page():
    return render_template('second.html')

@app.route('/table') 
def table(): 
    data = pd.read_csv('employee data\Lang\Lang_today.csv')
    data2 = pd.read_csv('employee data\Lang\Lang_biweekly.csv') 

    tables = [
        (data.to_html(classes='data', index=False), 'Lang Today'),
        (data2.to_html(classes='data', index=False), 'Lang Biweekly')
    ]

    return render_template('table.html', tables=tables)


if __name__ == '__main__':
    app.run(debug=True)