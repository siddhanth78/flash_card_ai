import streamlit as st
import json

with open("cards.json", "r", encoding="utf-8") as file:
    cards_json = json.load(file)

def check_ans(op, ans):
    if op[0] == ans:
        st.success(f"Nice! {cards_json['1']['explanation']}")
    else:
        st.error(f"Nope! The correct answer is {ans}! {cards_json['1']['explanation']}")

def go_back():
    pass

def go_fwd():
    pass

st.title("QnA")
opt = st.radio(f"1. {cards_json['1']['question']}", cards_json['1']['options'])

left, center, right = st.columns(3)
left.button("Prev", on_click=go_back)
center.button("Submit", on_click=check_ans, args=(opt, cards_json['1']['answer']), type="primary")
right.button("Next", on_click=go_fwd)
