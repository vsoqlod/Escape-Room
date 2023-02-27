import door
import random

class BasicDoor(door.Door):
  """Represents a basic door.
  Attributes: 
    state(int): initial state of a door.
    input(int): user input in escape room."""
  
  def __init__(self):
    """Initialize the randomized state of a door, and set the user input value."""
    
    self._state = random.choice([1, 2])
    self._input = 0
    
  def examine_door(self):
    """Return the description of a basic door and how it operates."""
    
    return "You encounter a basic door, you can either push it or pull it to open."
    
  def menu_options(self):
    """Return the description of menu options of basic door."""
    
    return "1. Push\n2. Pull"
    
  def get_menu_max(self):
    """Return the maximum option number of menu."""
    return 2 
    
  def attempt(self, option):
    """Pass the option object which will be the user's choice of the menu, generate the attempts pertaining to the choice of menu."""
    
    self._input = option
    if self._input == 1:
      return "You push the door."
      return self._input
    elif self._input == 2:
      return "You pull the door."
      return self._input
      
  def is_unlocked(self):
    """Return true or false when door is unlocked or not."""
    
    if self._state == self._input:
      return True
    else:
      return False
      
  def clue(self):
    """Returns description of the hint when user fails to unlock the door."""
    
    return "Try the other way"
    
  def success(self):
    """Returns congratulatory message when user unlocked the door."""
    
    if self.is_unlocked() == True:
      return "Congratulations, you opened the door."