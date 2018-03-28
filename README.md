# blackjack

A fun blackjack game in Python


This game was made by Jack Parry.

The motivation was to practice object-orientated programming in Python.

Please review the code and tell me where I could make any improvements!


In order to play the game, download the file, make it executable and run it in the terminal.
Requires NumPy.


RULES OF BLACKJACK:
 
Winning:
 - In order to win you must have a higher total hand value than the dealer.
 - The best hand value is 21. If your hand is valued above this then you're "bust" and you lose your bet.
 - If your hand equals that of the dealer, it is a "push" and your bet is returned (nobody wins).

Betting:
 - Betting takes place before any cards are dealt, in this game you start with $1000 and you can bet as much as you like!
 - If you win, you receive double your bet. The aim of the game is to make as much money as possible!

Dealing:
 - First the dealer is dealt one card.
 - Then the player is dealt two cards.
 - The player must then choose whether to "hit" (receive another card) or "stand" (stop receiving cards).
 - A player can "hit" ad infinitum until they go bust (hand total exceeds 21).
 - Once a player chooses to stand, or goes bust, the dealer will then deal their own hand according to the house rules.

Card values:
 - Your hand value is the sum of the individual card values.
 - All picture cards (J, Q, K) are worth 10.
 - All non-picture cards are worth their face values. [2c] = 2, [7s] = 7, etc.
 - Aces are worth 1 OR 11, depending on which one is closer to 21, and not bust.
 for example: if your hand is [4c, As], you have 4 + 11 = 15. 
 You may choose to hit, and receive a Jc, making your hand [4c, As, Jc] = 4 + 1 + 10 = 15. 
 Note how the Ace changes to a value of 1; you avoid going bust and still have 15.
 


 


