class Solution:
    def isPalindrome(self, x: int):
        i = 1
        rev = 0
        flag = 0
        temp = x
        while(1):
            if temp <10:
                n = temp
                flag = 1
            else:
                n = int(temp / 10)
            r = temp % 10
            temp = n
            rev = rev*10 +r
            i+=1
            if flag ==1:
                break
        return (rev==x)

if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome(123))
    print(a.isPalindrome(12344321))
    print(a.isPalindrome(123454321))