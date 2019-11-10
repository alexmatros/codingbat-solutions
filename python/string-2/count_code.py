def count_code(str):
  code = 0
  for i in range(len(str) - 3):
    if str[i:i+2] + str[i+3] == "coe":
      code += 1
    else:
      continue
  
  return code