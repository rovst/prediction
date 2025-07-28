#flask --app main.py run

print("hello world")
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']='sqlite:///data.db'
db=SQLAlchemy(app)

class data(db.model):
    id=db.month1(db.Interger, primary_key=True)
    id=db.month2(db.Interger, primary_key=True)
    id=db.month3(db.Interger, primary_key=True)
    id=db.month4(db.Interger, primary_key=True)
    id=db.month5(db.Interger, primary_key=True)
    id=db.month6(db.Interger, primary_key=True)
    id=db.month7(db.Interger, primary_key=True)
    id=db.month8(db.Interger, primary_key=True)
    id=db.month9(db.Interger, primary_key=True)
    id=db.month10(db.Interger, primary_key=True)
    id=db.month11(db.Interger, primary_key=True)
    id=db.month12(db.Interger, primary_key=True)

    def __data__(self):
        return'<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ =="main":
    app.run(debug=True)