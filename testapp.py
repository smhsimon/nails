from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('<h1>Hello, {{ name }}!</h1>', name='World')

if __name__ == '__main__':
    app.run(debug=True)
