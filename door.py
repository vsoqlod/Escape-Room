from abc import abstractmethod
import string
class Door:
  """Interface of the door that contains elements that will represent in escape room."""
  
  @abstractmethod
  def examine_door(self) -> string:
    """Returns a describtion of the door."""
    pass
    
  @abstractmethod
  def menu_options(self) -> string:
    """Returns a menu options inorder to unlock the door."""
    pass
    
  @abstractmethod
  def get_menu_max(self) -> int:
    """Returns the number of options of menu."""
    pass
    
  @abstractmethod
  def attempt(self, option) -> string:
    """Returns the attempt description of user pertaining to user's option selection."""
    pass
    
  @abstractmethod
  def is_unlocked(self) -> bool:
    """Return true or false when door is unlocked or not."""
    pass
    
  @abstractmethod
  def clue(self) -> string:
    """Returns description of the hint when user fails to unlock the door."""
    pass
    
  @abstractmethod
  def success(self) -> string:
    """Returns congratulatory message when user unlocked the door."""
    pass
    
    