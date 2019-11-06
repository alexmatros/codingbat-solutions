def max_end3(nums):
  array = []
  if nums[0] > nums[-1]:
    for i in range(len(nums)):
      array.append(nums[0])
  elif nums[0] < nums[-1]:
    for i in range(len(nums)):
      array.append(nums[-1])
  else:
    for i in range(len(nums)):
      array.append(nums[-1])
  
  return array