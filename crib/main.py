from card import Card
from game import Game


# Initialize hand and the cut
hand = [Card(1, 0), Card(2, 1), Card(3, 2), Card(4, 3)]
cut = Card(2, 0)

# Setup game
game = Game(hand, cut)

# Score hand
game.print_score()
