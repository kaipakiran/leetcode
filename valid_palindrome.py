import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(re.findall("[a-zA-Z0-9]*",s)).lower()
        if s=="":
            return True
        s_len = len(s)
        center = s_len/2
        is_palindrome = False
        if s_len%2!=0:
            center = int(center)+1
        i =0
        while i< center:
            if s[i]==s[s_len-(i+1)]:
                is_palindrome = True
            else:
                return False
            i+=1
        return is_palindrome

if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(a.isPalindrome(s="race a car"))