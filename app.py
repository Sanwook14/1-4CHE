import streamlit as st

st.title("CHE Calculator for 1~4")

Screentime = 100
Extime = 200
Sleeptime = 300

user_1 = st.number_input("Write your amount of time you are on any type of device:", value=0, key="u1")
user_2 = st.number_input("Write your amount of time you exercise:", value=0, key="u2")
user_3 = st.number_input("Write your amount of time you sleep:", value=0, key="u3")

st.divider()

diff_1 = user_1 - Screentime
diff_2 = user_2 - Extime
diff_3 = user_3 - Sleeptime

status_1 = f"Over (+{diff_1})" if diff_1 > 0 else (f"Under ({diff_1})" if diff_1 < 0 else "Perfect (0)")
status_2 = f"Over (+{diff_2})" if diff_2 > 0 else (f"Under ({diff_2})" if diff_2 < 0 else "Perfect (0)")
status_3 = f"Over (+{diff_3})" if diff_3 > 0 else (f"Under ({diff_3})" if diff_3 < 0 else "Perfect (0)")

st.subheader("Results")
st.text(f"You are this much away from your Screentime expectations: {status_1}")
st.text(f"You are this much away from your Exercise time expectations: {status_2}")
st.text(f"You are this much away from your Sleeptime expectations: {status_3}")

