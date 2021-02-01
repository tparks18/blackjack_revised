#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def turn_to_string(self):
        return str(self.rank) + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.cards = []
        suits = [
            'Clubs', 'Diamonds', 'Spades', 'Hearts '
        ]
        ranks = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
        ]
        for x in suits:
            for y in ranks:
                card_object = Card(x, y)
                self.cards.append(card_object)

    def shuffle(self):
        # randomizes the cards in self.deck
        random.shuffle(self.cards)

    def readable(self):
        # Makes it so that the card objects come out as 'rank of suit'
        results = []
        for cards in self.cards:
            results.append(cards.turn_to_string())
        return results

    def draw(self):
        return self.cards.pop(0)

class Dealer:
    def __init__(self):
        self.hand = []

    def deal_card(self, deck):
        return deck.draw()

    def show_hand(self, all = False):
        results = []
        for cards in self.hand:
            results.append(cards.turn_to_string())
        if all:
            return results
        return results[0]

    def add_card(self, card : Card):
        self.hand.append(card)

    def count_cards(self):
        sum_of_cards = 0
        for cards in self.hand:
            sum_of_cards += cards.rank
        return sum_of_cards

class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card : Card):
        self.hand.append(card)

    def show_hand(self):
        results = []
        for cards in self.hand:
            results.append(cards.turn_to_string())
        return results

    def count_cards(self):
        sum_of_cards = 0
        for cards in self.hand:
            sum_of_cards += cards.rank
        return sum_of_cards

done = False
while not done:

    # initialize the deck --> shuffle the deck -> initialize player and dealer.
    cards = Deck()
    cards.shuffle()
    player = Player()
    dealer = Dealer()

    # these two for loops are adding cards into the player and dealers hands.
    for x in range(2):
        player.add_card(dealer.deal_card(cards))

    for x in range(2):
        dealer.add_card(dealer.deal_card(cards))

    if player.count_cards() == 21:
        print("You win!")
        if input("Wanna play again? (y/n)").lower() != 'y':
            break
        else:
            continue

    action = ''
    print("dealer's hand: {}".format(dealer.show_hand()))
    while player.count_cards() < 21 and action != 'stand':
        print("player's hand: {}".format(player.show_hand()))
        action = input("Hit or Stand?").lower()
        if action == 'hit':
            player.add_card(dealer.deal_card(cards))
        elif action != 'stand':
            print('Invalid Command')

    if player.count_cards() > 21:
        print('Bust! Dealer Wins')
        if input("Wanna play again? (y/n)").lower() != 'y':
            break
        else:
            continue

    print("dealer's hand: {}".format(dealer.show_hand(True)))
    while dealer.count_cards() < 17:
        dealer.add_card(dealer.deal_card(cards))

    print("dealer's hand: {}".format(dealer.show_hand(True)))
    if dealer.count_cards() > 21:
        print("Bust! Player wins!")
    elif dealer.count_cards() >= player.count_cards():
        print("Dealer Wins!")
    else:
        print("Player Wins!")

    if input("Wanna play again? (y/n)").lower() != 'y':
        break

