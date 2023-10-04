import streamlit
import pandas
import requests
import snowflake.connector


streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

## Lesson 3: Importing Pandas
## Read the CSV from the S3 bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
## Display the CSV in Streamlit
streamlit.dataframe(my_fruit_list)

## Lesson 3: Add a Streamlit Multiselect Picker
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table
streamlit.dataframe(fruits_to_show)

# New Section to display fruityvice api response
streamlit.header('Fruityvice Fruice Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# GET from the fruityvice API
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Normalize JSON response into a table
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Write it to the page
streamlit.dataframe(fruityvice_normalized)

# Snowflake Connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()

my_cur2 = my_cnx.cursor()
my_cur2.execute("select * from PC_RIVERY_DB.PUBLIC.FRUITYVICE")
my_data_row2 = my_cur2.fetchone()


# my_cur = my_cnx.cursor()
#my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
#my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
streamlit.text(my_data_row2)
