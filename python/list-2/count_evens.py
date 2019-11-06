def count_evens(nums):
  even = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      even += 1
  
  return even