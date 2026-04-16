class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list = []
        list1 = []
        n = len(nums)
        for i in range(1,n+1):
            list.append(i)
        for j in list:
            if j not in nums:
                list1.append(j)
        return list1



