def rotate_left3(nums):
  rotated = nums[1:]
  rotated.append(nums[0])
  return rotated
