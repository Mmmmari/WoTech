import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    System.out.println("Hello! Welcome to a game of Tic-Tac-Toe!");
    System.out.println("First player will be X and the second player will be O. X player can start. Good luck!");

    char[][] grid = {   // creating 3x3 grid
      {'-', '-', '-'},  // each item in the array is a char '-'
      {'-', '-', '-'},
      {'-', '-', '-'}
    };

    Scanner scanner = new Scanner(System.in);
    char playerO = 'O';
    char playerX = 'X';
    
    boolean gameOver = false;
    boolean gameTied = false;
    
    char activePlayer = playerO;
    
    while (!gameOver){
      printBoard(grid);
      activePlayer = getActivePlayer(activePlayer, playerX, playerO);
      System.out.println("Player " + activePlayer + " please enter the row number (1, 2, or 3) and the column number (1, 2, or 3) of the cell you want to place your symbol in: ");
      int row = getInput("Row", scanner);
      int column = getInput("Column", scanner);

      if (checkFreeSpace(row, column, grid) == false){
        System.out.println("This cell is already occupied. Please choose another cell.");
        activePlayer = getActivePlayer(activePlayer, playerX, playerO);
        continue; //It goes back to the top of the while loop
      } 

      grid[row][column] = activePlayer;
      gameOver = checkIfWon(grid);
      if (gameOver == false){
        gameTied = checkIfTie(grid);
        if (gameTied == true){
          System.out.println("Game over! No one won!");
          gameOver = true;
        }
      }
      
    }
    if (gameTied != true){
      printBoard(grid);
      System.out.println("Congratulations! Player " + activePlayer + " wins!");
    }
  }  


  public static int getInput(String prompt, Scanner scanner){
    while (true){
      System.out.println(prompt + ": ");
      int input = scanner.nextInt();
      if (input < 1 || input > 3){
        System.out.println("Invalid input. Please enter a valid " + prompt +  " number (1, 2, or 3): ");
      } else {
        return input-1;
      }
    }
  }


  public static boolean checkFreeSpace(int row, int column, char[][] grid){

    boolean freeSpace = false;
    if (grid[row][column] == '-'){
      freeSpace = true;
    }
    return freeSpace;  
  }


  public static char getActivePlayer (char previousPlayer, char playerX, char playerO){
    if (previousPlayer == playerX){
      return playerO;
    } else {
      return playerX;
    }
  }


  public static void printBoard(char[][] grid){

    System.out.println("=====");
    for (int i = 0; i < grid.length; i++){
      for (int j = 0; j < grid[i].length; j++){
        System.out.print(grid[i][j] + " ");
      }
      System.out.println();
    }
    System.out.println("=====");
  }


  public static boolean checkIfWon(char[][] grid){
    // Checking rows
    if (grid[0][0] == grid[0][1] && grid[0][1] == grid[0][2] && grid[0][0] != '-'){
      return true;
    }
    if (grid[1][0] == grid[1][1] && grid[1][1] == grid[1][2] && grid[1][0] != '-'){
      return true;
    }
    if (grid[2][0] == grid[2][1] && grid[2][1] == grid[2][2] && grid[2][0] != '-'){
      return true;
    }
    // Checking columns
    if (grid[0][0] == grid[1][0] && grid[1][0] == grid[2][0] && grid[0][0] != '-'){
      return true;
    }
    if (grid[0][1] == grid[1][1] && grid[1][1] == grid[2][1] && grid[0][1] != '-'){
      return true;
    }
    if (grid[0][2] == grid[1][2] && grid[1][2] == grid[2][2] && grid[0][2] != '-'){
      return true;
    }
      // Checking diagonals
    if (grid[0][0] == grid[1][1] && grid[1][1] == grid[2][2] && grid[0][0] != '-'){
      return true;
    }
    if (grid[0][2] == grid[1][1] && grid[1][1] == grid[2][0] && grid[0][2] != '-'){
      return true;
    }
    return false;
  }

  
  public static boolean checkIfTie(char[][] grid){
    for (int i = 0; i < grid.length; i++){
      for (int j = 0; j < grid[i].length; j++){
        if (grid[i][j] == '-'){
          return false;
        }
      }
    }
    return true;
  }
}
