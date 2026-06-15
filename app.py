# app.py
# nickname generator v2 - todo: add colors later

import streamlit as st
from datetime import date

def make_nickname(name, dob):
    # split dob and get day month
    try:
        day = dob.day
        month = dob.month
    except:
        day = 12
        month = 2  # fallback lol

    # use first 3 letters of name
    name_part = name.replace(" ", "").lower()[:3]
    if len(name_part) < 3: 
        name_part = name_part + "x"*(3-len(name_part))
    
    # month based words cause it looks cool
    month_words = {
        1:"King",2:"Pookie",3:"Cute",4:"Moody",
        5:"Pookie",6:"Solar",7:"Baddass",8:"Bugaboo",
        9:"Beauty",10:"Ghost",11:"Heart-y",12:"Glitch"
    }
    
    # day decides the animal thing
    if day <= 10:
        end = "Rabbit"
    elif day <= 20:
        end = "Wolf" 
    else:
        end = "Lion"
    
    nickname = name_part.capitalize() + month_words.get(month,"Myst") + str(day) + end
    return nickname

st.title("Secret Nickname Generator 2026 ✨")
st.write("Get ur personalized aesthetic name based on ur real info")

name = st.text_input("Full name")
dob = st.date_input(
    "Date of birth",
    min_value=date(1980, 1, 1),
    max_value=date(2026, 12, 31),
    value=date(2005, 1, 1)
)
old_nick = st.text_input("Current nickname (optional)")

if st.button("Generate My New Name"):
    if name and dob:
        nick = make_nickname(name, dob)
        st.success(f"Your new name: **{nick}**")
        st.balloons()
        st.write("Screenshot this and flex it 😎")
        # print("debug:", name, dob) # remove later
    else:
        st.error("Bro fill name and DOB first")
