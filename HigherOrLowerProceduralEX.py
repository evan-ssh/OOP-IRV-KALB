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