def sum13(nums):
  sum = 0
  previous = 0
  if len(nums) == 0:
    sum = 0
  else:
    for i in range(len(nums)):
      if nums[i] == 13:
        previous = 13
        continue
      elif previous == 13:
        previous = 0
        continue
      elif nums[i] != 13:
        sum += nums[i]
  
  return sum
