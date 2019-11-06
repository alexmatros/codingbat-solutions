def first_two(str):
  if len(str) < 2:
    return str
  elif len(str) == 0:
    return "yields the empty string"
  start = str[:2]
  return start
