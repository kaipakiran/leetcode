class Solution:
    def merge(self, nums1: list(), m: int, nums2: list(), n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first_zero = m
        # l_n1 = len(nums1[:m])
        # print(l_n1)
        if m==0: 
            if len(nums1)==1:
                nums1[0]=nums2[0]
            else:
                for i,nu in enumerate(nums2,0):
                    nums1[i]= nu         
        else:    
            vals = [x for x in nums1[:m]]
            min_val = min(vals)
            for nu in nums2:       
                # print("val: ",nu)
                # print(nums1)
                if nu<min_val:
                    position = nums1.index(min_val)
                    min_val = nu
                else:
                    val = [x for x in nums1[:first_zero] if x<=nu][-1]
                    # print("value less tha val:",val)
                    # print("index for insersion: ",nums1[:first_zero][::-1].index(val))
                    position = len(nums1[:first_zero]) - nums1[:first_zero][::-1].index(val)
                    
                i = first_zero
                first_zero = first_zero+1
                # print("zero pos: ",first_zero)
                # print(nums1)
                # print(i,position)
                while i>position:
                    temp = nums1[i-1]
                    nums1[i] = temp
                    i-=1
                nums1[i] = nu
            print(nums1)
if __name__ == "__main__":
    a = Solution()
    (a.merge(nums1=[-1,0,0,2,3,0,0,0],m=5, nums2=[1,6,4], n=3))