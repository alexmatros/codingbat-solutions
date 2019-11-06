def left2(str):
  if len(str) == 2:
    return str
  front = str[:2]
  end = str[2:]
  return end + front
