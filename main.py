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
      self.dice.append(Dice(6))
    return
  
  def roll(self):
    self.dice_total = 0
        
    self.dice[0].value = 2
    self.dice[1].value = 1
    self.dice[2].value = 4
    self.dice[3].value = 5
    self.dice[4].value = 3
    
    for x in range(self.dice_count):
#      self.dice[x].roll()
      self.dice_total = self.dice_total + self.dice[x].toValue()

    self.dice.sort(key = lambda x: x.value)
    
    self.toString()
    return

  
  def toString(self):
    print("\n")
    for x in range(self.dice_count):
      print('Your Dice ' + str(x + 1) + ' is: ' + self.dice[x].toString() )
    return

  def reset(self):
    for x in range(self.dice_count):
      self.dice[x].keep = False

  def calcScore(self, val):
    calcVal = 0
    for x in range(self.dice_count):
      if self.dice[x].toValue() == val:
        calcVal = calcVal + val
    return calcVal

  def countValue(self,val):
    countVal = 0
    for x in range(self.dice_count):
      if self.dice[x].toValue() == val:
        countVal = countVal + 1
    return countVal

  
  def calcThreeOfaKind(self):
    calcVal = 0
    for x in range(self.dice_count):
        calcVal = calcVal + self.dice[x].value

    count = 0
    for x in range(1,7):
      count = self.countValue(x)
      if count >= 3:
        return calcVal
      
    return 0

  def calcFourOfaKind(self):
    calcVal = 0
    for x in range(self.dice_count):
        calcVal = calcVal + self.dice[x].value

    count = 0
    for x in range(1,7):
      count = self.countValue(x)
      if count >= 4:
        return calcVal
      
    return 0

  def calcFullHouse(self):
    calcVal = 25

    count = 0
    for x in range(1,7):
      count = self.countValue(x)
      if count == 3:
        count2 = 0
        for y in range(1,7):
          count2 = self.countValue(y)
          if count2 == 2 and x != y:
            return calcVal
    
    return 0

  def calcSmStraight(self):
    calcVal = 30

    count = 1
    for x in range(0, len(self.dice)-1):
      if (self.dice[x].value + 1) == self.dice[x+1].value:
        count = count + 1

    if count >= 4:
      return calcVal
    else:
      return 0
    
  def calcLgStraight(self):
    calcVal = 40

    count = 1
    for x in range(0, len(self.dice)-1):
      if (self.dice[x].value + 1) == self.dice[x+1].value:
        count = count + 1

    if count == 5:
      return calcVal
    else:
      return 0
  
  def calcFiveOfaKind(self):
    count = 0
    for x in range(1,7):
      count = self.countValue(x)
      if count == 5:
        return 50
      
    return 0

  
  def calcChance(self):
    calcVal = 0
    for x in range(self.dice_count):
        calcVal = calcVal + self.dice[x].value
    return calcVal
  
  def calcRow(self, row):
    if row == "a":
      return self.calcScore(1)
    elif row == "b":
      return self.calcScore(2)
    elif row == "c":
      return self.calcScore(3)
    elif row == "d":
      return self.calcScore(4)
    elif row == "e":
      return self.calcScore(5)
    elif row == "f":
      return self.calcScore(6)
    elif row == "g":
      return self.calcThreeOfaKind()
    elif row == "h":
      return self.calcFourOfaKind()
    elif row == "i":
      return self.calcFullHouse()
    elif row == "j":
      return self.calcSmStraight()
    elif row == "k":
      return self.calcLgStraight()
    elif row == "l":
      return self.calcFiveOfaKind()
    elif row == "m":
      return self.calcChance()
    else:
      return 100


class Player:

  def __init__(self, namePassed):
    self.total = 0
    self.name = namePassed
    self.hand = Hand()
    self.score = Score()
    
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
    command = "R"
    while (self.hand.roll_count <= self.hand.max_rolls):
      if command == "R" or command == "r":
        if self.hand.roll_count < self.hand.max_rolls:
          self.hand.roll()
          self.hand.roll_count = self.hand.roll_count + 1
        else:
          print("No rolls left.")
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
      elif (command in "abcdefghijklm") and len(command) == 1:
        self.score.setScore(command,self.hand.calcRow(command))
        break
      else:
        print("Please enter a valid input.")
        
      if self.hand.roll_count <= self.hand.max_rolls:
        self.score.toString(self.hand)
        print("You have " + str(self.hand.max_rolls - self.hand.roll_count) + " rolls remaining.")
        command = input('(R)oll or (a-m): ' )

    self.score.toString(self.hand)
    
