import tkinter as tk
# from Deck import Deck

class BlackjackUI:
    def __init__(self, root):
        # Init 
        self.root = root
        self.root.title("Group 3 - Blackjack")
        self.root.geometry("800x500") # Window size

        # why do i need to add this to self for it to work
        self.bgcolour = "#2b7a38" # global background colour variable

        self.root.configure(bg=self.bgcolour)

        # create window
        self.setup_game()

    #  considering fully importing the menu here as well, right now its just the game menu



    def setup_game(self):
        # DEALER SECTION (top of screen)

        self.dealer_frame = tk.Frame(self.root, bg=self.bgcolour)
        self.dealer_frame.pack(pady=20)
        # pack() stacks elements vertically
        # i dont know why this took me a significant amount of time to learn how to do
        # padx pady is margin equivalent of html

        # label is for text elements
        tk.Label(self.dealer_frame, text="Dealer's Hand", bg=self.bgcolour, fg="white", font=("Arial", 14, "bold")).pack()
        
        # display the actual cards (eg "10 spades, A hearts")
        self.dealer_cards_label = tk.Label(self.dealer_frame, text="[cards appear here]", bg=self.bgcolour, fg="white", font=("Arial", 18))
        self.dealer_cards_label.pack(pady=5)

        # label for dealer's score
        self.dealer_score_label = tk.Label(self.dealer_frame, text="Score: 0", bg=self.bgcolour, fg="white", font=("Arial", 12))
        self.dealer_score_label.pack()


        # MIDDLE SECTION (to display game messages)
        # Note: remember to hide/set to empty string during the game
        self.status_label = tk.Label(self.root, text="Play Blackjack!", bg=self.bgcolour, fg="black", font=("Arial", 16, "bold"))
        self.status_label.pack(pady=30)


        # BOTTOM SECTION 1 (player cards)
        self.player_frame = tk.Frame(self.root, bg=self.bgcolour)
        self.player_frame.pack(pady=20)

        tk.Label(self.player_frame, text="Player's Hand", bg=self.bgcolour, fg="white", font=("Arial", 14, "bold")).pack()
        
        self.player_cards_label = tk.Label(self.player_frame, text="[cards appear here]", bg=self.bgcolour, fg="white", font=("Arial", 18))
        self.player_cards_label.pack(pady=5)

        self.player_score_label = tk.Label(self.player_frame, text="Score: 0", bg=self.bgcolour, fg="lightgray", font=("Arial", 12))
        self.player_score_label.pack()


        # BOTTOM SECTION 2 (player buttons)
        # Frame to hold buttons side-by-side
        self.button_frame = tk.Frame(self.root, bg=self.bgcolour)
        self.button_frame.pack(pady=20)

        # The 'command' parameter connects the button click to a function
        self.hit_btn = tk.Button(self.button_frame, text="Hit", command=self.handle_hit, width=10, font=("Arial", 12))
        self.hit_btn.grid(row=0, column=0, padx=10)
        # grid() aligns items in rows and columns much easier than html
        # padx here is margin to the side of buttons

        self.stand_btn = tk.Button(self.button_frame, text="Stand", command=self.handle_stand, width=10, font=("Arial", 12))
        self.stand_btn.grid(row=0, column=1, padx=10)

        self.split_btn = tk.Button(self.button_frame, text="Split", command=self.handle_split, width=10, font=("Arial", 12))
        self.split_btn.grid(row=0, column=2, padx=10)
        self.split_btn.config(state="disabled") # need to figure out how to split first

        self.deal_btn = tk.Button(self.button_frame, text="New Game", command=self.handle_newgame, width=15, font=("Arial", 12))
        self.deal_btn.grid(row=0, column=3, padx=10)
        # Maybe replace new game button with exit? Or add somewhere else


    
    def handle_newgame(self):
        # button action for new game
        self.status_label.config(text="Game Started!")
        root.after(1000, self.clear_message) # clears text 1 second after start
        # TODO: initialize Deck()
        # TODO: deal 2 to each(?) player and dealer
        # TODO: update UI
        self.player_cards_label.config(text="10 spades   5 clubs")

        # I didnt know vscode auto colours TODO, its nice

    def clear_message(self):
        self.status_label.config(text="")
    

    def handle_hit(self):
        # button action for hit
        # TODO: draw card from deck, add to player hand
        self.status_label.config(text="Player hits")
        root.after(1000, self.clear_message)
        # TODO: calculate and update score
        # TODO: if score > 21, display bust message (and disable hit so the player can only stand or end game)
        # I feel like maybe figure out how to auto next round if player auto wins/loses
        pass

    def handle_stand(self):
        # button action for stand/pass
        self.status_label.config(text="Player stands")
        root.after(1000, self.clear_message)
        # TODO: dealer draws cards until >= 17
        # TODO: compare scores and update status label with winner
        pass

    def handle_split(self):
        # split code
        pass

# lets you run python tui.py to see the layout cause otherwise i would have to keep starting from main.py
if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackUI(root)
    root.mainloop()