import random
def randomtext(): # return a random phrase
    text=["Veronica is hot","I like popsicles","Eat the rich",
        "Python is cool",
        "Drark is coming for you","I like pretty dresses"]
    rnd=random.randrange(0, len(text))
    return text[rnd]

# tests
# print(randomtext())