# tic-tac-toe
Description on unittest Test Cases 
1. Test_Mark_Square;
   This test_Mark_Square case determines whether the current player's mark is appropriately marked on a square on the game board by the mark_square method.

stages;
- we should creat instance to initializing a tictactoe game
- using coordinate (0,0) to call the mark_square function
- Assert that the value in the corresponding position on the board is equal to the current player's mark (1).

2.Test_switch_player;
 This test_switch_player case determines that players 1 and 2 are appropriately switch between by the switch_player function.
 
 Stages
 - we should creat instance to initializing a tictactoe game
 - Taking a note of the first player.
 - calling  the switch_player function.
 - Assert that the current player is now the opposite of the initial player.

3. Test_play;
   This test_play case determines whether the play method successfully marks a square on the board in cases where the game hasn't ended.

stages
- we should creat instance to initializing a tictactoe game
-  using coordinate (0,0) to call the play function
-  Declaring that the player's mark (1) is equal to the value at the relevant position on the board.
-  Declaring that there is still game in it.
