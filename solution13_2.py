from functools import reduce
import copy

def main():
  # file = open('testinput13.txt', 'r')
  file = open('input13.txt', 'r')
  lines = [l.strip('\n') for l in filter(lambda l: bool(l.strip()), file.readlines())]

  points, fold_lines = [], []
  for line in lines:
      (points, fold_lines)[line.startswith("fold")].append(line)
    
  paper = {}
  for point in points:
    [x, y] = map(lambda pt: int(pt), point.split(','))
    paper[y] = paper.get(y, dict()) | { x: True }
  
  for fold_line in fold_lines:
    [dir, val] = map(lambda n: int(n) if n.isnumeric() else n, fold_line.split("fold along ")[1].split("="))
    paper = fold(paper, dir, val)
  
  count = 0
  for y in paper.keys():
    for x in paper[y].keys():
      count = count + 1
  
  print_paper(paper)

def fold(paper, dir: str, val: int):
  folded = copy.deepcopy(paper)
  if dir == 'y':
    after_fold = filter(lambda y: y > val, paper.keys())
    for y in after_fold:
      for x in paper[y].keys():
        new_y = val - (y - val)
        folded[new_y] = folded.get(new_y, dict()) | { x: True }
        folded[y].pop(x)
  else:
    for y in paper.keys():
      after_fold = filter(lambda x: x > val, paper[y].keys())
      for x in after_fold:
        new_x = val - (x - val)
        folded[y][new_x] = True
        folded[y].pop(x)
  return folded
  
def print_paper(paper):
  largest_y_with_value = max(filter(lambda y: len(list(filter(lambda x: paper[y][x], paper[y].keys()))) > 0, paper.keys()))
  largest_x_with_value = max(reduce(lambda a, b: a + b, [list(filter(lambda x: paper[y][x], paper[y].keys())) for y in paper.keys()]))

  for y in range(0, largest_y_with_value + 1):
    row = ''
    for x in range(0, largest_x_with_value + 1):
      row = row + ('#' if y in paper and x in paper[y] else '.')
    print(row)

if __name__ == '__main__':
    main()