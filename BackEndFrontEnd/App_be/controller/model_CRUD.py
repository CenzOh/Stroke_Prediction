from flask import Blueprint
from flask import request
from flask import jsonify
from App_be.model_.test_model import predict_
model_crud = Blueprint('model_crud', __name__)


@model_crud.route('/app/model', methods=['GET'])
def get_user():
    req_data = request.json
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

    response = {
        "res": int(p)
    }
    return jsonify(response)


"""
{
"gender": 1,
"age":67 ,
"hypertension":0,
"heart_disease":1 ,
"ever_married": 1,
"work_type": 0,
"Residence_type":1,
"avg_glucose_level":228.69,
"bmi": 36.6,
"smoking_status": 1
}

"""
