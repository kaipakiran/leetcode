class Solution:
    def next_permutation(self,nums:list(), r=None)->None:
        nlen = len(nums)
        if nlen == 1:
            return
        if len(set(nums))==1:
            return
        index = -1
        for i in range(nlen-1):
            if nums[i]<nums[i+1]:
                index = i
        if index==-1:
            nums.sort()
            return
        temp = nums[index]
        swap_candidates = [x for x in nums[index+1:] if x>temp]
        swap_index = max([nums.index(temp2,(index+1)) for temp2 in swap_candidates])
        nums[index]=nums[swap_index]
        nums[swap_index] = temp
        if nums[index+1:] == sorted(nums[index+1:]):
            return
        else:
            nums[index+1:] = sorted(nums[index+1:])




if __name__ == "__main__":
    a = Solution()
    nums = [1,2,0,3,0,1,2,4]
    #nums = [1,2,3]
    a.next_permutation(nums)
    print(nums)