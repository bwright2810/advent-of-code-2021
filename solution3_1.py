import functools

def main():
  file = open('input3_1.txt', 'r')
  lines = file.readlines()

  columns = functools.reduce(lambda a, b: to_columns(a, b), lines, {})

  gamma = ""

  for [pos, col] in columns.items():
    zeros = 0
    ones = 0
    for bit in col:
      if bit == "0":
        zeros = zeros + 1
      else:
        ones = ones + 1
    
    if ones > zeros:
      gamma = gamma + "1"
    else:
      gamma = gamma + "0"

  gamma_int = int(gamma, 2)

  epsilon = ""
  for c in gamma:
    if c == "0":
      epsilon = epsilon + "1"
    else:
      epsilon = epsilon + "0"
  epsilon_int = int(epsilon, 2)

  print(str(gamma_int * epsilon_int))

def to_columns(col_dict, line):
  for i in range(len(line)):
    if line[i] not in ["0", "1"]:
      continue
    if i not in col_dict:
      col_dict[i] = ""
    col_dict[i] = col_dict[i] + line[i]
  return col_dict

def main2():
  file = open('input3_1.txt', 'r')
  lines = file.readlines()

  found = None
  pos = 0
  rem_o2_lines = lines.copy()

  while not found:
    columns = functools.reduce(lambda a, b: to_columns(a, b), rem_o2_lines, {})
    col = columns[pos]

    zeros = 0
    ones = 0
    for bit in col:
      if bit == "0":
        zeros = zeros + 1
      else:
        ones = ones + 1
    
    if ones > zeros:
      most_common = "1"
    elif zeros > ones:
      most_common = "0"
    else:
      most_common = "1"

    rem_dict = {v: k for v, k in enumerate(rem_o2_lines)}
    matched_lines = []
    for idx, bit in enumerate(col):
      if bit == most_common:
        matched_lines.append(rem_dict[idx])
    
    pos = pos + 1
    rem_o2_lines = matched_lines.copy()
    if len(rem_o2_lines) == 1:
      found = rem_o2_lines[0]

  print(found)
  print(int(found, 2))
  o2 = int(found, 2)

  found = None
  pos = 0
  rem_co2_lines = lines.copy()

  while not found:
    columns = functools.reduce(lambda a, b: to_columns(a, b), rem_co2_lines, {})
    col = columns[pos]

    zeros = 0
    ones = 0
    for bit in col:
      if bit == "0":
        zeros = zeros + 1
      else:
        ones = ones + 1
    
    if ones > zeros:
      most_common = "1"
    elif zeros > ones:
      most_common = "0"
    else:
      most_common = "1"

    rem_dict = {v: k for v, k in enumerate(rem_co2_lines)}
    matched_lines = []
    for idx, bit in enumerate(col):
      if bit != most_common:
        matched_lines.append(rem_dict[idx])
    
    pos = pos + 1
    rem_co2_lines = matched_lines.copy()
    if len(rem_co2_lines) == 1:
      found = rem_co2_lines[0]
  
  print(found)
  print(int(found, 2))

  co2 = int(found, 2)

  print(o2 * co2)


if __name__ == '__main__':
  # main()
  main2()