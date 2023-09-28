# Dark-Souls-Death-Counter
This is a standalone application for counting deaths in the popular game "Dark Souls".
Currently it only supports "Dark Souls Remastered".

## Installation
1. Place the released executable in the game's folder.
2. Done.

### Alternatively
  Build an executable using the source code. For this you'll need **python** and **pyinstaller** (or any other module you're familiar with that can build a single file executable) installed on your machine.
  For pyisntaller run the following command:

  *pyinstaller.exe --onefile death_counter.py*

And put the executable in the game's folder.

## Usage
After putting the executable in the game's folder, run the executable as **_adminsitrator_**. It should automatically start the game too. For ease of use, you can make a shortcut for the executable.
The number of times you died is stored in the counter.txt file in the game's folder.

## Known issues / Things that will be improved
1. Only supports 1920x1080 resolution.
2. Only works if the game is displayed on your main monitor.
3. Counts overall death regardless of save/character.
4. I want to add an overlay and display the deaths that way. Not in a terminal.
