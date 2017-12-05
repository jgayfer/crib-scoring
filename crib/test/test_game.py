import pytest

from crib.card import Card
from crib.game import Game


class TestFifteen:

    def test_no_fifteen(self):
        """Test that a score of zero is given for no fifteens"""
        hand = [Card(1, 0), Card(2, 1), Card(0, 2), Card(1, 3)]
        cut = Card(2, 0)
        game = Game(hand, cut)
        game.score()
        assert game.fifteen_score == 0


    def test_two_cards_fifteen(self):
        """Test that two cards totalling fifteen is scored as 2"""
        hand = [Card(1, 0), Card(2, 1), Card(7, 2), Card(8, 3)]
        cut = Card(12, 0)
        game = Game(hand, cut)
        game.score()
        assert game.fifteen_score == 2


    def test_three_cards_fifteen(self):
        """Test that three cards totalling fifteen is scored as 2"""
        hand = [Card(1, 0), Card(1, 1), Card(0, 2), Card(8, 3)]
        cut = Card(12, 0)
        game = Game(hand, cut)
        game.score()
        assert game.fifteen_score == 2


    def test_four_cards_fifteen(self):
        """Test that four cards totalling fifteen is scored as 2"""
        hand = [Card(2, 0), Card(0, 1), Card(0, 2), Card(8, 3)]
        cut = Card(12, 0)
        game = Game(hand, cut)
        game.score()
        assert game.fifteen_score == 2


    def test_five_cards_fifteen(self):
        """Test that five cards totalling fifteen is scored as 2"""
        hand = [Card(1, 0), Card(0, 1), Card(0, 2), Card(0, 3)]
        cut = Card(9, 0)
        game = Game(hand, cut)
        game.score()
        assert game.fifteen_score == 2


    def test_double_counted_card(self):
        """Test that a card can be used in two different counts of 15"""
        hand = [Card(4, 0), Card(12, 1), Card(11, 2), Card(0, 3)]
        cut = Card(6, 0)
        game = Game(hand, cut)
        game.score()
        assert game.fifteen_score == 4


class TestFlush:

    def test_four_card_flush(self):
        """Test that four cards of the same suit is a flush"""
        hand = [Card(1, 0), Card(2, 0), Card(7, 0), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.flush_score == 4


    def test_five_card_flush(self):
        """Test that five cards of the same suit is a flush (include cut)"""
        hand = [Card(1, 0), Card(2, 0), Card(7, 0), Card(8, 0)]
        cut = Card(12, 0)
        game = Game(hand, cut)
        game.score()
        assert game.flush_score == 5


class TestRun:

    def test_no_run(self):
        """If there is no run, no points should be given"""
        hand = [Card(1, 0), Card(2, 0), Card(7, 0), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.run_score == 0


    def test_run_of_three(self):
        """Test that a three card run is scored as 3"""
        hand = [Card(1, 0), Card(2, 0), Card(3, 0), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.run_score == 3


    def test_run_of_four(self):
        """Test that a four card run is scored as 4"""
        hand = [Card(1, 0), Card(3, 0), Card(2, 0), Card(8, 0)]
        cut = Card(4, 3)
        game = Game(hand, cut)
        game.score()
        assert game.run_score == 4


    def test_run_of_five(self):
        """Test that a five card run is scored as 5"""
        hand = [Card(1, 0), Card(3, 0), Card(2, 0), Card(5, 0)]
        cut = Card(4, 3)
        game = Game(hand, cut)
        game.score()
        assert game.run_score == 5


    def test_double_run(self):
        """Test cards can be part of two runs"""
        hand = [Card(1, 0), Card(1, 0), Card(2, 0), Card(5, 0)]
        cut = Card(3, 3)
        game = Game(hand, cut)
        game.score()
        assert game.run_score == 6


class TestPairs:

    def test_no_pairs(self):
        """If thereare no pairs, no points should be given"""
        hand = [Card(1, 0), Card(2, 0), Card(7, 0), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.pair_score == 0


    def test_one_pair(self):
        """A single pair should be scored as 2"""
        hand = [Card(12, 0), Card(2, 0), Card(7, 0), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.pair_score == 2


    def test_two_pairs(self):
        """Two pairs should be scored as 4"""
        hand = [Card(12, 0), Card(2, 0), Card(2, 0), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.pair_score == 4


    def test_three_of_a_kind(self):
        """Three of a kind should be scored as 6"""
        hand = [Card(12, 0), Card(12, 1), Card(2, 0), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.pair_score == 6


    def test_four_of_a_kind(self):
        """Four of a kind should be scored as 12"""
        hand = [Card(12, 0), Card(12, 2), Card(12, 1), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.pair_score == 12


    def test_full_house(self):
        """A full house should be scored as 8"""
        hand = [Card(12, 0), Card(12, 2), Card(8, 1), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.pair_score == 8


class TestJack:

    def test_no_jack(self):
        """If no jack is in hand, no points should be awarded"""
        hand = [Card(1, 0), Card(2, 0), Card(7, 0), Card(8, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.jack_score == 0


    def test_jack_wrong_suit(self):
        """If a jack is in hand, but not of the cut suit, no points should be given"""
        hand = [Card(1, 0), Card(2, 0), Card(7, 0), Card(10, 0)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.jack_score == 0


    def test_jack_correct_suit(self):
        """If a jack is in hand of the same suit as the cut, award 1 point"""
        hand = [Card(1, 0), Card(2, 0), Card(7, 0), Card(10, 3)]
        cut = Card(12, 3)
        game = Game(hand, cut)
        game.score()
        assert game.jack_score == 1


class TestHands:

    def test_best_hand(self):
        """The best hand in crib is worth 29 points"""
        hand = [Card(4, 0), Card(4, 2), Card(4, 3), Card(10, 1)]
        cut = Card(4, 1)
        game = Game(hand, cut)
        game.score()
        assert game.total_score == 29
