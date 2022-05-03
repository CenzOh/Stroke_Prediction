from flask import Blueprint, redirect, render_template, url_for, session, request
from App_be.model_.test_model import predict_
from App_be.config import User, db
home_actions = Blueprint('home_actions', __name__, template_folder='templates')

inputs = [ 
    {'name':'gender', 'text': 'Gender', 'type': 'select', 'values': [ 'Female', 'Male' ]},
    {'name':'age', 'text': 'Age', 'type': 'number'},
    {'name':'hypertension', 'text': 'Hypertension', 'type': 'select', 'values': [ 'No', 'Yes' ]},
    {'name':'ever_married', 'text': 'Are you married?', 'type': 'select', 'values': [ 'No', 'Yes' ]},
    {'name':'heart_disease', 'text': 'Heart Disease', 'type': 'select', 'values': [ 'No', 'Yes' ]},
    {'name':'work_type', 'text': 'Work Type', 'type': 'select', 'values': [ 'Government Job', 'Never Worked', 'Private', 'Self Employeed', 'Children' ]},
    {'name':'Residence_type', 'text': 'Residence Type', 'type': 'select', 'values': [ 'Rular', 'Urban' ]},
    {'name':'avg_glucose_level', 'text': 'Average Glucode Level', 'type': 'number'},
    {'name':'bmi', 'text': 'BMI', 'type': 'number'},
    {'name':'smoking_status', 'text': 'Smoking Status', 'type': 'select', 'values': [ 'Unknown', 'Formely smoked', 'Never smoked', 'Smokes' ]},
]

@home_actions.route('/')
def index():
    if "user_id" not in session:
        return redirect(url_for('user_actions.login'))
    user = User.query.filter_by(id=session.get('user_id')).first()
    return render_template('home.html', inputs=inputs, user=user)

@home_actions.route('/perform', methods=['POST'])
def perform():
    if "user_id" not in session:
        return redirect(url_for('user_actions.login'))
    req_data = request.form
    gender = req_data.get("gender")
    age = req_data.get("age")
    hypertension = req_data.get("hypertension")
    heart_disease = req_data.get("heart_disease")
    ever_married = req_data.get("ever_married")
    work_type = req_data.get("work_type")
    Residence_type = req_data.get("Residence_type")
    avg_glucose_level = req_data.get("avg_glucose_level")
    bmi = req_data.get("bmi")
    smoking_status = req_data.get("smoking_status")
    p = predict_(gender, age, hypertension, heart_disease, ever_married,
                 work_type, Residence_type, avg_glucose_level, bmi, smoking_status)
    p = int(p)
    user = User.query.filter_by(id=session.get('user_id')).first()
    user.stroke = p
    db.session.commit()
    return redirect(url_for('home_actions.output'))

@home_actions.route('/perform')
def output():
    if "user_id" not in session:
        return redirect(url_for('user_actions.login'))
    user = User.query.filter_by(id=session.get('user_id')).first()
    return render_template('output.html', user=user)

