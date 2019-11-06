def centered_average(nums):
  nums.sort()
  nums = nums[1:-1]
  total = 0
  for i in range(len(nums)):
    total += nums[i]
  
  total = total / len(nums)
  
  return total
