import json

data = json.load(open("data.json"))
from difflib import get_close_matches

def translate(w):
    #w =w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return f"Did you mean {get_close_matches(w, data.keys())[0]}"
    else:
        return f"{word} is not an english word, check your spelling!!!"


word = input("Enter Word: ")
ab = translate(word.lower())
print(ab)
