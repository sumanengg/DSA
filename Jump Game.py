def canJump(self, nums: List[int]) -> bool:
    final_point = len(nums) - 1
    for i in range(len(nums) - 2 , -1, -1):
        if i + nums[i] >= final_point:
            final_point = i
    if final_point == 0:
        return True
    else:
        return False
