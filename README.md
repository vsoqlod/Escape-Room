# Escape-Room

The project simulates an escape room game where the user must open a series of three doors chosen randomly from several different types of doors. The Door interface defines abstract methods that must be implemented in each subclass of door. These methods include examining the door, providing menu options for unlocking the door, attempting to unlock the door, checking if the door is unlocked, providing a clue if unsuccessful, and providing a congratulatory message if successful.

## Features:
- Simulates an escape room game with three doors that are randomly chosen.
- Includes a Door interface and three different types of doors: BasicDoor, LockedDoor, and ComboDoor.
- Each door type has unique attributes and requires different methods to unlock.
- Provides a string description of the door and menu options for unlocking it.
- Tracks the user's attempts and provides clues if unsuccessful.
