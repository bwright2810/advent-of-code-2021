
def main():
  file = open('input10_1.txt', 'r')
  lines = [l.strip('\n') for l in filter(lambda l: bool(l.strip()), file.readlines())]
  # line = '[({(<(())[]>[[{[]{<()<>>'

  all_scores = []
  for line in lines:
    curlies, parens, squares, arrows = 0, 0, 0, 0
    symbols = []
    illegal_char_found = False
    for c in line:
      if c == '{':
        curlies = curlies + 1
        symbols.append('curly')
      elif c == '(':
        parens = parens + 1
        symbols.append('paren')
      elif c == '[':
        squares = squares + 1
        symbols.append('square')
      elif c == '<':
        arrows = arrows + 1
        symbols.append('arrow')
      elif c == '}':
        if symbols[-1] != 'curly':
          illegal_char_found = True
          break
        else:
          symbols.pop()
          curlies = curlies - 1
      elif c == ')':
        if symbols[-1] != 'paren':
          illegal_char_found = True
          break
        else:
          symbols.pop()
          parens = parens - 1
      elif c == ']':
        if symbols[-1] != 'square':
          illegal_char_found = True
          break
        else:
          symbols.pop()
          squares = squares - 1
      elif c == '>':
        if symbols[-1] != 'arrow':
          illegal_char_found = True
          break
        else:
          symbols.pop()
          arrows = arrows - 1
    
    if illegal_char_found:
      continue

    close_map = { 'curly': '}', 'paren': ')', 'square': ']', 'arrow': '>'}
    score_map = { ')': 1, ']': 2, '}': 3, '>': 4 }
    total_score = 0
    added = ''
    ct_to_close = len(symbols)
    while (ct_to_close > 0):
      to_close = symbols.pop()
      closing_sym = close_map[to_close]
      added = added + closing_sym
      total_score = (total_score * 5) + score_map[closing_sym]
      ct_to_close = ct_to_close - 1
    
    # print(added)
    # print(total_score)
    all_scores.append(total_score)
  
  # get middle score
  all_scores.sort()
  mid_idx = int(len(all_scores) / 2)
  print(all_scores[mid_idx])

if __name__ == '__main__':
  main()