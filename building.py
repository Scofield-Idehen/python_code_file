import json
from difflib import get_close_matches

while True:

    data = json.load(open('data.json'))


    def new_project(f):
        f = f.lower()
        if f in data:
            return data[f]
        elif len(get_close_matches(f, data.keys())) > 0:
            user_answer = input(f"Do you mean {get_close_matches(f, data.keys())[0]}?:if Yes Enter 'Y' or 'N: " )
            if user_answer.upper() == "Y":
                return f'{data[get_close_matches(f, data.keys())[0]]}'
            elif user_answer.upper() == 'N':
                return f'{write} is not in this dictionary, please check again: '
            else:
                return 'Unknow term!!!'

        else:
            return f'this {write} not found'

    write = input("Input your word: ")
    news = new_project(write)
    if type(news) == list:
        for i in news:
            print(i)
    else:
        print(news)