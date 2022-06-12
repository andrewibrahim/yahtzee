#!/usr/bin/env python3

import random

class Dice:

  def __init__(self, sides):
    self.sides = sides
    self.value = 0
    self.keep = False
    return

  def roll(self):
    if self.keep == False:
      self.value = random.randint(1,self.sides)
      return

  def toggle(self):
    if self.keep == True:
      self.keep = False
    else:
      self.keep = True
  
  def toString(self):
    s = str(self.value)
    if self.keep:
      s = s + "*"
    return s

  def toValue(self):
    return self.value

class Hand:
  def __init__ (self):
    self.dice_count = 5
    self.dice_total = 0
    self.max_rolls = 3
    self.rolls_count = 0
    self.dice = []
    for x in range(self.dice_count):
      self.dice.append(Dice(5))
    return

  def roll(self):
    self.dice_total = 0
    for x in range(self.dice_count):
      self.dice[x].roll()
      self.dice_total = self.dice_total + self.dice[x].toValue()
      
    self.toString()
    return

  def toString(self):
    for x in range(self.dice_count):
      print('Your Dice ' + str(x + 1) + ' is: ' + self.dice[x].toString() )
    return

  def reset(self):
    for x in range(self.dice_count):
      self.dice[x].keep = False
 

class Player:

  def __init__(self, namePassed):
    self.total = 0
    self.name = namePassed
    self.hand = Hand()
    return

  def addScore(self, s):
    self.total = self.total + s
    return

  def score(self):
    return self.total

  def turn(self):
    print("\nPlayer " + self.name + " turn starting!")
    self.hand.roll_count = 0
    self.hand.reset()
    command = "Y"
    while (self.hand.roll_count < self.hand.max_rolls):
      if command == "Y":
        self.hand.roll()
        self.hand.roll_count = self.hand.roll_count + 1
      elif command == "1":
        self.hand.dice[0].toggle()
        self.hand.toString()
      elif command == "2":
        self.hand.dice[1].toggle()
        self.hand.toString()
      elif command == "3":
        self.hand.dice[2].toggle()
        self.hand.toString()
      elif command == "4":
        self.hand.dice[3].toggle()
        self.hand.toString()
      elif command == "5":
        self.hand.dice[4].toggle()
        self.hand.toString()
      else:
        print("End of turn!")
        break
        
      if self.hand.roll_count < self.hand.max_rolls:
        print("You have " + str(self.hand.max_rolls - self.hand.roll_count) + " rolls remaining.")
        command = input('Roll again? (Y)es or (N)o: ' )
        if command == "N":
          print("End of turn!")
          break

def main():
  print("Welcome to the Yahtzee game!")

  player_count = int(input("How many people are playing?: "))
  players = []
  for x in range(player_count):
    name_entered = input("Enter player " + str(x + 1) + " name: ")
    players.append(Player(name_entered))

  while True:
    command = input('Enter your command (R)ound or e(X)it: ' )
    if command == "X":
      print("Thanks for playing!")
      break   
      
    for z in range(player_count):
      players[z].turn()

def random_number():
  x = random.randint(0,6)
  return (x)


if __name__ == "__main__":
  main()