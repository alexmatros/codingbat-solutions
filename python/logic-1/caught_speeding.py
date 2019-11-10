def caught_speeding(speed, is_birthday):
  ticket = None
  if is_birthday == False:
    if speed <= 60:
      ticket = 0
    elif speed >= 61 and speed <= 80:
      ticket = 1
    else:
      ticket = 2
  else:
    if speed <= 65:
      ticket = 0
    elif speed >= 66 and speed <= 85:
      ticket = 1
    else:
      ticket = 2
      
  return ticket