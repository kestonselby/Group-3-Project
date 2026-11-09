from Deck import Deck

class Hand:
    # Creates a new hand for a player or dealer
    def __init__(self, owner):
        self.cards = []
        self.owner = owner

    # Adds a card to the hand
    def add_card(self, card):
        self.cards.append(card)


    def score(self):
        score = 0
        aces = 0

        for card in self.cards:
            rank = card.split()[0]
            score+= Deck.CARD_VALUES[rank]

            if rank== "A":
                aces+= 1

        # If over 21, changes Aces from 11 to 1
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

    # Checks if the hand is over 21
    def is_bust(self):
        return self.score() > 21

    def is_blackjack(self):
        return len(self.cards) == 2 and self.score() == 21

    # Shows the owner, the cards and the score
    def show(self):
        return f"{self.owner}'s hand: {', '.join(self.cards)} (Score: {self.score()})"

if __name__ == "__main__":
    print("Testing Hand.py...")

    hand1 = Hand("Player")
    hand1.add_card("K spades")
    hand1.add_card("9 hearts")
    print(hand1.show()) # score: 19

    hand2 = Hand("Player")
    hand2.add_card("A clubs")
    hand2.add_card("K hearts")
    print(hand2.show(), hand2.is_blackjack()) # score: 21, true

    hand3 = Hand("Player")
    hand3.add_card("K spades")
    hand3.add_card("Q hearts")
    hand3.add_card("5 clubs")
    print(hand3.show(), hand3.is_bust()) # score: 25, true