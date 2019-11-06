def front_back(str):
  if len(str) <= 1:
    return str
  front = str[0]
  back = str[-1]
  middle = str[1:-1]
  return back + middle + front