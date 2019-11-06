def sum67(nums):
  previous = 0
  total = 0
  for i in range(len(nums)):
    if nums[i] == 6 or previous == 6:
      previous = 6
      if nums[i] == 7:
        previous = 0
        continue
      else:
        continue
    else:
      total += nums[i]
  
  return total
