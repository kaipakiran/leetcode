from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        candidates = {}
        chars = []
        i = 0
        seq = 0
        t_len = len(t)
        temp = Counter(t)   
        if len(s)<len(t):
            return ""
        if len(t)==1:
            if t in s:
                return t
        for j,char in enumerate(s,0):
            if char in temp.keys():
                print(j, char)
                print(temp[char])
                if len(chars)==0:
                    i = j
                if temp[char]>=1:
                    chars.append(char)
                    temp[char]-=1
                else:
                    if char in chars:
                        chars=[char]
                        temp = Counter(t)
                        i = j
                    else:
                        chars.append(char)
                if j>0 and s[j-1] in chars:
                    print("s[j-1]: ",s[j-1],"j: ",j)
                    seq+=2   
                print("len of chars:",len(chars))
                print("chars: ",chars)
                if len(chars)==t_len:
                    candidates[j-i] = "".join(s[i:j+1])
                    print(candidates[j-i])
                    print("seq: ",seq)
                    if seq>0:
                        print("chars:",chars)
                        chars=chars[(t_len-seq):]
                        i = j - seq+1
                        seq = 0
                    else:
                        chars = [char]
                        i = j
                    temp = Counter(t)
                    print("chars after: ",chars)
                    
        print(candidates)
        return candidates[min(candidates.keys())] if len(candidates.keys())>0 else ""

if __name__ == "__main__":
    a = Solution()
    #print(a.minWindow(s='bdab',t='ab'))
    print(a.minWindow(s='ADOBECODEBANC',t='ABC'))
    print(a.minWindow(s='cabwefgewcwaefgcf',t='cae'))