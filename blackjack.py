#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
THIS IS A BLACKJACK GAME

Can be run from the terminal (make sure file is executable).

Please have fun! Remember to gamble responsibly.

"""

import numpy as np

cards_values = (['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ac','2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'Ad', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'Ah', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'As'], [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, (1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, (1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, (1,11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, (1,11)])

deck = {}
for card in range(len(cards_values[0])):
	deck[cards_values[0][card]] = cards_values[1][card]

class Dealer():
	def __init__(self, bank=10000, hand=[], sleeve=list(deck.keys())):
		self.sleeve = sleeve
		self.bank = bank
		self.hand = hand
		
	def deal_card(self):
		card = np.random.randint(len(self.sleeve))
		return self.sleeve.pop(card)

	def refresh_sleeve(self):
		self.sleeve = list(deck.keys())
		self.hand=[]
	
	def pay_up(self, bet, win):
		if win:
			self.bank -= bet
			return bet
		else:
			self.bank += bet


class Player():
	def __init__(self, chips=0, hand=[]):
		self.chips=chips
		self.hand=[]
	
	def place_bet(self, bet):
		int_check = True
		while int_check:
			if type(bet) == int:
				int_check = False
			else:
				try: bet=int(bet)
				except ValueError: bet = input("This casino does not accept '{}'. Please enter a reasonable bet (integer): ".format(bet))
				int_check = True
		self.chips -= bet
		return bet

	def hit_me(self, decision):
		hit = True
		while hit:
			if decision == "y":
				hit = False
				return True
			elif decision == "n":
				hit = False
				return False
			else:
				decision = input("I suggest you hit, sir/madam... (please enter y or n): ")
				hit = True
				
	def refresh_hand(self):
		self.hand=[]


def calculate_hand(hand):
	tot=0
	aces = []
	for card in hand:
		try: tot+=deck[card]
		except: aces.append(card)
	if aces:
		if tot <= 10:
			tot += sum([max(deck[card]) for card in aces])
		else:
			tot+= sum([min(deck[card]) for card in aces])
	return tot


def bust_check(hand):
	tot = calculate_hand(hand)
	bust = False
	if tot == 21:
		if len(hand)==2: 
			print("BLACKJACK!!!, {}!".format(tot))
		return bust
	elif tot < 21:
		return bust
	else:
		bust = True
		print("Bust!")
		return bust


def play_blackjack():
	#initialise the player and casino
	player=input("What is your name? ")
	print("Welcome to the casino, {}!".format(player))
	casino = Dealer()
	player = Player(1000)
	
	def play_hand():
		input("Press ENTER to play... ")
		#betting phase
		bet = player.place_bet(input("You have ${}. Place your bets! ".format(player.chips)))
		print("Your bet is: ${}, remaining chips: ${}".format(bet, player.chips))
		#first deal phase
		casino.hand.append(casino.deal_card())
		print("The dealer face-up card is: {}, total: {}.".format(casino.hand, calculate_hand(casino.hand)))
		input("Press ENTER to deal your cards! ")
		player.hand.append(casino.deal_card())
		player.hand.append(casino.deal_card())
		print("Your hand is: {}, total: {}.".format(player.hand,calculate_hand(player.hand)))
		#player can hit until bust
		bust = bust_check(player.hand)
		while not bust:
			decision = player.hit_me(input("Would you like to hit? Enter y or n: "))
			if decision:
				player.hand.append(casino.deal_card())
				print("Your hand is: {}, total: {}.".format(player.hand,calculate_hand(player.hand)))
				bust = bust_check(player.hand)
			else:
				print("Your final hand is: {}, total: {}".format(player.hand,calculate_hand(player.hand)))
				break
		#dealer follows house rules, hits under 17, stand otherwise.
		while calculate_hand(casino.hand) < 17:	
			print('dealer hand is: {}, total: {}, dealing card..'.format(casino.hand, calculate_hand(casino.hand)))
			casino.hand.append(casino.deal_card())
			input("Press ENTER to continue... ")
		print("Your final hand is: {}, total: {}".format(player.hand,calculate_hand(player.hand)))
		print("Dealer's final hand is: {}, total: {}".format(casino.hand, calculate_hand(casino.hand)))
		#decide who wins
		if bust:
			print("You lost {}!".format(bet))
			casino.pay_up(bet, False)
		elif bust_check(casino.hand):
			print("You won ${}!".format(bet))
			player.chips += casino.pay_up(bet, True)*2
		elif calculate_hand(player.hand) > calculate_hand(casino.hand):
			print("You won ${}!".format(bet))
			player.chips += casino.pay_up(bet, True)*2
		elif calculate_hand(player.hand) == calculate_hand(casino.hand):
			print("Push, you get your money back")
			player.chips += casino.pay_up(bet, True)
		else:
			print("You lost {}!".format(bet))
			casino.pay_up(bet, False)
			
	game_on=True
	while game_on == True:
		play_hand()
		if input("You have ${}. Would you like to continue playing? (y or n): ".format(player.chips)).lower() == 'n':
			print("Better luck next time!")
			game_on = False
		else:
			print("Shuffling cards...")
			casino.refresh_sleeve()
			player.refresh_hand()
			game_on = True


if __name__=="__main__":
	play_blackjack()

		

