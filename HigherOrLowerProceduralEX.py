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
print("Right answers = +20 points, wrong answer = -15")
print("Begin with 50 points")

startingDeckList = []
for suit in suits:
    for value, rank in enumerate(ranks):
        cardDict = {'rank':rank,'suit':suit, 'value':value+1}
        startingDeckList.append(cardDict)
score = 50

while True:
    print()
    gameDeckList = Shuffle(startingDeckList)
    currentCardDict = GetCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print(f"Starting card is: {currentCardRank} of {currentCardSuit}\n")

    for cardNumber in range(0,NCARDS):
        answer = input(f"Will the next card be higher or lower than {currentCardRank} of {currentCardSuit}? (enter h or l)").casefold()
        nextCardDict = GetCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print(f"Next card is: {nextCardRank} of {nextCardSuit}")

        if answer == "h":
            if nextCardValue > currentCardValue:
                print("Correct, It Was Higher! +20")
                score += 20
            else:
                print("Incorrect, It Was Lower -15")
                score -= 15

        elif answer == "l":
            if nextCardValue < currentCardValue:
                print("Correct, It Was Lower! +20")
                score += 20
            else:
                print("Incorrect, It Was Higher -15")
                score -= 15

        print(f"Your Score Is:{score}\n")
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit
    goAgain = input("To player again press 'ENTER' or 'q' to quit")
    if goAgain == 'q':
        break
