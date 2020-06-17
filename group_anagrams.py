class Solution:
    def groupAnagrams(self, strs: list()) -> list(list()):
        c = {}
        for x in strs: 
            key = ''.join(sorted(x))
            if key in c.keys():
                c[key].append(x)
            else:
                c[key]=[x]
        return(list(c.values()))

if __name__ == "__main__":
    a = Solution()
    print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))