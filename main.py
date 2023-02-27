"""
Gabriel Quezada, Thuan Nguyen, Jae Bum Jang
Fall 2022, 10/25
Lab 10 - Group 17

This program is a simulation of an escape room where user has to open series of three different types of doors that randomly displayed.
"""

import basic_door
import combo_door
import locked_door
import random
import check_input

def open_door(door):
  
  """General operation of opening door. Pass in a door object which user will unlock. Introduce the type of the door, prompt user a menu options pertaining to the type of door, display attempt toward the door from user input, give user a clue and let them try again until the unlock the door using while loop, display success message when user unlock the door.
  Args: 
    door(class): different types of door that imported. """
  
  print(door.examine_door())
  print(door.menu_options())
  choice = check_input.get_int_range("", 1, door.get_menu_max())
  print(door.attempt(choice))
  while door.is_unlocked() != True:
    print(door.clue())
    choice = check_input.get_int_range("", 1, door.get_menu_max())
    print(door.attempt(choice))
  print(door.success())

def main():
  
  """Prompt user to the escape room, repeat the operation using for loop until they unlock 3 different types of door, randomize the order using random function. Exit for loop when user unlock all 3 types of door and display celebration message then program terminates."""
  
  print("Welcome to the Escape Room. You must unlock 3 doors to escape...")
  for time in range(3):
    basic = basic_door.BasicDoor()
    combo = combo_door.ComboDoor()
    locked = locked_door.LockedDoor()
    random_door = random.choice([basic, combo, locked])
    open_door(random_door)
  print("Congratulations! You escaped...this time.")

main()
