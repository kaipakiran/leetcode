import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s = re.search('^[0-9]+|^[-/+][0-9]+',s)
        if s is None:
            return 0
        s = int(s[0])
        if s<-2147483648:
            return -2147483648
        elif s>2147483647:
            return 2147483647
        return s

if __name__ == "__main__":
    s = '+0012a42'
    a = Solution()
    print(a.myAtoi(s))