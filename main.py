print("hello world")
from flask import Flask, render_template, request
from models.average import average
from data import data
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        months = [str(i) for i in range(1, 13)]
        entry = [int(request.form[month]) for month in months]

        data.append(entry)
        #print(entry)

        average()
    return render_template('index.html')
