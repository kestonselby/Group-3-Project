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