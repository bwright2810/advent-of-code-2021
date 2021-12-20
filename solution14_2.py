import time

def main():
  file = open('testinput14.txt', 'r')
  # file = open('input14.txt', 'r')
  lines = [l.strip('\n') for l in filter(lambda l: bool(l.strip()), file.readlines())]

  template = lines[0]
  pi_rules = filter(lambda l: '->' in l, lines)
  pi_dict = {p[0]: p[1] for p in [r.split(' -> ') for r in pi_rules]}

  temp = template
  print("starting steps")
  for step in range(40):
    print(f'Processing step {step + 1}')
    start = time.perf_counter()
    new_s = ''
    pair = ['', '']
    for i in range(len(temp)):
      c = temp[i]
      if pair[1] == '':
        pair[1] = c
        new_s = new_s + c
      else:
        pair[0] = pair[1]
        pair[1] = c
        pair_s = pair[0] + pair[1]
        new_s = new_s + (pi_dict[pair_s] + c if (pair_s) in pi_dict else c)
    temp = new_s
    # print(temp)
    print("finished step")
    print(str(time.perf_counter() - start))

  ct_dict = {}
  for c in temp:
    ct_dict[c] = ct_dict.get(c, 0) + 1
  
  (first_char, first_ct) = list(ct_dict.items())[0]
  hi = (first_char, first_ct)
  low = (first_char, first_ct)

  for (char, ct) in ct_dict.items():
    if ct > hi[1]: hi = (char, ct)
    if ct < low[1]: low = (char, ct)
  
  print(hi[1] - low[1])

if __name__ == '__main__':
    main()