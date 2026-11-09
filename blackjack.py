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

# cmd line argumment to enable dealer hole card (zay)
parser.add_argument("--hole-card", action="store_true", help="Hide dealer's first card")

# cmd line argument to display game history (keston) 
parser.add_argument( "--history", action="store_true", help="Display saved Blackjack game history")

args = parser.parse_args()



# loads specific save deck as current game
# if args.load_save:
#     gameDeck = Deck()
#     gameDeck.loadDeck(args.load_save)

# Temporary test for show-soft
# player_hand = Hand("Player", show_soft=args.show_soft)

# player_hand.add_card("A spades")
# player_hand.add_card("5 hearts")

# print(player_hand.show())


# MAIN GAME LOGIC GOES HERE

# File I/O and Command-Line Argument (Keston)
def display_game_history():
    try:
        with open("game_history.txt", "r", encoding="utf-8") as file:
            history = file.read()

        print("\n========== GAME HISTORY ==========")

        if history.strip():
            print(history)
        else:
            print("No game history available.")

        print("=================================")

    except FileNotFoundError:
        print("\nNo game history file found.")


def main():
     # Keston's command-line history option
    if args.history:
        display_game_history()

    while True:
        # Import menu functions - to turn into tkinter ui as well if time permits
        print("\n1. Start Game")
        print("2. View Arguments")
        print("3. Exit")
        choice = input("Enter choice: ")

        match choice:
            case "1":
                root = tk.Tk()
                app = BlackjackUI(root, args)
                root.mainloop()
                break
            case "2":
                while True:
                    print("\nOptions:")
                    print(f"1. Soft Hand: {args.show_soft}")
                    print(f"2. Hole Card: {args.hole_card}")
                    print(f"3. Load Save: {args.load_save}")
                    print(f"4. Return")
                    choice = input("Toggle: ")
                    match choice:
                        case "1": args.show_soft = not getattr(args, 'show_soft', False)
                        case "2": args.hole_card = not getattr(args, 'hole_card', False)
                        case "3": 
                            save_num = input("Enter save number: ")
                            try:
                                args.load_save = int(save_num)
                            except:
                                print("\nINVALID NUMBER.")
                            pass
                        case _: break
            case "3":
                break

if __name__ == '__main__':
    main()
