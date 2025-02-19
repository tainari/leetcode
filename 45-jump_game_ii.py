import math
class Solution:
    def canJump(self, nums) -> bool:
        # hash of steps to jump
        # define valid and invalid variables
        VALID = 1
        INVALID = 0
        UNKNOWN = -1
        # track
        valid_spots = [UNKNOWN] * len(nums)
        valid_spots[-1] = VALID
        steps_to_end = [math.inf] * len(nums)
        steps_to_end[-1] = 0
        # start from the back
        max_ind = len(nums) - 1
        for start_ind in range(max_ind - 2, -1, -1):
            max_dist = nums[start_ind]
            min_steps_to_end = math.inf
            for jump_ind in range(start_ind + 1, min(start_ind + max_dist + 1, max_ind + 1)):
                if valid_spots[jump_ind] == VALID:
                    valid_spots[start_ind] = VALID
                    min_steps_to_end = min(min_steps_to_end, steps_to_end[jump_ind])
            if valid_spots[start_ind] != VALID:
                valid_spots[start_ind] == INVALID
            else:
                steps_to_end[start_ind] = min_steps_to_end + 1
        return steps_to_end[0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([2,3,1,1,4]))
    print(solution.canJump([2,3,0,1,4]))