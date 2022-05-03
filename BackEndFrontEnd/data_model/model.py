import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
from joblib import dump, load
# Importing the dataset
dataset = pd.read_csv("dataset.csv")

# Encoding categorical features
objList = dataset.select_dtypes(include="object").columns
le = LabelEncoder()
for feat in objList:
    dataset[feat] = le.fit_transform(dataset[feat].astype(str))

# save the encoder into a file
dump(le, 'encoder.joblib')

# Dealing with missing values in 'bmi' column
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, -2:])
X[:, -2:] = imputer.transform(X[:, -2:])

# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)

#Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# save the scaler in a file
dump(sc, 'scaler.bin', compress=True)



#Training the Random Forest Classification model on the Training set


classifier = RandomForestClassifier(n_estimators = 25, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)


# save the mdoel into a file
filename = 'finalized_model.sav'
pickle.dump(classifier, open(filename, 'wb'))


"""
id               
gender           
age              
hypertension     
heart_disease    
ever_married     
work_type        
Residence_type   
avg_glucose_level
bmi              
smoking_status   
stroke           
"""
