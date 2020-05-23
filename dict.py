import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def SearchAlgorithm(word):
        word=word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word,data.keys()))>0:
            print("Do you want to find %s instead!" % get_close_matches(word, data.keys())[0])
            decision = input("press Y for Yes or N for No:")
            if decision == "y" or decision == "Y":
                return data[get_close_matches(word, data.keys())[0]]
            elif decision == "n" or decision == "N":
                return ("You have entered wrong word!Check spelling again!")
            else:
                return ("You have entered wrong Input!Please enter just Y or N")
        else:
            return None

while(True):
    print("**********  DICTIONARY  **********")
    ch=input("Do you want to search a word(Y/N):")
    if ch=="Y" or ch=="y":
        userWord=input("Enter Word:")
        output=SearchAlgorithm(userWord)
        if output!=None:
            if type(output) == list:
                i=1
                for item in output:
                    print(i,item)
                    print()
                    i=i+1
            else:
                print(output)
        else:
            print("Word you have entered is not available in my dataset,sorry!")
    elif ch=="N" or ch=="n":
        break
    else:
        print("Please input N or Y!")
print("Thanks for joining me,hope you have a fun!")