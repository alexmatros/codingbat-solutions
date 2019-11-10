def make_chocolate(small, big, goal):
  max_big = goal / 5
  if big >= max_big:
    if small >= (goal - max_big * 5):
      return goal - max_big * 5
  if big < max_big:
    if small >= (goal - big * 5):
      return goal - big * 5
  return -1