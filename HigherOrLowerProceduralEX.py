import random

suits = ("spades","Hearts","Clubs","Diamonds")
ranks = ("Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King")

NCARDS = 8

def GetCard(deckListin):
    thisCard = deckListin.pop()
    return thisCard

def Shuffle(deckListin):
    deckListOut = deckListin.copy()
    random.shuffle(deckListOut)
    return deckListOut

print("Welcome to higher or lower")
print("Choose whether the next card to be shown will be higher or lower than current card")
print("Right answers = +20 points, and a wrong answer = -15")
print("Begin with 50 points")

startingDeckList = []
for suit in suits:
    for value, rank in enumerate(ranks)
        cardDict = {'rank':rank,'suit':suit, 'value':value+1}
        startingDeckList.append(cardDict)