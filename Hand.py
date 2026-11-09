import json
from Deck import Deck


class Hand:
    # Creates a new hand for a player or dealer
    def __init__(self, owner, show_soft=False):
        self.cards = []
        self.owner = owner
        self.show_soft = show_soft

    # Adds a card to the hand
    def add_card(self, card):
        self.cards.append(card)

    # Recursively changes Aces from 11 to 1 if the score is over 21
    def adjust_aces(self, total, aces):
        if total > 21 and aces > 0:
            return self.adjust_aces(total - 10, aces - 1)
        return total

    # Calculates the total score of the hand
    def score(self):
        total = 0
        aces = 0

        for card in self.cards:
            rank = card.split()[0]
            total += Deck.CARD_VALUES[rank]
            if rank == "A":
                aces += 1

        return self.adjust_aces(total, aces)

    def is_bust(self):
        return self.score() > 21

    def is_blackjack(self):
        return len(self.cards) == 2 and self.score() == 21

    # Displays 6/16 for A+5 only when --show-soft was enabled
    def score_display(self, hole_card_status=False):
        total = self.score()
        aces = sum(card.split()[0] == "A" for card in self.cards)
        raw_total = sum(Deck.CARD_VALUES[card.split()[0]] for card in self.cards)

        if hole_card_status:
            hole_card = self.cards[0].split()[0]
            if hole_card == 'A':
                total -= 11
                aces -= 1
            elif hole_card in ["J", "Q", "K", "A"]:
                total -= 10
            else:
                total -= int(hole_card)


        # At least one Ace is still counted as 11
        has_soft_ace = aces > 0 and (raw_total - total) < 10 * aces
        if self.show_soft and has_soft_ace:
            return f"{total - 10}/{total}"
        return str(total)

    # Shows the owner, cards and score
    def show(self):
        return f"{self.owner}'s hand: {', '.join(self.cards)} (Score: {self.score_display()})"

    # Turns the hand into data JSON can store
    def to_dict(self):
        return {"owner": self.owner, "cards": self.cards.copy()}

    # Rebuilds a Hand from saved data
    @classmethod
    def from_dict(cls, data, show_soft=False):
        hand = cls(data["owner"], show_soft=show_soft)
        hand.cards = list(data["cards"])
        return hand


# Saves hands beside Rayan's deck without replacing the saved deck
def save_hands(game_num, hands):
    try:
        with open("saveData.json", "r", encoding="utf-8") as read_file:
            saves = json.load(read_file)
    except (FileNotFoundError, json.JSONDecodeError):
        saves = {}

    saves[f"save{game_num}_hands"] = [hand.to_dict() for hand in hands]

    with open("saveData.json", "w", encoding="utf-8") as write_file:
        json.dump(saves, write_file, indent=4)


# Loads hands for the requested save number
def load_hands(game_num, show_soft=False):
    try:
        with open("saveData.json", "r", encoding="utf-8") as read_file:
            saves = json.load(read_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    saved_data = saves.get(f"save{game_num}_hands", [])
    return [Hand.from_dict(item, show_soft=show_soft) for item in saved_data]


if __name__ == "__main__":
    hand1 = Hand("Player")
    for card in ["A spades", "A hearts", "9 clubs"]:
        hand1.add_card(card)
    print(hand1.show())
    assert hand1.score() == 21

    hand2 = Hand("Player")
    for card in ["K spades", "6 hearts", "A clubs"]:
        hand2.add_card(card)
    print(hand2.show())
    assert hand2.score() == 17

    hand3 = Hand("Player", show_soft=True)
    for card in ["A spades", "5 hearts"]:
        hand3.add_card(card)
    print(hand3.show())
    assert hand3.score_display() == "6/16"

    hand4 = Hand("Player")
    hand4.add_card("A spades")
    hand4.add_card("A hearts")
    hand4.add_card("A clubs")
    hand4.add_card("9 diamonds")

    print(hand4.show()) 
    assert hand4.score() == 12

    print("Part B and D tests passed!")
