import streamlit as st
import joblib 

def map_yes_no(valor_codificado):
    return "Yes" if valor_codificado == 1 else "No"


svm_model = joblib.load('ML_Mental_Disorder.pkl')

st.title('Mental Disorder:skull:')
Mood_Swing=st.radio('Mood Swing', [0, 1], format_func=map_yes_no)
Optimism=st.select_slider('Optimisim',['on a scale 1-10',1,2,3,4,5,6,7,8,9,10])   
Sexual_Activity=st.select_slider('Sexual Activity',['on a scale 1-10',1,2,3,4,5,6,7,8,9,10])   
Suicidal_thoughts=st.radio('Suicidal thoughts', [0, 1], format_func=map_yes_no)
Aggresive_response=st.radio('Aggressive Response', [0, 1], format_func=map_yes_no)
Euphoric_Usually = st.checkbox('Euphoric_Usually')
Euphoric_Seldom = st.checkbox('Euphoric_Seldom')
Sadness_Sometimes = st.checkbox('Sadness_Sometimes')
Sadness_Usually = st.checkbox('Sadness_Usually')

if st.button('Predict'):
    input_data = [[Mood_Swing, Optimism, Sexual_Activity, Suicidal_thoughts, Aggresive_response, Euphoric_Usually, Euphoric_Seldom, Sadness_Sometimes, Sadness_Usually]]
    prediction = svm_model.predict(input_data)
    st.write('Mental Disorder: ', prediction)
    


    





