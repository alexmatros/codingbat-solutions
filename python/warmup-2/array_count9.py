def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    index = nums[i]
    if index == 9:
      count += 1
  
  return count