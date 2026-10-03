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