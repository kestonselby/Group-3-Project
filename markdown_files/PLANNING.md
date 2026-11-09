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

### Beginner Guide, Menu Navigation (Keston)
1. add for case "3" in the switch case match calling the how to play function and also replace "Option 3" -> "How To Play"
2. in the case "3" bracket call the function How_To_Play so when the user inputs 3 it will do what the function does instead of having it all in case "3"
3. create the function how_to_play
4. add all the rules to blackjack in the how to play screen and also add an input to go back to basically the main menu screen or (The 5 options again.)
5. add an if else statement just in case the user doesn't do the input 1, it tells the user the input he did is invalid. and if the input is 1 it does what end of step 4 says.

## Milestone 2 - Practical Application

### Deck Creation and Manipulation (Rayan)

**Purpose:**
Expand m1's deck system using oop principles, deck is now responsible for creation, resetting, dealing, saving, and loading cards. recursion is added in the form of a recursive deck validation function, and argparse is included by giving the ability to load specific saves from the file

**Data:**
- Deck class, holds and manages deck info
- List of current cards in a deck
- Dict containing card's and their respective values
- List of card suits
- JSON file to which game saves are read and written from

**Functions/Responsibilites:**
1. initializeDeck - creates a new deck with all 52 cards
2. resetDeck - resets the current deck back to initialized state
3. dealCard - randomly pops card from array and returns
4. saveDeck - saves current deck into selected save in the JSON file
5. loadDeck - loads a selected save deck from the JSON file
6. validateDeck - recursively checks a loaded deck to check for corrupted/altered card info
7. --load-save - argparse command used to select specific game save to load

**Process:**
1. Deck object is created and initialized
2. dealCard is used to remove and return cards from respective Deck object
3. resetDeck can be used to return the Deck object back to initialized state
4. saveDeck stores current deck in selected save # in JSON file
5. loadDeck reads selected save from JSON file for use in game
6. validateDeck checks each card before current deck is replaced with save deck
7. when --load-save is added to the run command, selected save number is passed to loadDeck

# Player Statistics, & History 
Purpose:

Expand the Blackjack game's functionality by introducing player statistics through OOP, recursive menu input validation, file handling for game history, and additional command-line functionality. OOP is implemented through a PlayerStats class that stores and manages player statistics. Recursion is used to validate menu selections by repeatedly requesting input until a valid choice is entered or the attempt limit is reached. File I/O allows saved game history to be retrieved and displayed, while argparse provides the ability to access game history directly when launching the program. The interface is also expanded with a Player Statistics menu option.

Data:
- PlayerStats class, responsible for managing player statistics
- Integer variable rounds_played, stores the number of rounds played
- Integer variable attempts, tracks the number of invalid menu attempts
- List of valid menu choices, used to validate user input
- String variable history, stores the contents read from the game history file
- Text file game_history.txt, used to store and retrieve game records
- Boolean command-line argument --history, determines whether game history should display at startup

Functions/Responsibilities:

1. PlayerStats - Class that manages and stores player statistics.
2. __init__ - Initializes the PlayerStats object and sets rounds_played to zero.
3. record_round - Increases the player's round counter when a round is recorded.
4. display_stats - Displays the player's current statistics.
5. get_valid_choice - Recursively validates user menu selections and limits invalid attempts to five.
6. display_game_history - Opens and reads the saved game history file, then displays its contents.
7. --history - Argparse command-line argument that allows users to display saved game history when launching the program.
8. Player Statistics Menu Option - Allows users to access their player statistics directly through the main menu.

Process:

Step 1. A PlayerStats object is created using the PlayerStats class, initializing the player's round counter to zero.

Step 2. When a round is recorded, record_round increases the rounds_played variable.

Step 3. When the player selects the statistics option from the menu, display_stats displays the current statistics.

Step 4. When the user enters a menu selection, get_valid_choice checks whether the selection is valid.

Step 5. If the selection is invalid, the function calls itself again and increases the attempt counter. After five invalid attempts, the function stops.

Step 6. display_game_history opens game_history.txt in read mode and retrieves previously saved game records.

Step 7. If the history file cannot be found, exception handling displays an appropriate message instead of allowing the program to crash.

Step 8. When --history is included in the command-line launch, the program checks the argument and calls display_game_history to display the saved records.

Step 9. The Player Statistics menu option connects the user interface to the PlayerStats object, allowing statistics to be accessed through the main menu.
