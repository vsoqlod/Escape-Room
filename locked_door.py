import door
import random

class LockedDoor(door.Door):
  """Represents a locked door where user have to seek for hidden key.
  Attributes: 
    key_location(int): location of the hidden key to unlock the locked door.
    input(int): user input in escape room."""
  def __init__(self):
    """Initialize the correct value randomly for a door, and set the user input value."""
    self._key_location = random.choice([1, 2, 3])
    self._input = 0

  def examine_door(self):
    """Returns the description of a locked door and how it operates."""
    return "You encounter a locked door. Look around for the key..."
      
  def menu_options(self):
    """Return the description of menu options of locked door."""
    return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake door."

  def get_menu_max(self):
    """Returns the maximum value of the menu option."""
    return 3 
    
  def attempt(self, option):
    """Pass the option object which will be the user's choice of key location, then generate the attempts pertaining to the choice."""
    self._input = option
    if self._input == 1:
      return "You looked under the mat"
    elif self._input == 2:
      return "You looked under the flower pot"
    elif self._input == 3:
      return "You looked under the fake rock"  
      
  def is_unlocked(self):
    """Return true or false when door is unlocked or not."""
    if self._key_location == self._input:
      return True
    else:
      return False
      
  def clue(self):
    """Returns description of the hint according to the wrong location of the key."""
    return "Look somewhere else."
    
  def success(self):
    """Returns congratulatory message when user unlocked the door and found the correct key."""
    if self.is_unlocked() == True:
      return "You found the correct key, and you opened the door."