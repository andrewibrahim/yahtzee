#!/usr/bin/env python3

import random

class Dice:

  def __init__(self, sides):
    self.sides = sides
    self.value = 0
    return

  def roll(self):
    self.value = random.randint(1,self.sides)
    return

  def toString(self):
    return str(self.value)

  def toValue(self):
    return self.value
    
class Player:

  def __init__(self, namePassed):
    self.total = 0
    self.name = namePassed
    return

  def addScore(self, s):
    self.total = self.total + s
    return

  def score(self):
    return self.total


def main():
  print("Welcome to the Yahtzee game!")

  player_count = int(input("How many people are playing?: "))
  players = []
  for x in range(player_count):
    name_entered = input("Enter player " + str(x + 1) + " name: ")
    players.append(Player(name_entered))
  
  dice_count = 6
  dice = []
  for x in range(dice_count):
    dice.append(Dice(6))

  while True:
    command = input('Enter your command (R)oll or e(X)it: ' )
    if command == "X":
      print("Thanks for playing!")
      break   
      
    for z in range(player_count):
      dice_total = 0
      
      for x in range(dice_count):
        dice[x].roll()
        print('Your Dice ' + str(x + 1) + ' roll was: ' + dice[x].toString() )
        dice_total = dice_total + dice[x].toValue()
        players[z].addScore(dice[x].toValue())
        
      print("the total for this roll is: " + str(dice_total))
      print(players[z].name + " has: " + str(players[z].score()))

def random_number():
  x = random.randint(0,6)
  return (x)


if __name__ == "__main__":
  main()