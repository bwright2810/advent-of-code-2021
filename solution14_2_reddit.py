from collections import Counter
from time import perf_counter as pfc

# the bulk of this was taken from reddit user Gravitar64

def main():
  # file = open('testinput14.txt', 'r')
  file = open('input14.txt', 'r')
  lines = [l.strip('\n') for l in filter(lambda l: bool(l.strip()), file.readlines())]
  template = lines[0]
  insertions = filter(lambda l: '->' in l, lines)
  chars = Counter(template)
  template = Counter(a+b for a, b in zip(template, template[1:]))
  insertions = {x[0]: x[1] for x in [r.split(' -> ') for r in insertions]}
  for _ in range(40):
    new_temp = Counter()
    for (a, b), count in template.items():
      insert = insertions[a+b]
      new_temp[a+insert] += count
      new_temp[insert+b] += count
      chars[insert] += count
    template = new_temp
  print(max(chars.values()) - min(chars.values()))

if __name__ == '__main__':
  start = pfc()
  main()
  print(pfc() - start)