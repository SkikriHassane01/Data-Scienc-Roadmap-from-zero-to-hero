# importing liberaries 
import streamlit as st 
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier 

# first let's create a title for our app
st.title('Classification Application')

# load the dataset from load_iris method
@st.cache_data
def load_data():
    data = load_iris()
    df = pd.DataFrame(data.data, columns = data.feature_names) 
    df['species'] = data.target # it will return the species number
    return df, data.target_names # it will return the species name and the dataframe

df, target_names = load_data()

# create the model 

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1],df['species'])

# create the sidebar
st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
    sepal_width = st.sidebar.slider('Sepal width', float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
    petal_length = st.sidebar.slider('Petal length', float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
    petal_width = st.sidebar.slider('Petal width', float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))
    data = {
        'sepal length (cm)': sepal_length,
        'sepal width (cm)': sepal_width,
        'petal length (cm)': petal_length,
        'petal width (cm)': petal_width
    }
    features = pd.DataFrame(data, index = [0])
    return features

input_df = user_input_features()

# the prediction 

prediction = model.predict(input_df) # it will return the species number
prediction_species = target_names[prediction[0]]# it will return the species name

st.write("## Prediction")

# display the input data with the prediction
st.write("The input data is :")
st.write(input_df)
st.write(f"The predicted species with is : {prediction_species}")

# display the probability of each species with the name of the species

st.write("The probability of each species is :")
data = model.predict_proba(input_df)
# change the column name to the species name
data = pd.DataFrame(data, columns = target_names)
st.write(data)