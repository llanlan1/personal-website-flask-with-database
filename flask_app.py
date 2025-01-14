from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace with your actual MySQL credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lanlan91:01928374pqowieur@lanlan91.mysql.pythonanywhere-services.com/lanlan91$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a Visitor model
class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

# Create the tables (run this once to set up)
# Comment this out after the first run to avoid unnecessary calls
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    visitor = Visitor.query.first()
    if not visitor:
        visitor = Visitor(count=0)
        db.session.add(visitor)
        db.session.commit()

    # Increment the visitor count
    visitor.count += 1
    db.session.commit()

    return render_template('portfoliobylan.html', visitor_count=visitor.count)

app.config['DEBUG'] = False


def init_resources():
    # Code to initialize database connection or other resources
    pass

init_resources()

