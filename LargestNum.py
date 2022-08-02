class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i]=str(n) #Converts all the numbers in String from integer
        
        def compare(n1,n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums))) #For input: 0,0,0 we want to return 0 instead of 000