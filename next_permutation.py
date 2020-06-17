class Solution:
    """
    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

    Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    Find the largest index l greater than k such that a[k] < a[l].
    Swap the value of a[k] with that of a[l].
    Reverse the sequence from a[k + 1] up to and including the final element a[n].
    For example, given the sequence [1, 2, 3, 4] (which is in increasing order), and given that the index is zero-based, the steps are as follows:
    Index k = 2, because 3 is placed at an index that satisfies condition of being the largest index that is still less than a[k + 1] which is 4.
    Index l = 3, because 4 is the only value in the sequence that is greater than 3 in order to satisfy the condition a[k] < a[l].
    The values of a[2] and a[3] are swapped to form the new sequence [1,2,4,3].
    The sequence after k-index a[2] to the final element is reversed. Because only one value lies after this index (the 3), the sequence remains unchanged in this instance. Thus the lexicographic successor of the initial state is permuted: [1,2,4,3].
    Following this algorithm, the next lexicographic permutation will be [1,3,2,4], and the 24th permutation will be [4,3,2,1] at which point a[k] < a[k + 1] does not exist, indicating that this is the last permutation.
    This method uses about 3 comparisons and 1.5 swaps per permutation, amortized over the whole sequence, not counting the initial sort
    """
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