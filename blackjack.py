import argparse
from Deck import Deck

parser = argparse.ArgumentParser()

# cmd line arugment addition (rayan)
parser.add_argument("--load-save", type=int, help="Choose a game-save to load from")

args = parser.parse_args()

# loads specific save deck as current game
if args.load_save:
    gameDeck = Deck()
    gameDeck.loadDeck(args.load_save)


# MAIN GAME LOGIC GOES HERE



