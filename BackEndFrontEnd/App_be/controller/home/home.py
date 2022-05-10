from flask import Blueprint, redirect, render_template, url_for, session, request,flash
from App_be.model_.test_model import predict_
from App_be.config import User, db,PridictionsHistory

home_actions = Blueprint('home_actions', __name__, template_folder='templates')
from datetime import datetime

inputs = [ 
    {'name':'gender', 'text': 'Gender', 'type': 'select', 'values': [ 'Female', 'Male' ]},
    {'name':'age', 'text': 'Age (in years)', 'type': 'number'},
    {'name':'hypertension', 'text': 'Hypertension', 'type': 'select', 'values': [ 'No', 'Yes' ]},
    {'name':'ever_married', 'text': 'Are you married?', 'type': 'select', 'values': [ 'No', 'Yes' ]},
    {'name':'heart_disease', 'text': 'Heart Disease', 'type': 'select', 'values': [ 'No', 'Yes' ]},
    {'name':'work_type', 'text': 'Work Type', 'type': 'select', 'values': [ 'Government Job', 'Never Worked', 'Private', 'Self Employeed', 'Children' ]},
    {'name':'Residence_type', 'text': 'Residence Type', 'type': 'select', 'values': [ 'Rural', 'Urban' ]},
    {'name':'avg_glucose_level', 'text': 'Average Glucose Level (55.1 - 272)', 'type': 'number'},
    {'name':'bmi', 'text': 'BMI', 'type': 'number'},
    {'name':'smoking_status', 'text': 'Smoking Status', 'type': 'select', 'values': [ 'Unknown', 'Formely smoked', 'Never smoked', 'Smokes' ]},
]

@home_actions.route('/home',methods=['POST','GET'])
def index():
    if "user_id" not in session:
        return redirect(url_for('user_actions.login'))
    user = User.query.filter_by(id=session.get('user_id')).first()
    bmi = ''

    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        feet = float(request.form.get('feet'))
        inches = float(request.form.get('inches'))
        height = feet*12+inches
        bmi = (weight/height**2)*703
        return render_template('home.html', user=user,bmi=bmi,inputs=inputs)


    return render_template('home.html', inputs=inputs, user=user)


@home_actions.route('/')
def LandingPage():
    
    return render_template('landing_page.html')

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
    if float(avg_glucose_level) < 52.1:
        flash("Glucose Level Must Be More than 52.1")
        return redirect(url_for('home_actions.index'))
    date = datetime.now()
        
    p = predict_(gender, age, hypertension, heart_disease, ever_married,
                 work_type, Residence_type, avg_glucose_level, bmi, smoking_status)
    p = int(p)
    
    user = User.query.filter_by(id=session.get('user_id')).first()
    user.stroke = p
    db.session.commit()
    pridiction = PridictionsHistory(avg_gluscose_level=avg_glucose_level,bmi=bmi,stroke=p,date=date,user_id=session.get('user_id'))
    db.session.add(pridiction)
    db.session.commit()
    return redirect(url_for('home_actions.output'))

@home_actions.route('/perform')
def output():
    if "user_id" not in session:
        return redirect(url_for('user_actions.login'))
    user = User.query.filter_by(id=session.get('user_id')).first()
    return render_template('output.html', user=user)

@home_actions.route('/pridictions_history')
def Pridiction_History():
    if "user_id" not in session:
        return redirect(url_for('user_actions.login'))
    pridictions =PridictionsHistory.query.filter_by(user_id=session.get('user_id')).all()
    user = User.query.filter_by(id=session.get('user_id')).first()
    return render_template('pridictionshistory.html', pridictions=pridictions,user=user)