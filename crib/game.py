from crib.card import Card
from crib.util import powerset


class Game:

    def __init__(self, hand, cut):
        self.hand = hand
        self.cut = cut
        self.all_five = list(hand)
        self.all_five.append(cut)
        self.total_score = None


    def score(self):
        """Compute score of the Crib hand"""

        if len(self.hand) != 4:
            raise ValueError("The given hand is not of size four")

        for card in self.hand:
            if not isinstance(card, Card):
                raise ValueError("The hand must consist of only Card objects")

        if not isinstance(self.cut, Card):
            raise ValueError("The cut must be a single Card object")

        # Compute scores
        self.pair_score = self._pairs()
        self.fifteen_score = self._fifteens()
        self.flush_score = self._flush()
        self.jack_score = self._jack()
        self.run_score = self._runs()
        self.total_score = (self.pair_score + self.fifteen_score + self.flush_score +
                            self.jack_score + self.run_score)

        return self.total_score


    def print_score(self):
        """Print the score for each element of the game"""

        if not self.total_score:
            self.score()

        print("Hand: ", end="")
        for card in self.hand[:-1]:
            print("{}, ".format(card.card_str()), end="")
        print("{}".format(self.hand[-1].card_str()), end="")
        print("\nCut: {}".format(self.cut.card_str()))
        print("---")
        print("Pair: {}".format(self.pair_score))
        print("Fifteen: {}".format(self.fifteen_score))
        print("Run: {}".format(self.run_score))
        print("Flush: {}".format(self.flush_score))
        print("Jack: {}".format(self.jack_score))
        print("---")
        print("Total: {}".format(self.total_score))


    def _pairs(self):
        """Compute the score for pairs"""
        pair_score = 0

        # For every card value, count the number of occurences, compute
        # the score, and add that score to the total pair score
        for i in range(13):
            count = self._count_value(i)
            if count == 2:
                pair_score += 2
            elif count == 3:
                pair_score += 6
            elif count == 4:
                pair_score += 12

        return pair_score


    def _fifteens(self):
        """Compute the score for fifteens"""
        fifteen_score = 0
        pset = powerset(self.all_five)

        for entry in pset:
            if self._sum_cards(entry) == 15:
                fifteen_score += 2

        return fifteen_score


    def _flush(self):
        """Compute the score for a flush (four card or five card)"""
        if all(card.suit == self.hand[0].suit for card in self.hand):
            if self.cut.suit == self.hand[0].suit:
                return 5
            else:
                return 4
        return 0


    def _jack(self):
        """Compute the score for having a jack of the same suit as the cut"""
        for card in self.hand:
            if (card.value == 10) and (card.suit == self.cut.suit):
                return 1
        return 0


    def _runs(self):
        """Compute the score for a run of three, four, or five cards"""

        # Used for sorting subsets
        def get_card_value(card):
            return card.value

        runs = []
        run_score = 0
        pset = powerset(self.all_five)

        for entry in pset:

            sub_run = False
            if len(entry) < 3:
                continue

            sorted_entry = sorted(entry, key=get_card_value)
            current_val = sorted_entry[0].value
            count = 1

            for card in sorted_entry[1:]:
                if card.value == (current_val + 1):
                    count += 1
                    current_val = card.value
                else:
                    count = 0

            if count == 0:
                continue

            if count >= 3:
                runs.extend([sorted_entry])

        runs_final = []
        for run1 in runs:
            sublist = False
            for run2 in runs:
                if self._sublist(run1, run2):
                    sublist = True
            if not sublist:
                runs_final.extend([run1])

        for run in runs_final:
            run_score += len(run)

        return run_score


    def _count_value(self, value):
        """Count the number of occurences of the given value (all five cards)"""
        count = 0
        for card in self.all_five:
            if card.value == value:
                count += 1
        return count


    def _sum_cards(self, cards):
        """Compute the sum of the values of the given set of cards"""
        hand_sum = 0
        for card in cards:
            hand_sum += card.fifteen_value()
        return hand_sum


    def _print_cards(self, cards):
        for card in cards:
            print(card.card_str())


    def _sublist(self, lst1, lst2):
       l1 = []
       l2 = []

       for item in lst2:
           l2.append(item.value)

       for item in lst1:
           l1.append(item.value)

       return set(l1) < set(l2)
