ex = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

ex2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

def main():
  file = open('input12.txt', 'r')
  lines = [l.strip('\n') for l in filter(lambda l: bool(l.strip()), file.readlines())]
  # lines = [l.strip('\n') for l in filter(lambda l: bool(l.strip()), ex2.split('\n'))]

  full_map = dict()
  for line in lines:
    [a, b] = line.split('-')
    full_map[a] = full_map.get(a, dict()) | { b: True }
    full_map[b] = full_map.get(b, dict()) | { a: True }
  
  path_trees = explore('start', [], full_map, {})

  paths = []
  for path_tree in path_trees:
    dig_for_path(path_tree, paths)

  print(paths)

  print(f'There are {len(paths)} paths')

def explore(point: str, curr_path: list, full_map: dict, small_caves_explored: dict):
  if point == 'start' and curr_path:
    return []

  if point in small_caves_explored and small_caves_explored.get('double-small-used', False):
    return []

  curr_path.append(point)

  if point == 'end':
    return curr_path

  if point.islower():
    if point in small_caves_explored:
      small_caves_explored['double-small-used'] = True
    else:
      small_caves_explored[point] = True
  
  connections = full_map[point]
  explored = [explore(conn, list(curr_path), full_map, dict(small_caves_explored)) for conn in connections]
  return list(filter(lambda p: p, explored))

def dig_for_path(arr, paths):
  for el in arr:
    if len(el) > 1 and type(el[0]) == str:
      paths.append(el)
    else:
      dig_for_path(el, paths) 

if __name__ == '__main__':
  main()