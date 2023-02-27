import door
import random

class ComboDoor(door.Door):
  """Represents a combo door where locked with a combination lock, solve by spining dial a number between 1 to 10.
  Attributes: 
    correct value(int): correct dial for combo door.
    input(int): user input in escape room."""
  
  def __init__(self):
    """Initialize the correct value randomly for a door, and set the user input value."""
    self._correct_value = random.randint(1, 10)
    self._input = 0
    
  def examine_door(self):
    """Return the description of a combo door and how it operates."""
    return "You encounter a door with a combination lock, you can spin the dial to a number between 1-10."
    
  def menu_options(self):
    """Return the description of menu options of combo door."""
    return "Enter a number between 1-10:"

  def get_menu_max(self):
    """Return the maximum option number of menu."""
    return 10

  def attempt(self, option):
    """Pass the option object which will be the user's choice of dial value, then generate the attempts pertaining to the choice of value."""
    self._input = option
    return "You turn the dial to... " + str(self._input) + "."

  def is_unlocked(self):
    """Return true or false when door is unlocked or not."""
    if self._correct_value == self._input:
      return True
    else:
      return False
    
  def clue(self):
    """Returns description of the hint according to the wrong value that user inputted"""
    if self._input < self._correct_value: 
     return "Too low."
    elif self._input > self._correct_value:
      return "Too high."

  def success(self):
    """Returns congratulatory message when user unlocked the door and dialed correct value."""
    while self._input == self._correct_value:
      return "You found the correct value and opened the door."