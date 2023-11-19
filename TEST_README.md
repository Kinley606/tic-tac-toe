# tic-tac-toe
Description on unittest Test Cases 

1. setup

- Before every test method in a test class, there is a unique method called setUp. 
- In this instance, it sets the game's audio mixer to its starting state.

 2. Test_Mark_Square;

- This test the mark_square function, which adds a player's mark to the Tic-Tac-Toe board at a given place.
- It utilizes self and makes two separate calls to mark_square with distinct arguments.
- 'self.assertEqual' is to verify that the board was updated accurately.

3. Test_squared_available;

- The available_square function, which determines if a square on the board is available, whether it was unoccupied.
- It uses self and verifies that a square is available both before and after marking it.
-  uses 'self.assertTrue' and 'self.assertFalse' for assertions.

4. Test_is-Board_Full;

- This  is board full function, which determines whether the Tic Tac Toe board is fully filled, is tested using this way.
- It first verifies that the board is not full, then moves through each cell, placing Player 1's mark in each one, and lastly verifies that the board is filled.


5. Test_check_win:

  - This  check_win function, which ascertains whether a player has won the game, is tested by this method.
  -  Before and after marking three consecutive squares for Player 1, it looks for a win.
   
6. TearDown;

  - This method named tearDown is invoked following every test method.
  - Here, it turns off the mixer and releases any resources it had gained from the testing.

The unit tests are only run when the script is run directly, not when it is imported as a module.
with the help of the if __name__ == '__main__': block, the test cases are executed by unittest.main(), and the test results are shown.


References 
- https://www.youtube.com/watch?si=S12ryN5bv1VyYxj_&fbclid=IwAR3EglZae-QalhJKiVTTNoNgAC8r1--dlFEw5jJbwKqri_zDAtKsu1WZ4tU&v=v1MtwCPTmBI&feature=youtu.be
- https://www.youtube.com/watch?si=8V9ULoW1nwVc8gxe&fbclid=IwAR2PbuOp4PcRZH58C3yKuEWHB7Jm-NF-O4_I5IxBTolhVNIAqXLnNLJorM8&v=96mDQrlceEk&feature=youtu.be

