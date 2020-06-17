class Solution:
    def removeDuplicates(self, nums: list()) -> int:
        n_len = len(nums)
        if n_len==0:
            return 0
        else:
            cnt = 1
        i = n_len-2
        val = nums[n_len-1]
        while i>=0:
            #print(val)
            if val!=nums[i]:
                cnt+=1
                val = nums[i]
                i-=1
            else:
                nums.pop(i)
                i-=1
        return cnt

if __name__ == "__main__":
    c = Solution()
    l = [1,1,2]
    print(l[:c.removeDuplicates(l)])
    