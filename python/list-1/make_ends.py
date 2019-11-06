def make_ends(nums):
  ls = []
  if len(nums) == 1:
    ls.append(nums[0])
    ls.append(nums[0])
  else:
    ls.append(nums[0])
    ls.append(nums[-1])
  
  return ls