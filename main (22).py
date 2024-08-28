# Black jack Card Game 
# 1. Your hand should not be higher than 21. If it is higher than 21, you lose.
# 2. Cards 2-10 are scored using their face value and J,Q,K are all equal to 10
# 3. Aces can be 1 or 11 (You can choose their value)
# 4. The one who has Black Jack (Ace + J/Q/K), wins.
# 5. If your score is below 21, the user is asked whether he wants to draw another card.
# 6. There is no limit to how many cards you want to draw but if your hand gets higher than 21, you lose
# 7. If the computer’s total adds up to 16 or lower, it will draw cards till the score is 17 or higher. But if its 17 or higher they stay with their hand
# 8. After drawing cards, if the computer busts (total is 21 or higher), user wins.
# 9. If computer does not bust, then you compare computer’s score with user’s score. Whoever has a higher total win
# Hints
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.

# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


# Hint 1: create a deal_card() function that uses the List below to *return* a random card.
import random
from replit import clear
from art import logo


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Hint 3 : Create a function called calculate_score() that takes a List of cards as input and returns the score.

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0  # Blackjack
    
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"

  elif user_score > computer_score:
    return "You win"
  else: 
    return "You lose"
# print(deal_card())

# Hint 2 : Deal the user and computer 2 cards each using deal_card() and append().

# user_cards = []
# computer_cards = []

# for _ in range(2):
#   user_cards.append(deal_card())
#   computer_cards.append(deal_card())



# Hint 4 : Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21

def game_initialize():
  print(logo)
# Create the user_cards list here:
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  is_game_over = False
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    # Hint 5 : If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() to add another card to the user_cards List. If no, then the game has ended.
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'hit' to get another card, type 'hold' to pass: ")
      if user_should_deal == "hit":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
    
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    game_initialize()
    
 

      
  
  
  
