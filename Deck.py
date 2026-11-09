import random, json

class Deck:
    # class attributes
    CARD_VALUES = { "2" : 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                   "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11 }

    SUITS = ["spades", "clubs", "diamonds", "hearts"]

    # constructor for deck class
    def __init__(self):
        # deck initialization
        self.deck = []
        self.initializeDeck()
    
    # initializes the deck of cards to starting state
    def initializeDeck(self):
        # adds numbered cards to deck
        for i in range(2, 11):
            self.deck.append(str(i) + " spades")
            self.deck.append(str(i) + " clubs")
            self.deck.append(str(i) + " diamonds")
            self.deck.append(str(i) + " hearts")
    
        # adds face cards to deck
        for card in ["J", "Q", "K", "A"]:
            self.deck.append(card + " spades")
            self.deck.append(card + " clubs")
            self.deck.append(card + " diamonds")
            self.deck.append(card + " hearts")

    # reset and reinitialize the deck
    def resetDeck(self):
        # clears deck first then runs initializeDeck()
        self.deck.clear()
        self.initializeDeck()

    # randomly deal a card from the deck 
    def dealCard(self):
        # pops and returns a random card
        randomCard = self.deck.pop(random.randrange(len(self.deck)))
        return randomCard  

    ### above is refactored code from m1 for OOP
    
    # saveDeck - implementation for file i/o
    def saveDeck(self, gameNum):
        try:
            with open("saveData.json", "r") as readFile:
                saves = json.load(readFile)
        except (FileNotFoundError, json.JSONDecodeError):
            saves = {}

        saves["save"+str(gameNum)] = self.deck
        with open("saveData.json", "w") as writeFile:
            json.dump(saves, writeFile, indent=4)
    
    # loadDeck - implementation 2 for file i/o, makes use of validateDeck
    def loadDeck(self, gameNum):
        try:
            with open("saveData.json", "r") as readFile:
                saves = json.load(readFile)
            
            key = 'save'+str(gameNum)
            if key in saves:
                loadedDeck = saves[key]
                if self.validateDeck(loadedDeck, len(loadedDeck)-1):
                    self.deck = loadedDeck
                else:
                    print("Deck is corrupted.")
            else:
                print("Save data not found.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("File could not be read or does not exist")
    
    # validateDeck - implementation for recursion (redundant mainly here for recursion principle proof)
    def validateDeck(self, saveDeck, index):
        # base case
        if index < 0: 
            return True

        # holds card info 
        current_card = saveDeck[index]
        card_elements = current_card.split()

        # checks card has exactly 2 parts, protects against manual json alterations 
        if len(card_elements) < 2 or len(card_elements) > 2:
            return False

        # checks card info and makes recursive call if checks pass
        if card_elements[0] in self.CARD_VALUES and card_elements[1] in self.SUITS: 
            return self.validateDeck(saveDeck, index-1)
        else:
            return False    

    # (zay ya) added popular shuffle to fulfill recursion requirement
    def fisherYates_shuffle(self, deck, index=None):
        # shuffle index starts at the end of the list
        if index is None:
            index = len(deck) - 1
            
        # base case: index reaches front of list
        if index == 0:
            return deck
            
        # select random index to swap with
        random_index = random.randint(0, index)
        
        # swap cards
        temp = deck[index]
        deck[index] = deck[random_index]
        deck[random_index] = temp

        # print(f"{deck}\n")
        
        # go through the deck recursively as index lowers to 0
        return self.fisherYates_shuffle(deck, index - 1)

# if __name__ == "__main__":
#     deck = Deck()
#     shuffled = deck.fisherYates_shuffle(deck.deck)
