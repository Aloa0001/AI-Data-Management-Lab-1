import random

CARDS_DECK_SIZE = 52
SUITS = ["s", "h", "d", "c"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def createDeck():
    deck = []
    for val in VALUES:
        for su in SUITS:
            deck.append(val + su)
    return deck


def shuffle(deck):
    s_deck = deck.copy()  # Copy the deck to be shuffled

    # Shuffle the cards deck - at every index, swap the value with a random index
    for i in range(CARDS_DECK_SIZE):
        j = random.randint(0, CARDS_DECK_SIZE - 1)
        (s_deck[i], s_deck[j]) = (s_deck[j], s_deck[i])

    return (deck, s_deck)


class Cards:
    # having a constructor to initialize the instance state (attributes)
    def __init__(self):
        self.cards = createDeck()

    # creates the cards deck
    #
    # but, a better practice is to use the __init__ constructor
    # for initializing the instances state (attributes)
    # def create(self):
    #     # Create a complete deck of cards
    #     self.cards = createDeck()

    def shuffle(self):
        # Shuffle the order of cards in the deck
        self.cards, shuffled_cards = shuffle(self.cards)

    # hands - the number of hands,
    # card_num - the number of cards per hand,
    # self - a deck of cards*
    def deal(self, hands, card_num):
        # Cards list, assigned to hands
        dealt_hands = []
        # Arrays for each hand
        for i in range(0, hands):
            dealt_hands.append([])

        # For each new round of cards
        for i in range(0, card_num):
            # For each of the hands lists
            for hand in dealt_hands:
                # If cards are available
                if self.cards:
                    # Pop a card from the card deck and append it to the hand
                    hand.append(self.cards.pop(0))

        return dealt_hands
