import streamlit as st
import json

with open("cards.json", "r", encoding="utf-8") as file:
    cards_json = json.load(file)

if 'q' not in st.session_state:
    st.session_state.q = 1

curr = str(st.session_state.q)

def check_ans(op, ans):
    if op[0] == ans:
        st.success(f"Nice! {cards_json[curr]['explanation']}")
    else:
        st.error(f"Nope! The correct answer is {ans}! {cards_json[curr]['explanation']}")

def go_back():
    st.session_state.q -= 1
    if st.session_state.q < 1:
        st.session_state.q = 1

def go_fwd():
    st.session_state.q += 1
    if st.session_state.q > len(cards_json):
        st.session_state.q = len(cards_json)

def display():
    st.title(f"Question {st.session_state.q}")
    curr = str(st.session_state.q)
    
    opt = st.radio(
        f"{st.session_state.q}. {cards_json[curr]['question']}", 
        cards_json[curr]['options'],
        key=f"radio_{curr}")

    left, center, right = st.columns(3)
    left.button("Prev", on_click=go_back)
    center.button("Submit", on_click=check_ans, args=(opt, cards_json[curr]['answer']), type="primary")
    right.button("Next", on_click=go_fwd)

display()
