# app.py
# nickname generator v2 - todo: add colors later

import streamlit as st

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
        1:"Frost",2:"Cloud",3:"Storm",4:"Blaze",
        5:"Drift",6:"Solar",7:"Tidal",8:"Astro",
        9:"Cyber",10:"Ghost",11:"Nova",12:"Glitch"
    }
    
    # day decides the animal thing
    if day <= 10:
        end = "Fox"
    elif day <= 20:
        end = "Wolf" 
    else:
        end = "Bear"
    
    nickname = name_part.capitalize() + month_words.get(month,"Myst") + str(day) + end
    return nickname

st.title("Secret Nickname Generator 2026 ✨")
st.write("Get ur personalized aesthetic name based on ur real info")

name = st.text_input("Full name")
dob = st.date_input("Date of birth", value=None) 
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
