import json
from difflib import get_close_matches

data = json.load(open("data.json"))

search = input("Enter string:")


def find(search):
    search = search.lower()

    if search in data.keys():
        return data[search]
    elif search.title() in data:
        return data[search.title()]
    elif search.upper() in data:
        return data[search.upper()]

    elif len(get_close_matches(search,data.keys())) > 0:
        yn = "X"
        while yn != "Y" or yn != "N":
            yn = input("Did you mean '%s' instead? Enter 'Y' if Yes, 'N' if No:" % get_close_matches(search, data.keys())[0])
            if yn == "Y":
                return data[get_close_matches(search, data.keys())[0]]
            elif yn == "N":
                return "Sorry the word entered does not exist, please double check it"

            print("Please enter Y or N")

    else:
        return "Sorry the word entered does not exist, please double check it"


out = find(search)
num = 1
if type(out) == list:
    for value in out:
        print("%d. %s" % (num, value))
        num = num + 1
else:
    print(out)

