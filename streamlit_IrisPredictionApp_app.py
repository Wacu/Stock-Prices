import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


st.write("""
# An APP to predict the type of Iris flower 

Welcome to yet another App. Enjoy!
""")
st.sidebar.header("User Input Parameters")

#Define a function to take in user parameters and create a dataframe

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length',3.4,8.0,4.2)
    sepal_width = st.sidebar.slider('Sepal Width',1.5,5.2,2.7)
    petal_length =st.sidebar.slider('Petal Length',1.0,7.7,2.5)
    petal_width = st.sidebar.slider('Petal Width',0.2,3.4,1.2)
    data = {'sepal_length' : sepal_length,
            'sepal_width' : sepal_width,
            'petal_length' : petal_length,
            'petal_width' : petal_width}
    features = pd.DataFrame(data,index=[0])
    return features 

df = user_input_features()

#generate a table to view user input
st.subheader('User Input Paramaters')
st.write(df)

#Prepare data for modelling
# load the iris dataset
iris = datasets.load_iris()
X = iris.data    #data was defined above
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)

prediction = clf.predict(df)
prediction_prob = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_prob)
