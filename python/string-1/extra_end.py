def extra_end(str):
  if len(str) == 2:
    return str + str + str
  end = str[-2:]
  return end + end + end
