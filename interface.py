from flask import Flask, render_template

import settings

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', employees=settings.employees)

if __name__ == '__main__':
    app.run(debug=True)