import streamlit
import io
import pandas
#page = streamlit.sidebar.radio("Choose a page", ["Page 1", "Page 2"])
streamlit.set_page_config(page_title='My App', layout='wide')
streamlit.title("The Best Company")

placeholder_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis leo vitae magna consequat 
euismod. Fusce id lacus quis augue tincidunt tincidunt. Phasellus at nisl sit amet nisi 
aliquet lacinia. Mauris vitae neque ac justo sagittis ullamcorper. Quisque et nunc id massa 
fringilla faucibus. Curabitur quis nisl ut erat sollicitudin rhoncus. Pellentesque habitant 
morbi tristique senectus et netus et malesuada fames ac turpis egestas.
"""
streamlit.write(placeholder_text)

streamlit.subheader('Our Team')

col1, col2, col3 = streamlit.columns(3)


# image
pf = pandas.read_csv('data.csv', sep =',')
with col1:
    for index, row in pf[:4].iterrows():
        streamlit.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        streamlit.write(row['role'])
        streamlit.image(f'images/{row["image"]}')
        streamlit.write("\n")

with col2:
    for index, row in pf[4:8].iterrows():
        streamlit.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        streamlit.write(row['role'])
        streamlit.image(f'images/{row["image"]}')
        streamlit.write("\n")

with col3:
    for index, row in pf[8:12].iterrows():
        streamlit.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        streamlit.write(row['role'])
        streamlit.image(f'images/{row["image"]}')
        streamlit.write("\n")


