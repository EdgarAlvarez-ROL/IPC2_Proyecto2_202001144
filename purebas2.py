from glob import glob
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# matrix = [
#   [1, 0, 0, 1],
#   [1, 0, 0, 1],
#   [1, 0, 0, 1],
#   [1, 1, 1, 1]
# ]


matrix = []
x = 0
y = 0
# start = grid.node(0, 0)
# end = grid.node(3, 0)

def hacerMatrix(todo_papa, end, start):
  global matrix
  matrix = []
  temp = []
  for cosas in todo_papa:
    for x in cosas:
      if x == '*':
        x = 0
      elif x == ' ':
        x = 1
      elif x == 'M':
        x = 0
      elif x == 'R':
        x = 0
      elif x == 'E':
        x = 1
      elif x == 'C':
        x = 1
      temp.append(x)

    matrix.append(temp)
    temp = []

  # print(matrix)

  usar()



def usar():
  global matrix, x, y
  grid = Grid(matrix=matrix)
  start = grid.node(0, 0)
  end = grid.node(3, 0)
  # h = horizontalMovement.always
  finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
  path, runs = finder.find_path(start, end, grid)
  print('operations:', runs, 'path length:', len(path))
  print(grid.grid_str(path=path, start=start, end=end))