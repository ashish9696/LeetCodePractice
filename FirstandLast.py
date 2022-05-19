class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) is 0:
            return [-1, -1]
        
        else:
            start, end = -1, -1
            if nums[0]==target:
                start = 0
            else:
                l, r = 0, len(nums)-1
                while l<=r:
                    mid = (l+r)//2
                    if nums[mid]==target and nums[mid-1]<target:
                        start = mid
                        break
                    elif nums[mid]>=target:
                        r = mid-1
                    else:
                        l = mid+1


            if nums[-1]==target:
                end = len(nums)-1
            else:
                l, r = 0, len(nums)-1
                while l<=r:
                    mid = (l+r)//2
                    if nums[mid]==target and nums[mid+1]>target:
                        end = mid
                        break
                    elif nums[mid]<=target:
                        l = mid+1
                    else:
                        r = mid-1

            return [start, end]
        
        
