from joblib import dump, load
import pickle
import pandas as pd

scaler = load('data_model/scaler.bin')
model = pickle.load(open("data_model/finalized_model.sav", 'rb'))

def predict_(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status):

    one_record = {
        "gender": [gender],
        "age": [age],
        "hypertension": [hypertension],
        "heart_disease": [heart_disease],
        "ever_married": [ever_married],
        "work_type": [work_type],
        "Residence_type": [Residence_type],
        "avg_glucose_level": [avg_glucose_level],
        "bmi": [bmi],
        "smoking_status": [smoking_status],

    }

    one_record_dataframe = pd.DataFrame(one_record)
    num_cols = ["gender", "age", "hypertension", "heart_disease", "ever_married",
                "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status"]
    one_record_dataframe[num_cols] = scaler.transform(
        one_record_dataframe[num_cols])
    pred = model.predict(one_record_dataframe)
    print(pred)
    return pred[0]