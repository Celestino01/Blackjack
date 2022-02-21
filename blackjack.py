import random
from replit import clear
def dealCards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculateCards(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)

def compare(userScore, computerScore):
  if userScore == computerScore:
    return "Draw"
  elif computerScore == 0:
    return "Lose, opponent has black jack"
  elif userScore == 0:
    return "Congrats! You Won!"
  elif userScore > 21:
    return "You went over 21"
  elif computerScore > 21:
    return "Opponent went over, you win"
  elif userScore > computerScore:
    return "You win"
  else:
    return "You lose"
def playGame():
  
  userHand = []
  computerHand = []
  isGameOver = False
  
  for _ in range(2):
    userHand.append(dealCards())
    computerHand.append(dealCards())
  
  while not isGameOver:
    userScore = calculateCards(userHand)
    computerScore = calculateCards(computerHand)
    
    print(f" Your cards:{userHand}, current score: {userScore}")
    print(f" Computers first hand {computerHand[0]}")
    
    if userScore == 21 or computerScore == 0 or userScore > 21:
      isGameOver = True
    else:
      userShouldDeal = input("Type 'y' to get another card, type 'n' to pass: ")
      if userShouldDeal == 'y':
        userHand.append(dealCards())
      else:
        isGameOver == True
    
  while computerScore != 0 and computerScore < 17:
    computerHand.append(dealCards())
    computerScore = calculateCards(computerHand)
  print(f" Your final hand: {userHand}, final score is {userScore}")
  print(f" Computers final hand: {computerHand}, final score is {computerScore}")
  print(compare(userScore, computerScore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == 'y':
  clear()
  playGame()
