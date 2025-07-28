print("hello world")
from flask import Flask, render_template, request

app = Flask(__name__)

data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        entry = {month: int(request.form[str(month)]) for month in months}
        data.append(entry)
        print(entry)
    return render_template('index.html')
