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
    break
  
  count = 0
  for y in paper.keys():
    for x in paper[y].keys():
      count = count + 1
  
  print(count)

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

if __name__ == '__main__':
    main()