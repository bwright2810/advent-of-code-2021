
def main():
  file = open('input9_1.txt', 'r')
  lines = filter(lambda l: bool(l.strip()), file.readlines())

  grid = list()
  for line in lines:
    nums = [int(char) for char in filter(lambda c: bool(c.strip()), [char for char in line])]
    grid.append(nums)

  lows = []

  for y, row in enumerate(grid):
    gridend = len(grid) - 1
    for x, num in enumerate(row):
      rowend = len(row) - 1
      if y == 0:
        if x == 0:
          adjacents = [grid[1][0], grid[0][1]]
        elif x == rowend:
          adjacents = [grid[0][rowend - 1], grid[1][rowend]]
        else:
          adjacents = [grid[0][x - 1], grid[0][x + 1], grid[1][x]]
      elif y == gridend:
        if x == 0:
          adjacents = [grid[gridend - 1][0], grid[gridend][1]]
        elif x == rowend:
          adjacents = [grid[gridend][rowend - 1], grid[gridend - 1][rowend]]
        else:
          adjacents = [grid[gridend][x - 1], grid[gridend][x + 1], grid[gridend - 1][x]]
      elif x == 0:
        adjacents = [grid[y - 1][x], grid[y + 1][x], grid[y][x + 1]]
      elif x == rowend:
        adjacents = [grid[y][x - 1], grid[y - 1][x], grid[y + 1][x]]
      else:
        adjacents = [
          grid[y][x - 1], grid[y][x + 1], grid[y - 1][x], grid[y + 1][x]
        ]

      is_low_point = all(map(lambda a: num < a, adjacents))
      if (is_low_point):
        lows.append(num)
  
  total_risk = sum(map(lambda l: l + 1, lows))
  print(total_risk)

if __name__ == '__main__':
  main()