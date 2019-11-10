def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str) - 2):
    if str[i:i+3] == "dog":
      dog += 1
    elif str[i:i+3] == "cat":
      cat += 1
    else:
      continue
  
  if dog == cat:
    return True
  else:
    return False