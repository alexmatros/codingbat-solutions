def array_front9(nums):
  nine = False
  if len(nums) < 4:
    for i in range(len(nums)):
      if nums[i] == 9:
        nine = True
  else:
    for i in range(4):
      if nums[i] == 9:
        nine = True
  
  return nine