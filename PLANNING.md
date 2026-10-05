# BlackJack Planning

## Milestone 1 - Core Prototype

### Deck Creation and Manipulation (Rayan)

**Purpose:**  
In charge of initializing/resetting the deck of cards at the start of each round, drawing and dealing cards to player and dealer, printing out respective cards info to console.

**Data:**  
- List for deck of cards
- Dictionary holding value of each rank of card 2-ACE
- List for Dealer hand
- List for Player hand

**Functions / Responsibilities:**  
1. initializeDeck - clears all lists and resets to starting point, full deck, empty hands
2. dealCard - takes random card from deck and adds to respective players hand
3. printCardInfo - prints out card info when called

**Process:**  
1. Deck and hands are initialized using initializeDeck at the start of each round
2. draw/dealCard is called to take a card from the deck and put it in either the player's or dealer's hand
3. printCardInfo will output the card drawn and to who the card belongs to

### Score Calculation and Show players hand (Jerome)

**Purpose:**
In charge of calculating the score of a hand, including deciding whether eachAce counts as a 1 or 11, and printing a hand's cards and total to the console so the player can see them.

**Data:**
- List for the hand being scored (the Dealer hand or the Player hand)
- Variable for the running score total
- Variable counting the number of Aces in the hand

**Function / Responsibilities:**
1. calculateScore - adds up the value of every card in a hand and returns the total, lowering Aces from 11 to 1 when the hand goes over 21
2. showHand - prints whose hadn it is, each card in the hand, and the hand's total score

**Process:**
1. calculateScore starts the score and Ace counter at 0
2. it loops through each card in the hand, splits the card text to get the rank(for example "K hearts" becomes "K"), and adds that rank's value from deckValues to the score
3. Each time an Ace is found, the Ace counter goes up by 1
4. After all cards are added, while the csore is over 21 and there is still an Ace counted as 11, it subtracts 10 (changing that Ace to 1) and lowers the Ace counter by 1
5. The final score is returned so other parts of the game (player turn, dealer turn, deciding the winner) can use it
6. showHand prints the name and each card, then calls calculateScore to print the total score

### Gameplay structure (Zay Ya)

**Purpose:**
In charge of the central gameplay logic and flow of the code, 

**Data:**
- Deck (From others' code)
- Dealer and player hands (From others' code)
- Int for current round
- Int for total rounds
- Int for playercount
- List of int for score (With assistance from others functions)

**Function / Responsibilities:**
1. playgame - Begins the game of blackjack. Sets up board, Calls for player turns, handle final score comparison.

**Process:**
1. Initialise variables
2. Game starts in a while(True) which constantly loops the code, increments the turn counter, and is immediately met by a condition that exits the loop when the current turn number exceeds the maximum turn number
3. Deck is called to reset the deck and player hands
4. Hands are populated with cards
5. If dealer has a 21, proceed to final score calculation. Else, move on to loop through the players to prompt their input.
6. During player input, players choose to draw, pass or surrender. If player score reaches above 21, their turn automatically moves on
7. Final score comparison, compare scores of players and dealer to determine winners, losers and draws.
8. Game loops back to the top due to the while(True) loop, only exiting due to step 2.
s