import tkinter as tk
import sys
from Deck import Deck
from Hand import Hand, save_hands, load_hands

class BlackjackUI:
    def __init__(self, root, args):
        self.root = root
        self.root.title("Group 3 - Blackjack")
        self.root.geometry("800x530") # Window size

        self.bgcolour = "#2b7a38" # global background colour variable

        self.root.configure(bg=self.bgcolour)

        #The game starts without a deck or any dealt cards
        self.show_soft = args.show_soft
        self.deck = Deck()
        self.player_hand = Hand("Player", show_soft=args.show_soft)
        self.dealer_hand = Hand("Dealer", show_soft=args.show_soft)
        self.game_over = True

        self.hole_card = args.hole_card
        self.save_slot = getattr(args, 'load_save', None)

        # this variable is specifically to track the 1s timer status so it doesnt overlap
        self.message_timer = None

        # create window
        self.setup_game()
        self.update_hand_labels()

        self.hit_btn.grid_remove()
        self.stand_btn.grid_remove()
        self.split_btn.grid_remove() # nyi
        self.save_btn.pack_forget() # prevent saving of nothing
        self.save_frame.config(bg=self.bgcolour)

        # if save parameter passed, attempt to load save
        if self.save_slot:
            self.load_game(self.save_slot)


    #  considering fully importing the menu here as well, right now its just the game menu
    def menu(self):

        pass


    def setup_game(self):
        # DEALER SECTION (top of screen)
        self.dealer_frame = tk.Frame(self.root, bg=self.bgcolour)
        self.dealer_frame.pack(pady=20)
        # pack() stacks elements vertically
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

        self.stand_btn = tk.Button(self.button_frame, text="Stand", command=self.handle_stand, width=10, font=("Arial", 12))
        self.stand_btn.grid(row=0, column=1, padx=10)

        self.split_btn = tk.Button(self.button_frame, text="Split", command=self.handle_split, width=10, font=("Arial", 12))
        self.split_btn.grid(row=0, column=2, padx=10)

        self.deal_btn = tk.Button(self.button_frame, text="New Game", command=self.handle_newgame, width=15, font=("Arial", 12))
        self.deal_btn.grid(row=0, column=3, padx=10)

        
        # The SAVE Layer
        self.save_frame = tk.Frame(self.root, bg="#FB9B45", bd=0)
        self.save_frame.pack(pady=25)
        self.save_btn = tk.Button(self.save_frame, text="🟄 SAVE", command=self.handle_save, width=7, height=2, font=("OCR A", 20, "bold"), fg="#FB9B45", bg="black", bd=0, relief="flat")
        self.save_btn.pack(padx=3, pady=3)



    def update_hand_labels(self):
        self.player_cards_label.config(text=", ".join(self.player_hand.cards) if self.player_hand.cards else "[no cards]")
        self.player_score_label.config(text=f"Score: {self.player_hand.score_display()}", fg="red" if self.player_hand.is_bust() else "lightgray")

        if self.game_over or not self.hole_card:
            self.dealer_cards_label.config(text=", ".join(self.dealer_hand.cards) if self.dealer_hand.cards else "[no cards]")
            self.dealer_score_label.config(text=f"Score: {self.dealer_hand.score_display()}", fg="red" if self.dealer_hand.is_bust() else "white")
        else:
            self.dealer_cards_label.config(text=f"[? ?], {self.dealer_hand.cards[1]}" if self.dealer_hand.cards else "[no cards]")
            self.dealer_score_label.config(text=f"Score: {self.dealer_hand.score_display(self.hole_card)}", fg="red" if self.dealer_hand.is_bust() else "white")


    def finish_game(self, message):
        self.game_over = True
        self.update_hand_labels() # update again to display final score
        self.status_label.config(text=message)
        self.hit_btn.config(state="disabled")
        self.stand_btn.config(state="disabled")
        self.deal_btn.grid()

        self.save_btn.pack_forget() # prevent saving of done game
        self.save_frame.config(bg=self.bgcolour)
        

        if self.message_timer is not None:
            self.root.after_cancel(self.message_timer)
            self.message_timer = None

    def handle_newgame(self):
        # button action for new game

        # remove the newgame button until game has ended
        self.deal_btn.grid_remove()

        self.status_label.config(text="Game Started!")
        self.message_timer = self.root.after(1000, self.clear_message) # clears text 1 second after start
    
        # Create a fresh deck and empty hands
        self.deck.resetDeck()
        self.player_hand = Hand("Player", show_soft=self.show_soft)
        self.dealer_hand = Hand("Dealer", show_soft=self.show_soft)

        # Deal two cards to each hand
        for _ in range(2):
            self.player_hand.add_card(self.deck.dealCard())
            self.dealer_hand.add_card(self.deck.dealCard())

        self.game_over = False
        self.hit_btn.config(state="normal")
        self.stand_btn.config(state="normal")
        self.update_hand_labels()

        if self.player_hand.is_blackjack() and self.dealer_hand.is_blackjack():
            self.finish_game("Both have blackjack! Tie!")
        elif self.player_hand.is_blackjack():
            self.finish_game("Blackjack! Player wins!")
        elif self.dealer_hand.is_blackjack():
            self.finish_game("Dealer has blackjack! Dealer wins!")
        else:
            self.status_label.config(text="Game started! Hit or Stand.")


        # show the player action buttons
        self.hit_btn.grid()
        self.stand_btn.grid()
        # self.split_btn.grid()

        self.save_btn.pack(padx=3, pady=3)
        self.save_frame.config(bg="#FB9B45")



    def handle_hit(self):
        # button action for hit

        if self.game_over:
            return
        
        self.status_label.config(text="Player hits")
        if self.message_timer is not None: # if there is an existing timer
            self.root.after_cancel(self.message_timer) # cancel previous 1s timer
        self.message_timer = self.root.after(1000, self.clear_message) # make new 1s timer
        
        
        # draw card from deck, add to player hand
        card = self.deck.dealCard()
        self.player_hand.add_card(card)

        self.update_hand_labels()

        if self.player_hand.is_bust():
            self.finish_game("Player busts! Dealer wins.")
        else:
            self.status_label.config(text="Player hits. Hit or Stand?")

        # automatic stand after reaching blackjack
        if self.player_hand.is_blackjack():
            self.handle_stand()
        
    def handle_stand(self):
        # button action for stand/pass
        if self.game_over:
            return

        # The dealer draws until reaching at least 17.
        while self.dealer_hand.score() < 17:
            self.dealer_hand.add_card(self.deck.dealCard())

        self.update_hand_labels()

        if self.dealer_hand.is_bust():
            self.finish_game("Dealer busts! Player wins!")
        elif self.player_hand.score() > self.dealer_hand.score():
            self.finish_game("Player wins!")
        elif self.player_hand.score() < self.dealer_hand.score():
            self.finish_game("Dealer wins!")
        else:
            self.finish_game("Tie game!")

        # again, disable action buttons
        self.hit_btn.grid()
        self.stand_btn.grid()
        # self.split_btn.grid()

        # re-show the new game button
        self.deal_btn.grid()


    def handle_split(self):
        # Splitting is not implemented yet.
        pass


    def clear_message(self):
        self.status_label.config(text="")
        self.message_timer = None


    def handle_save(self):
        # Ensure there is data to save in the first place
        if self.deck and self.player_hand and self.dealer_hand:
            # default to slot 42 if no slot was specified
            slot = self.save_slot if self.save_slot else 42
            
            self.deck.saveDeck(slot)
            save_hands(slot, [self.player_hand, self.dealer_hand])
            
            self.status_label.config(text=f"Game saved to slot {slot}!")
            if self.message_timer:
                self.root.after_cancel(self.message_timer)
            self.message_timer = self.root.after(2000, self.clear_message)
    pass

    def load_game(self, slot):
        # call load code
        self.deck.loadDeck(slot)
        hands = load_hands(slot, self.show_soft)
        
        # verify both hands loaded correctly
        if len(hands) == 2:
            self.player_hand = hands[0]
            self.dealer_hand = hands[1]

            # enable game buttons
            self.game_over = False
            self.hit_btn.config(state="normal")
            self.stand_btn.config(state="normal")
            self.hit_btn.grid()
            self.stand_btn.grid()

            self.save_btn.pack(padx=3, pady=3)
            self.save_frame.config(bg="#FB9B45")

             # re hide new game button
            self.deal_btn.grid_remove()
            
            self.update_hand_labels()
            self.status_label.config(text=f"Loaded save {slot} successfully!")
        else:
            # invalid loading
            self.status_label.config(text="Save invalid.")


# lets you run python tui.py directly
if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackUI(root, show_soft="--show-soft" in sys.argv)
    root.mainloop()
