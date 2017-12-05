from map import VALUE_MAP, SUIT_MAP


class Card:

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value


    def fifteen_value(self):
        """Compute the value of the card used to count fifteens"""
        if self.value < 9:
            return self.value + 1
        else:
            return 10


    def card_str(self):
        """Return a string representation of the card"""
        suit_str = SUIT_MAP.get(self.suit)
        value_str = VALUE_MAP.get(self.value)
        return "{} of {}".format(value_str, suit_str)
