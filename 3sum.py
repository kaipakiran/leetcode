from collections import Counter
class Solution:
    def threeSum(self, nums: list()) -> list(list()):
        if len(nums) <3:
            return []
        nums.sort()
        count = Counter(nums)
        candidates = {}
        keys = count.keys()
        positive = [x for x in keys if x>=0]
        negative = [x for x in keys if x<0]
        for i, o1 in enumerate(nums,0):
            balance=0-o1
            if balance>=0:
                o2_list = [k for k in positive if k<=balance]
            else:
                o2_list =  [k for k in negative if k>balance]  
            for j, o2 in enumerate(o2_list,0):
                balance = 0-(o1 + o2)
                if balance in keys:
                    c = [o1,o2,balance]
                    c.sort()
                    if str(c) in candidates.keys(): 
                        break
                    if (o1==o2 and count[o1]==1) or \
                        (o2==balance and count[o2]==1) or \
                        (o1==balance and count[o1]==1) or \
                        (o1==o2 and o1==balance and count[o1]<3):
                            pass
                    else:
                        candidates[str(c)] =c     
        return list(candidates.values())

if __name__ == "__main__":
    c = Solution()
    nums = [-15,10,0,-2,14,-1,-10,-14,10,12,6,-6,10,2,-11,-9,2,13,2,-9,-14,-12,-10,-12,13,13,-10,-3,2,-11,3,-6,6,10,7,5,-13,4,-2,12,1,-11,14,-4,6,-12,-6,-14,8,11,-8,1,7,-3,5,5,-13,10,9,-3,6,-10,6,-3,7,-9,-13,9,10,0,-1,-11,4,-10,-8,-13,-15,2,-12,8,-2,-12,-14,-10,-8,6,2,-5,-7,-11,7,14,-6,-10,-12,8,-4,-10,-5,14,-3,9,-12,8,14,-13]
    print(c.threeSum(nums))


        

                    

