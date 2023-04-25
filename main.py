import pandas
import streamlit as stream

df = pandas.read_csv('team_info.csv', sep=',')
stream.header('The best company')
content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit' \
          ', sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' \
          ' Proin tortor purus platea sit eu id nisi litora libero.' \
          'Neque vulputate consequat ac amet augue blandit maximus' \
          ' aliquet congue. Pharetra vestibulum posuere ornare ' \
          'faucibus fusce dictumst orci aenean eu facilisis ut' \
          ' volutpat commodo senectus purus himenaeos famesprimis convallis nisi.'
stream.write(content)
stream.subheader('Our team')
col1, col2, col3 = stream.columns(3)

with col1:
    for index, rows in df[:4].iterrows():
        stream.subheader((f"{rows['first name']} {rows['last name']}"))
        stream.write(rows['role'])
        stream.image(f"team_portraits/{rows['image']}")

with col2:
    for index, rows in df[4:8].iterrows():
        stream.subheader((f"{rows['first name']} {rows['last name']}"))
        stream.write(rows['role'])
        stream.image(f"team_portraits/{rows['image']}")

with col3:
    for index, rows in df[8:12].iterrows():
        stream.subheader((f"{rows['first name']} {rows['last name']}"))
        stream.write(rows['role'])
        stream.image(f"team_portraits/{rows['image']}")

