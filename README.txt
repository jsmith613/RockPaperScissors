This is a personal machine learning Rock Paper Scissors Game.

There are Three Modes:
-Easy: Computer Chooses Rock, Paper or Scissors at Random
-Impossible!: Computer chooses throw that will beat yours
-Hard: Computer Predicts what you will throw based on the patterns of others

Future Improvements:
-Connection Hard.txt to a server to update as more people play
-Tracking individual player patterns as well as patterns of all players

The Code:
-The code is very sloppy and not DRY at all (This was started before I was taught python conventions)
-Hard mode predicts based on the last round
  -It looks what most players throw next considering the player's last move and the result
  -i.e. what do most players do if they just lost to rock
-Again, I apologize for the terrible code. I hope to edit this in the future so it isn't so terrible

Hard.txt explanation:
-The first digit after "move:" represents the players last throw (1-rock, 2-paper, 3-scissors)
-The second digit after "move:" represents the computers last throw (1-rock, 2-paper, 3-scissors)
-The "r,p,s" lines represent the number of times players have thrown each option
