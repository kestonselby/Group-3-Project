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

# Moved main below, configuring game code as one function so we can have a menu that doesnt run through the game code.

def playgame():

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
    
    # Maybe specify turns before game starts? We can have something like a settings menu before the start of the game at later milestones.

    # Main gameplay loop (use break; to exit loop after x amount of turns)
    while(game):
        # Handle rounds
        current_round+=1 # start current_round from 0)
        if (current_round > max_rounds):
            # break out of loop and proceed to final score
            pass

        # Set up board
        intializeDeck(deck, dealerH, playerH)
        
        # Gambling? In this economy? (Players bet a value) (maybe)
        # Distribution of cards: 2 per player, 2 to dealer (1 hidden depending on which rules we're going by)

        for i in range(playercount+1): # playercount set to 1 until we finalise code structure
            dealCard(deck, dealerH, playerH, i)
            dealCard(deck, dealerH, playerH, i)

        # Calculate initial score (remember ace can be 1 or 11)
        calculateScore()

        # If dealer has a god pull and does an ace + 10, dealer immediately triggers win condition and the game is reset
        if (dealerscore == 21):
            print("Bad luck lmao")
            break;

        # Begin gameplay loop

        # Player's turns
        for playernumber in range(playercount):

            # Print board
            printCardInfo(randomCard, currentP)

            # if player [n] has a 21
                # set player[n] victory condition
                # break;

            # List of actions for player to take
            print("1. Hit | 2. Pass | 3. Split | 4. Forfeit") # 5. Double down

            # Hit, pass, split(if both cards have the same value (e.g. both are 5, king + queen)), forfeit, (double down)
            while True:
                decision = input("Enter choice: ")

                match decision:
                    case "1":
                        # add card to hand
                        printCardInfo(randomCard, currentP)

                        # calculate score

                        if ( score(playernumber) >= 21 ): 
                            # player has won/bust, move to next player
                            break;

                        # print board again
                        # dont break here so they can hit more cards.

                    case "2":
                        break;
                    
                    case "3":
                        # some special handle split case idk
                        pass
                        break;

                    case "4":
                        # Lose their bet/game
                        break;
                    
                    case _:
                        print("Invalid entry.")
                        # dont break here so they loop until they enter a valid option

            # Update player cards and score
                # take care how to handle ace (1 or 11), we can show smth like [6/16] if they have a+5, then if they get a 6, collapse back to [12]

            # Update player status

            # Idk how we're going to handle splits right now
            # ig we can get a seperate boolean for if a player has a split deck and then repeat the player turn?
            # Unless we want to store player data in a dictionary similar to how regular games do it
            # See how, we work on a functional base game first

        # if there are still players who havent bust or gotten blackjack:
            
            # Dealer's turn
            # Dealer draws cards until at least 17
            # If dealer busts, remaining players win
            
        # Calculate changes in scores of players
            # If dealer manages to get blackjack:
                # If player also has blackjack:
                    # player ties, does not win or lose.
                # remainng players lose
            
            # if dealer does not have blackjack:
                # if player has blackjack, they win (earns bet + 1.5x of their bet)
                # elseif player is higher than dealer, they win (earns bet + 1x of their bet)
                # else, player loses

        pass
        # Loop until broken by turn handler at the top



    # This section is outside the while loop, runs after the game has ended.

    # Print final scores of the game (money won/lost, rounds won/lost?)

    # Wait for input before moving back to menu.

    pass

def main():
    print("CSCI 1030U group project - not built yet.")
    print("Replace main() with your core loop. See MILESTONES.md for what is due when.")

    print("Blackjack Introduction message\n")

    while True:
        # clear screen?

        # Display menu options
        print("1. Start Game")
        print("2. Settings")
        print("3. How To Play")
        print("4. Option 4")
        print("5. Exit")

        # Get user choice
        print()
        choice = input("Enter your choice: ")

        # Call the corresponding function based on user choice
        match choice:
            case "1":
                playgame()
            case "2":
                settings_menu()
            case "3":
                how_to_play()
            case "4":
                print("Option 4")
            case "5":
                break
            case _:
                print("Invalid entry.")

    print("Code has ended.")

#How to play function menu, basically just a text menu that explains how to play blackjack, 
# and then returns to the main menu when the user presses 1.
def how_to_play():
    while True:
        print("\n========== HOW TO PLAY BLACKJACK ==========")
        print("The goal of Blackjack is to get as close to 21 as possible")
        print("without going over 21.\n")
        print("Card Values:")
        print("- Number cards (2-10) are worth their number.")
        print("- J, Q, and K are worth 10.")
        print("- An Ace (A) is worth 11 or 1, depending on what is better")
        print("  for your hand.\n")
        print("How the game works:")
        print("1. The player and dealer are each dealt two cards.")
        print("2. The player chooses what to do with their hand.")
        print("3. Hit - Draw another card.")
        print("4. Pass - Keep your current hand and end your turn.")
        print("5. Split - Split your hand when the two cards have the same")
        print("   value.")
        print("6. Forfeit - Give up the hand.\n")
        print("Winning:")
        print("- Getting exactly 21 is called Blackjack.")
        print("- If your hand goes over 21, you bust and lose.")
        print("- If the dealer goes over 21, the remaining player wins.")
        print("- If your hand is closer to 21 than the dealer's, you win.")
        print("- If you and the dealer have the same score, it is a tie.\n")
        print("===========================================")
        print("1. Back to Main Menu\n")

        howToPlayChoice = input("Enter your choice: ")

        if howToPlayChoice == "1":
            break
        else:
            print("Invalid entry. Press 2 to return to the main menu.")          
                
if __name__ == '__main__':
    main()
