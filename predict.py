import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, accuracy_score


def ml(a, b, c):
    df = pd.read_csv("ds/Dataset1.csv")
    df = df[['Present Health', 'Present Mental Health', 'Drinking and Smoking', 'Psychiatrist consulted']]
    label_encoder = LabelEncoder()
    df['Present Health'] = label_encoder.fit_transform(df['Present Health'])
    df['Present Mental Health'] = label_encoder.fit_transform(df['Present Mental Health'])
    df['Drinking and Smoking'] = label_encoder.fit_transform(df['Drinking and Smoking'])
    df['Psychiatrist consulted'] = label_encoder.fit_transform(df['Psychiatrist consulted'])

    ## Assigning independent and dependent variables to x & y respectively
    x = df[['Present Health', 'Present Mental Health', 'Drinking and Smoking']]  # independent variables
    y = df[['Psychiatrist consulted']]  # dependent variable
    list_training_error = []
    list_testing_error = []

    ## Splitting the data into Train and test data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)

    ## Creating a linear regression model
    mlr = linear_model.LinearRegression()

    ## Training the model with traing data
    mlr.fit(x_train.values, y_train.values)

    ## Predicting the model with test data
    # print(x_test)
    pred = mlr.predict(x_test.values)


    if a != '' or b != '' or c != '':
        global p_h
        p_h = float(a)

        global m_h
        m_h = float(b)

        global s_n_d
        s_n_d = float(c)

        x = float(mlr.predict([[p_h, m_h, s_n_d]]))
        if x <= 0.5:
            y = 0
        elif 0.5 <= x <= 1:
            y = 1
        else:
            y = 2

        Prediction_result = str(label_encoder.inverse_transform([y])[0])
        return Prediction_result
    else:
        return str("Error")
