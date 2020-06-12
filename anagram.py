from collections import Counter
import re
import numpy as np
class Solution:
    def find_anagrams(self, s: str, p: str) -> list():
        s_len = len(s)
        p_len = len(p)

        if p == s:
            return [0]   
        index = []
        # flag = 0
        # set_p = set(p)
        # if len(set_p)==p_len:
        #     flag = 1
        # else:
        sorted_p = Counter(p)
        sorted_s = Counter()
        for i in range(s_len):
            sorted_s[s[i]]+=1
            # if flag:
            #     if set(seq)==set_p:
            #         index.append(i)
            if i>=p_len:
                if sorted_s[s[i-p_len]] == 1:
                    del sorted_s[s[i-p_len]]
                else:
                    sorted_s[s[i-p_len]]-=1
            if sorted_s==sorted_p:
                index.append(i - p_len + 1)
        return index

    def find_anagrams_soln(self, s:str,p:str) -> list():
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter 
            # on the right side of the window
            s_count[s[i]] += 1
            # remove one letter 
            # from the left side of the window
            if i >= np:
                print(s_count)
                print(p_count)
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output

if __name__ == "__main__":
    a  = Solution()
    s = "abababab"
    p='ab'
    import timeit
    print(len(s))
    print(a.find_anagrams(s,p))
    print(a.find_anagrams_soln(s,p))