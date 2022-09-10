from re import L


class Solution:
    def canBeIncreasing(self, nums: list[int], i=0) -> bool:
        isSeq = True
        temp = nums.copy()
        temp.pop(i)
        for idx, num in enumerate(temp):
            if idx > 0:
                if temp[idx - 1] < num:
                    isSeq = True
                else:
                    isSeq = False
                    break

        if (i == len(nums) - 1 or isSeq):
            return isSeq
        else:
            resp = self.canBeIncreasing(nums, i + 1)
            return resp

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        resp_arr = []
        for idx in range(len(nums)):
            temp = nums.copy()
            temp.pop(idx)
            y = target - nums[idx]
            if (y in temp):
                resp_arr.append(idx)
                resp_arr.append(next(i for i in reversed(range(len(nums))) if nums[i] == y))
                break
        return resp_arr


sol = Solution()
test1 = [1, 2, 10, 5, 7]
test2 = [2, 3, 5, 2]
test3 = [1, 1, 1]
test4 = [1, 1]
test5 = [2, 7, 11, 15]
test6 = [3, 2, 4]
test7 = [3, 3]
# print(sol.twoSum(test5, 9))
print(sol.twoSum(test1, 6))
print(sol.twoSum(test7, 6))
print(sol.twoSum(test2, 4))
print(sol.twoSum(test6, 6))
# print(sol.twoSum(test6, 6))
# print(sol.twoSum(test5, 9))

# print(sol.canBeIncreasing(test4))
