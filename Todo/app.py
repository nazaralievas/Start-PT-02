from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/rules')
def rules():
    return render_template('rules.html')


if __name__ == "__main__":
    app.run(debug=True)
