class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        results = 0
        for j,n in enumerate(num1[::-1],0):
            carry = 0
            result=[]
            for m in num2[::-1]:
                value = int(n)*int(m)+carry
                carry, units=divmod(value,10)
                result.append(str(units))
                #carry = int(value/10)
            if carry>0:
                result.append(str(carry))
            result = result[::-1]
            result.extend('0'*j)
            results+=(int("".join(result)))
        return str((results))

if __name__ == "__main__":
    a = Solution()
    print(a.multiply('123','456'))