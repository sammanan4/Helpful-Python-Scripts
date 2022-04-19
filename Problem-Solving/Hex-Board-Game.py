'''
Question link: https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942527#problem


This problem was inspired by a board game called Hex, designed independently by Piet Hein and John Nash. 
It has a similar idea, but does not assume you have played Hex.

This game is played on an N×N board, where each cell is a hexagon.
There are two players: Red side (using red stones) and Blue side (using blue stones). 
The board starts empty, and the two players take turns placing a stone of their color on a single cell within the overall playing board. 
Each player can place their stone on any cell not occupied by another stone of any color. 
There is no requirement that a stone must be placed beside another stone of the same color. 
The player to start first is determined randomly (with equal probability among the two players).

The upper side and lower sides of the board are marked as red, and the other two sides are marked as blue. 
For each player, the goal of the game is to connect the two sides marked with their color by forming a connected path using stones of their color. 
The first player to achieve this wins. Note that the four corners are considered connected to both colors.

The game ends immediately when one player wins.

Given a game state, help someone new to the game determine the status of a game board. Say one of the following:

    Impossible: If it was impossible for two players to follow the rules and to have arrived at that game state.
    Red wins: If the player playing the red stones has won.
    Blue wins: If the player playing the blue stones has won.
    Nobody wins: If nobody has yet won the game. Note that a game of Hex cannot end without a winner!

Note that in any impossible state, the only correct answer is Impossible, 
even if red or blue has formed a connected path of stones linking the opposing sides of the board marked by their colors.


The first line of input gives the number of test cases, T. 
T test cases follow. Each test case start with the size of the side of the board, N. 
This is followed by a board of N rows and N columns consisting of only B, R, and . characters. 
B indicates a cell occupied by blue stone, 
R indicates a cell occupied by red stone, 
and . indicates an empty cell.
Output

For each test case, output one line containing 
Case #x: y, where x is the case number (starting from 1) and y is the status of the game board. 
It can be 
"Impossible", 
"Blue wins", 
"Red wins", 
or "Nobody wins" (excluding the quotes). 
Note that the judge is case-sensitive, so answers of "impossible", "blue wins", "red wins", and "nobody wins" will be judged incorrect.

Sample Input:
7
1
.
1
B
1
R
2
BR
BB
4
BBBB
BBB.
RRR.
RRRR
4
BBBB
BBBB
RRR.
RRRR
6
......
..R...
BBBBBB
..R.R.
..RR..
......

Sample Output:
Case #1: Nobody wins
Case #2: Blue wins
Case #3: Red wins
Case #4: Impossible
Case #5: Blue wins
Case #6: Impossible
Case #7: Blue wins





Status: Error
This case considered as nobody wins but seems like impossible since red has 2 moves and blue has none
2
.R
R.
'''
from collections import Counter

def has_won(player, board, N, row=0, col=0):
    if player == 'B':
        if col==N-1:
            if  board[row][col] != 'B':
                return False
            else:
                board[row][col] = 'M'
                return True

        for crow in range(row, N):
            if board[crow][col] == 'B':
                board[crow][col] = 'M'
            else:
                continue
            if (
                # top right
                (col + 1 < N and crow - 1 >= 0 and board[crow-1][col+1] == 'B' and has_won(player, board, N, crow - 1, col + 1)) or 
                # right
                (col + 1 < N and board[crow][col+1] == 'B' and has_won(player, board, N, crow, col + 1)) or
                # top
                (crow - 1 >= 0 and board[crow-1][col] == 'B' and has_won(player, board, N, crow - 1, col)) or
                # bottom
                (crow + 1 < N and board[crow+1][col] == 'B' and has_won(player, board, N, crow + 1, col)) 
            ):
                return True
            if not (row==0 and col==0):
                break
        return False
    if player == 'R':
        if row==N-1:
            if board[row][col] != 'R':
                return False
            else:
                board[row][col] = 'M'
                return True

        for ccol in range(col, N):
            if board[row][ccol] == 'R':
                board[row][ccol] = 'M'
            else:
                continue
            if (
                # bottom left
                (row + 1 < N and ccol - 1 >= 0 and board[row+1][ccol-1] == 'R' and has_won(player, board, N, row + 1, ccol - 1)) or
                # bottom 
                (row + 1 < N and board[row+1][ccol] == 'R' and has_won(player, board, N, row + 1, ccol)) or
                # left
                (ccol - 1 >= 0 and board[row][ccol-1] == 'R' and has_won(player, board, N, row, ccol - 1)) or
                # right
                (ccol + 1 < N and board[row][ccol+1] == 'R' and has_won(player, board, N, row, ccol + 1))
            ):
                return True
            if not (row==0 and col==0):
                break
        return False
                
        
if __name__=="__main__":
  T = int(input())
  l = []
  import pprint
  for i in range(1, T+1):
      N = int(input())
      board = []
      blues = 0
      reds = 0
      for j in range(N):
          board.append(list(input()))
          counter = Counter(board[-1])
          blues+=counter.get('B', 0)
          reds+=counter.get('R', 0)
      # print(f"{blues=} {reds=}")
      if (blues != 0 and reds != 0) and (blues - reds) not in (1, 0, -1):
          # l.append(f'Case #{i}: Impossible')
          print(f'Case #{i}: Impossible')
          continue
      # print(f"{blues=} {reds=}")
      board_copy1 = [row[:] for row in board]
      board_copy2 = [row[:] for row in board]
      b_won = has_won('B', board_copy1, N)
      b_won1 = False
      if b_won:
        b_won1 = has_won('B', board_copy1, N)
      r_won = has_won('R', board_copy2, N)
      r_won1 = False
      if r_won:
        r_won1 = has_won('R', board_copy2, N)
      if (
          (b_won and r_won) or 
          (b_won and b_won1 and N!=1) or 
          (r_won and r_won1 and N!=1) or
          (b_won and blues < reds) or
          (r_won and reds < blues)
      ):
          print(f'Case #{i}: Impossible')
      elif b_won:
          print(f'Case #{i}: Blue wins')
      elif r_won:
          print(f'Case #{i}: Red wins')
      else:
          print(f'Case #{i}: Nobody wins')



