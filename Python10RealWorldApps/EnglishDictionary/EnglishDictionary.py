import json
from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("data.json"))

#returns a dictionary of 'word':'definitions'
def translate(w):
    w = w.lower()
    result = {}
    if w in data:
        result[w] = data[w]
        return result
    elif len(get_close_matches(w, data.keys())) > 0:
        close_matches = get_close_matches(w, data.keys(), n=10)
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % close_matches[0])
        if yn == "Y":
            return data[close_matches[0]]
        else:
            return close_matches
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == dict:
    for key in output.keys():
        for word_def in output[key]:
            print(key,": ", word_def)
else:
    print(output)

