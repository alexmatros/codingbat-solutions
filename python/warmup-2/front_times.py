def front_times(str, n):
  final = ""
  if len(str) < 3:
    for _ in range(n):
      final += str
  else:
    char = str[:3]
    for _ in range(n):
      final += char
  return final