class Score:
  def __init__(self):
    self.upper_aces = -1
    self.upper_twos = -1
    self.upper_threes = -1
    self.upper_fours = -1
    self.upper_fives = -1
    self.upper_sixes = -1
    self.upper_bonus = 35
    self.lower_three = -1
    self.lower_four = -1
    self.lower_house = -1
    self.lower_small = -1
    self.lower_large = -1
    self.lower_yahtzee = -1
    self.lower_chance = -1

  def formatScore(self, row, num, hand):
    if num < 0:
      return "+" + str(hand.calcRow(row))
    else:
      return str(num)

  def setScore(self, row, val):
    if row == "a":
      self.upper_aces = val
    elif row == "b":
      self.upper_twos = val
    elif row == "c":
      self.upper_threes = val
    elif row == "d":
      self.upper_fours = val
    elif row == "e":
      self.upper_fives = val
    elif row == "f":
      self.upper_sixes = val
    elif row == "g":
      self.lower_three = val
    elif row == "h":
      self.lower_four = val
    elif row == "i":
      self.lower_house = val
    elif row == "j":
      self.lower_small = val
    elif row == "k":
      self.lower_large = val
    elif row == "l":
      self.lower_yahtzee = val
    elif row == "m":
      self.lower_chance = val

  def calcScore(self, val):
    if val < 0:
      return 0
    else:
      return val
  
  def calcUpperTotalScore(self):
    total = self.calcScore(self.upper_aces) + self.calcScore(self.upper_twos) + self.calcScore(self.upper_threes) + self.calcScore(self.upper_fours) + self.calcScore(self.upper_fives) + self.calcScore(self.upper_sixes)
    return total

  def calcUpperBonus(self):
    if self.calcUpperTotalScore() >= 63:
      return self.upper_bonus
    else:
      return 0
  
  def calcLowerTotal(self):
    total = self.calcScore(self.lower_three) + self.calcScore(self.lower_four) + self.calcScore(self.lower_house) + self.calcScore(self.lower_small) + self.calcScore(self.lower_large) + self.calcScore(self.lower_yahtzee) + self.calcScore(self.lower_chance)
    return total
  
    
  def toString(self, hand):
    print("-------------------------------------")
    print("[a] Aces:        " + self.formatScore("a", self.upper_aces, hand))
    print("[b] Twos:        " + self.formatScore("b", self.upper_twos, hand))
    print("[c] Threes:      " + self.formatScore("c", self.upper_threes, hand))
    print("[d] Fours:       " + self.formatScore("d", self.upper_fours, hand))
    print("[e] Fives:       " + self.formatScore("e", self.upper_fives, hand))
    print("[f] Sixes:       " + self.formatScore("f", self.upper_sixes, hand))
    print("-------------------------------------")
    print("Total:           " + str(self.calcUpperTotalScore()))
    print("Bonus:           " + str(self.calcUpperBonus()))
    print("Upper Total:     " + str(self.calcUpperTotalScore() + self.calcUpperBonus()))
    print("-------------------------------------")
    print("[g] 3 of a kind: " + self.formatScore("g", self.lower_three, hand) )
    print("[h] 4 of a kind: " + self.formatScore("h", self.lower_four, hand))
    print("[i] Full House:  " + self.formatScore("i", self.lower_house, hand))
    print("[j] Sm Straight: " + self.formatScore("j", self.lower_small, hand))
    print("[k] Lg Straight: " + self.formatScore("k", self.lower_large, hand))
    print("[l] YAHTZEE!:    " + self.formatScore("l", self.lower_yahtzee, hand))
    print("[m] Chance:      " + self.formatScore("m", self.lower_chance, hand) )
    print("-------------------------------------")
    print("Lower Total:     " + str(self.calcLowerTotal()))
    print("Upper Total:     " + str(self.calcUpperTotalScore() + self.calcUpperBonus()))
    print("Grand Total:     " + str(self.calcLowerTotal() + self.calcUpperTotalScore() + self.calcUpperBonus()))
    print("-------------------------------------")

    

def main():
  print("Welcome to the Yahtzee game!")

  player_count = int(input("How many people are playing?: "))
  players = []
  for x in range(player_count):
    name_entered = input("Enter player " + str(x + 1) + " name: ")
    players.append(Player(name_entered))

  while True:
    command = input('Enter your command (R)ound or e(X)it: ' )
    if command == "X" or command == "x":
      print("Thanks for playing!")
      break   
    elif command == "R" or command == "r":  
      for z in range(player_count):
        players[z].turn()
    else:
      print("Please enter a valid input.")

def random_number():
  x = random.randint(0,6)
  return (x)


if __name__ == "__main__":
  main()