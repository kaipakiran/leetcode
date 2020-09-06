class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2:list):
        val1 = nums1
        val2 = nums2
        val1_len = len(val1)
        val2_len = len(val2)
        overall_len = val1_len+val2_len
        even=False
        if overall_len%2 ==0:
            even = True    
        if val1_len==0:
            val3 = val2
        elif val2_len ==0:
            val3 = val1
        elif val1[-1]<val2[0]:
            val3 = val1
            val3.extend(val2)
        elif val2[-1]<val1[0]:
            val3 = val2
            val3.extend(val1)
        else:
            val3 = []
            flag = 0
            i = 0
            while i < overall_len:
                if flag==0:
                    if val1[-1]>val2[-1]:
                        val3.append(val1[-1])
                        val1.pop(val1.index(val3[i]))
                        if len(val1)==0:
                            flag =1
                    else:
                        val3.append(val2[-1])
                        val2.pop(val2.index(val3[i]))
                        if len(val2)==0:
                            flag = 2
                elif flag ==1:
                    val3.extend(val2[::-1])
                    break
                else:
                    val3.extend(val1[::-1])
                    break
                i+=1
        index = int(overall_len/2)
        if even:   
            return ((val3[index]+val3[index-1])/2.0)
        else:
            return (val3[index]/1.0)

if __name__ == "__main__":
    a = Solution()
    print(a.findMedianSortedArrays([1,2,3],[4,5]))
    print(a.findMedianSortedArrays([1,2,6],[4,5]))