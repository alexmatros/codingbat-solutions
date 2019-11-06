def pos_neg(a, b, negative):
  if a > 0 and b < 0:
    if negative == True:
      return False
    else:
      return True
  elif a < 0 and b > 0:
    if negative == True:
      return False
    else:
      return True
  elif a < 0 and b < 0:
    if negative == True:
      return True
    else:
      return False
  else:
    return False