def has22(nums):
  previous = 0
  contain_22 = False
  for i in range(len(nums)):
    if nums[i] == 2 and previous == 2:
      contain_22 = True
      break
    elif nums[i] == 2:
      previous = 2
    else:
      previous = 0
      continue
    
  return contain_22