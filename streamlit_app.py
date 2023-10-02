import streamlit
import pandas


streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

## Lesson 3: Importing Pandas
## Read the CSV from the S3 bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
## Display the CSV in Streamlit
streamlit.dataframe(my_fruit_list)

## Lesson 3: Add a Streamlit Multiselect Picker
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

