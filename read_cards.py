import ast
import json

def get_cards(txt_file):
    with open(txt_file, "r") as file:
        data = file.read()
    cards = data.split("---")
    return cards

def process_cards(card_list):
    card_dict = {}
    for cl in card_list:
        c_l = cl.split("\n")
        c_l_clean = [c_ for c_ in c_l if c_!=""]
        if c_l_clean:
            c_l_clean.sort()
            c_l_clean[-1] = c_l_clean[-1][:-1]
            if c_l_clean[:-1]:
                card_dict[c_l_clean[-1]] = c_l_clean[:-1]
                for i in range(len(card_dict[c_l_clean[-1]])):
                    card_dict[c_l_clean[-1]][i] = card_dict[c_l_clean[-1]][i][:-1]

    n = 1
    all_cards = {}

    for cd in card_dict:
        card_dict[cd][-1] = ast.literal_eval(card_dict[cd][-1].strip("options: "))
        cd_str = ast.literal_eval(cd.strip("question: "))
        card_dict[cd][0] = ast.literal_eval(card_dict[cd][0].strip("answer: "))
        card_dict[cd][1] = card_dict[cd][1].strip("explanation: ")[1:]
        print("----------")
        print(cd_str)
        print(card_dict[cd][-1])
        print(card_dict[cd][0])
        print(card_dict[cd][1])
        print("----------\n")

        all_cards[n] = {"question": cd_str, "options": card_dict[cd][-1], "answer": card_dict[cd][0], "explanation": card_dict[cd][1]}
        n += 1

    return all_cards

cd_ = process_cards(get_cards("cards.txt"))
with open("cards.json", "w", encoding="utf-8") as file:
    json.dump(cd_, file, indent=4)
print("Cards stored")
