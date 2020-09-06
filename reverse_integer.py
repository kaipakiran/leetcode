class Solution:
    def reverse(self, x):
        val = str(x)
        if val[0]=='-':
            rev = val[1:][::-1]
            rev = -1*int(rev)
            if rev < -2**31:
                return 0
            return rev
        else:
            if int(val[::-1])>(2**31-1):
                return 0
            return int(val[::-1])

if __name__ == "__main__":
    a = Solution()
    print(a.reverse(-123))
    print(a.reverse(2324))