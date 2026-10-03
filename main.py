"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.

Authors: Keston, Rayan, Jeromie, Zay Ya
Date: Oct/2/2026
Subject: Group Project (Intro to comp sci)
Objective: Create a blackjack game.
"""

# Slice 1: Deck Creation & Manipulation (Rayan)

import random

deck = []
deckValues = { "2" : 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
               "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11 } 
dealerHand = []
playerHand = []

# Initializes the deck of cards to starting state and resets hands to empty
def intializeDeck(deck, dealerH, playerH):
    # empties deck first
    deck.clear()

    # adds numbered cards to deck
    for i in range(2, 11):
        deck.append(str(i) + " spades")
        deck.append(str(i) + " clubs")
        deck.append(str(i) + " diamonds")
        deck.append(str(i) + " hearts")
    
    # adds face cards to deck
    faceCards = ["J", "Q", "K", "A"]
    for card in faceCards:
        deck.append(card + " spades")
        deck.append(card + " clubs")
        deck.append(card + " diamonds")
        deck.append(card + " hearts")

    # empties dealer and player hands
    dealerH.clear()
    playerH.clear()

    return deck, dealerH, playerH


# takes random card from deck and adds to either dealer or player hand
def dealCard(deck, dealerH, playerH, currentP):
    # takes out a random card from the deck
    randomCard = deck.pop(random.randrange(len(deck)))

    # based on who the current player is, adds it to their respective hand
    if currentP == 1:
        dealerH.append(randomCard)
    else :
        playerH.append(randomCard)

    return randomCard

# takes randomCard and current player and outputs what card has been added and 
def printCardInfo(randomCard, currentP):
    # modifies print message based on current player
    faceCards = ["J", "Q", "K", "A"]
    if currentP == 1:
        if randomCard[0] not in faceCards:
            if randomCard[0] == "1":
                print("Dealer has: 10 of " + randomCard[3:])
            else:
                print("Dealer has: " + randomCard[0] + " of " + randomCard[2:])
        elif randomCard[0] == "J":
            print("Dealer has: Jack of " + randomCard[2:])
        elif randomCard[0] == "Q":
            print("Dealer has: Queen of " + randomCard[2:])
        elif randomCard[0] == "K":
            print("Dealer has: King of " + randomCard[2:])
        elif randomCard[0] == "A":
            print("Dealer has: Ace of " + randomCard[2:])
    else:
        if randomCard[0] not in faceCards:
            if randomCard[0] == "1":
                print("Player has: 10 of " + randomCard[3:])
            else:
                print("Player has: " + randomCard[0] + " of " + randomCard[2:])
        elif randomCard[0] == "J":
            print("Player has: Jack of " + randomCard[2:])
        elif randomCard[0] == "Q":
            print("Player has: Queen of " + randomCard[2:])
        elif randomCard[0] == "K":
            print("Player has: King of " + randomCard[2:])
        elif randomCard[0] == "A":
            print("Player has: Ace of " + randomCard[2:])        

def main():
    print("CSCI 1030U group project - not built yet.")
    print("Replace main() with your core loop. See MILESTONES.md for what is due when.")


    print("Blackjack Introduction message\n")

    #tests for deck creation and manipulation
    #print(deck)
    #print(dealerHand)
    #print(playerHand)
    #print("")

    intializeDeck(deck, dealerHand, playerHand)
    #print(deck)
    #print(dealerHand)
    #print(playerHand)
    #print("")


    player = 1
    printCardInfo(dealCard(deck, dealerHand, playerHand, player), player)
    player = 2
    printCardInfo(dealCard(deck, dealerHand, playerHand, player), player)

    

    #dealCard(deck, dealerHand, playerHand)

    # Create variables and functions above the gameplay loop
    # Cards in deck, no. of players, turn tracker, etc

    # Feel free to rearrange anything!

    # Upper section here is a good place to handle things like a menu, alternative is having a menu at the below __name__ code.
    # I guess technically we should be using the TUI from our lecture?



    # Main gameplay loop (use break; to exit loop after x amount of turns)
    while (True): 
        break;
        # Set up board
        # Gambling? In this economy? (Players bet a value) (maybe)
        # Distribution of cards: 2 per player, 2 to dealer (1 hidden depending on which rules we're going by)

        # If dealer has a god pull and does an ace + 10, dealer immediately triggers win condition and the game is reset


        # Begin gameplay loop

        # Player's turns

        # Print board
        # List of actions for player to take
            # Hit, pass, split(if both cards have the same value (e.g. both are 5, king + queen)), forfeit, (double down)

            # Update player cards and score
                # take care how to handle ace (1 or 11), we can show smth like [6/16] if they have a+5, then if they get a 6, collapse back to [12]
            # Update player status

            # Idk how we're going to handle splits right now
            # ig we can get a seperate boolean for if a player has a split deck and then repeat the player turn?
            # Unless we want to store player data in a dictionary similar to how regular games do it
            # See how, we work on a functional base game first

        # Check win condition, if all players bust then dealer wins


        # Dealer's turn
        # Dealer draws cards until at least 17
        # If dealer busts, remaining players win
        
        # Calculate changes in scores of players

        # Game repeats until x turns, can be handled with a simple if (turns == x): break; since it will repeat by itself
        # Maybe specify turns before game starts? We can have something like a settings menu before the start of the game at later milestones.
        pass



    # This section is outside the while loop, runs after the game has ended.

    # Print final scores of the game (money won/lost, rounds won/lost?)



    pass

if __name__ == '__main__':
    main()
