#Import modules
import pandas
import streamlit as stream

#Open database 'team_info.csv' and separate columns split by a comma.
df = pandas.read_csv('team_info.csv', sep=',')
#Add header
stream.header('The best company')
#Adding dummy paragraph and printing it.
content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit' \
          ', sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' \
          ' Proin tortor purus platea sit eu id nisi litora libero.' \
          'Neque vulputate consequat ac amet augue blandit maximus' \
          ' aliquet congue. Pharetra vestibulum posuere ornare ' \
          'faucibus fusce dictumst orci aenean eu facilisis ut' \
          ' volutpat commodo senectus purus himenaeos famesprimis convallis nisi.'
stream.write(content)
#Add subheader 'Our Team'
stream.subheader('Our team')
#Create columns.
col1, col2, col3 = stream.columns(3)
# Add first 4 team members in leftmost column.
with col1:
    for index, rows in df[:4].iterrows():
        stream.subheader((f"{rows['first name']} {rows['last name']}"))
        stream.write(rows['role'])
        stream.image(f"team_portraits/{rows['image']}")
# Add next 4 team members in middle column.
with col2:
    for index, rows in df[4:8].iterrows():
        stream.subheader((f"{rows['first name']} {rows['last name']}"))
        stream.write(rows['role'])
        stream.image(f"team_portraits/{rows['image']}")

# Add last 4 teammembers in rightmost column.
with col3:
    for index, rows in df[8:12].iterrows():
        stream.subheader((f"{rows['first name']} {rows['last name']}"))
        stream.write(rows['role'])
        stream.image(f"team_portraits/{rows['image']}")
