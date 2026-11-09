import argparse
from Deck import Deck
from Hand import Hand

import tkinter as tk
from tui import BlackjackUI

parser = argparse.ArgumentParser()

# cmd line arugment addition (rayan)
parser.add_argument("--load-save", type=int, help="Choose a game-save to load from")

# cmd line argumment to display soft scores (jerome)
parser.add_argument("--show-soft", action="store_true", help="Show soft Ace scores")

args = parser.parse_args()

# loads specific save deck as current game
if args.load_save:
    gameDeck = Deck()
    gameDeck.loadDeck(args.load_save)

# Temporary test for show-soft
player_hand = Hand("Player", show_soft=args.show_soft)

player_hand.add_card("A spades")
player_hand.add_card("5 hearts")

print(player_hand.show())


# MAIN GAME LOGIC GOES HERE




def main():
    while True:
        # Import menu functions - to turn into tkinter ui as well if time permits
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter choice: ")

        match choice:
            case "1":
                root = tk.Tk()
                app = BlackjackUI(root)
                root.mainloop()
                break
            case "2":
                break

if __name__ == '__main__':
    main()
