from flask import Flask, render_template, request, redirect, url_for
from models.average import average
from data import data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        months = [str(i) for i in range(1, 13)]
        entry = [int(request.form[month]) for month in months]
        data.append(entry)

        avg = average()
        return redirect(url_for('output', avg=avg))

    return render_template('index.html')

@app.route('/output')
def output():
    avg = request.args.get('avg', default=0, type=float)
    return render_template('output.html', message=avg)
