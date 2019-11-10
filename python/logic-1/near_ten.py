def near_ten(num):
  distance = num % 10
  if distance >= 8 or distance <= 2:
    return True
  else:
    return False