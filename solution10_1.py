
def main():
  file = open('input10_1.txt', 'r')
  lines = [l.strip('\n') for l in filter(lambda l: bool(l.strip()), file.readlines())]
  # line = '{([(<{}[<>[]}>{[]{[(<()>'

  illegals = []
  for line in lines:
    curlies, parens, squares, arrows = 0, 0, 0, 0
    symbols = []
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
          illegals.append('}')
          break
        else:
          symbols.pop()
          curlies = curlies - 1
      elif c == ')':
        if symbols[-1] != 'paren':
          illegals.append(')')
          break
        else:
          symbols.pop()
          parens = parens - 1
      elif c == ']':
        if symbols[-1] != 'square':
          illegals.append(']')
          break
        else:
          symbols.pop()
          squares = squares - 1
      elif c == '>':
        if symbols[-1] != 'arrow':
          illegals.append('>')
          break
        else:
          symbols.pop()
          arrows = arrows - 1
  
  score_map = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
  print(sum(map(lambda i: score_map[i], illegals)))

if __name__ == '__main__':
  main()