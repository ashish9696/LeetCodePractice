class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = int((high + low)/2)
        while low<=high:
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                low = mid+1
            else:
                high = mid-1
            mid = int((high + low)/2)
        return -1
