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
        close_matches = get_close_matches(w, data.keys(), n=5)
        print("Close matches: ",close_matches)
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % close_matches[0])
        if yn.lower() == "y":
            result[close_matches[0]] = data[close_matches[0]]
            return result
        else:
            print("\nReturning 5 closest matches...")
            for match in close_matches:
                result[match] = data[match]
            return result
    else:
        return "The word doesn't exist."

word = input("Enter word for lookup: ")
output = translate(word)
if type(output) == dict:
    for key in output.keys():
        for word_def in output[key]:
            print(key,": ", word_def)
        print("")
else:
    print(output)

