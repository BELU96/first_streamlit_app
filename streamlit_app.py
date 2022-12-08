import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('MENU')
streamlit.text('Smoked Ribs')
streamlit.text('Italian Ribs')
streamlit.text('Pulled Pork')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
