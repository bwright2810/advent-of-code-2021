
def main():
  file = open('input9_1.txt', 'r')
  lines = filter(lambda l: bool(l.strip()), file.readlines())

  grid = list()
  for line in lines:
    nums = [int(char) for char in filter(lambda c: bool(c.strip()), [char for char in line])]
    grid.append(nums)

  lows = []

  for y, row in enumerate(grid):
    for x, num in enumerate(row):
      adjacents = get_adjacents(grid, row, y, x)
      is_low_point = all(map(lambda a: num < a, [a[0] for a in adjacents]))
      if (is_low_point):
        lows.append([num, y, x])
  
  basins = []
  for low in lows:
    explored_map = dict()
    basin_total = explore_basin(low, explored_map, grid)
    basins.append(basin_total)

  basins.sort(reverse=True)

  print(basins[0] * basins[1] * basins[2])

def explore_basin(point, explored_map, grid):
  [val, y, x] = point
  
  if (y in explored_map and x in explored_map[y]):
    return 0
  elif val == 9:
    return 0
  
  if y not in explored_map:
    explored_map[y] = dict()
  explored_map[y][x] = True

  adj_total = 0
  adjacents = get_adjacents(grid, grid[y], y, x)
  for a in adjacents:
    adj_total = adj_total + explore_basin(a, explored_map, grid)
  return 1 + adj_total

def get_adjacents(grid, row, y, x):
  gridend = len(grid) - 1
  rowend = len(row) - 1
  
  if y == 0:
    if x == 0:
      adjacents = [[grid[1][0], 1, 0], [grid[0][1], 0, 1]]
    elif x == rowend:
      adjacents = [[grid[0][rowend - 1], 0, rowend - 1], [grid[1][rowend], 1, rowend]]
    else:
      adjacents = [[grid[0][x - 1], 0, x - 1], [grid[0][x + 1], 0, x + 1], [grid[1][x], 1, x]]
  elif y == gridend:
    if x == 0:
      adjacents = [[grid[gridend - 1][0], gridend - 1, 0], [grid[gridend][1], gridend, 1]]
    elif x == rowend:
      adjacents = [[grid[gridend][rowend - 1], gridend, rowend - 1], [grid[gridend - 1][rowend], gridend - 1, rowend]]
    else:
      adjacents = [[grid[gridend][x - 1], gridend, x - 1], [grid[gridend][x + 1], gridend, x + 1], [grid[gridend - 1][x], gridend -1, x]]
  elif x == 0:
    adjacents = [[grid[y - 1][x], y - 1, x], [grid[y + 1][x], y + 1, x], [grid[y][x + 1], y, x + 1]]
  elif x == rowend:
    adjacents = [[grid[y][x - 1], y, x - 1], [grid[y - 1][x], y - 1, x], [grid[y + 1][x], y + 1, x]]
  else:
    adjacents = [
      [grid[y][x - 1], y, x - 1],
      [grid[y][x + 1], y, x + 1], 
      [grid[y - 1][x], y - 1, x], 
      [grid[y + 1][x], y + 1, x]
    ]
  
  return adjacents

if __name__ == '__main__':
  main()