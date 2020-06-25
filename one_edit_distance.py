from collections import Counter
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        s_len = len(s)
        t_len = len(t)
        action = ""
        if abs(t_len-s_len)>1:
            print("less")
            return False
        if s_len < t_len:
            d_counter = t_counter - s_counter
            action = 1 #add
        elif s_len==t_len:
            d_counter = t_counter - s_counter
            r_counter = s_counter - t_counter
            action = 2 # replace
        else:
            d_counter = s_counter - t_counter
            action = 3 # delete
        if len(d_counter.keys())>1:
            return False
        elif len(d_counter.keys())==0:
            return False
        else:
            if action == 1: #add
                t= list(t)
                t.pop(t.index(list(d_counter.keys())[0]))
                t = "".join(t)
                if s == t:
                    return True
                else:
                    return False
            elif action == 2: #replace
                s = list(s)
                t = list(t)
                token = list(d_counter.keys())[0]
                replace = list(r_counter.keys())[0]
                index = 0
                while(s_counter[replace]>=1):
                    index = s.index(replace,index)
                    s[index] = token                    #print(index)
                    if "".join(s) == "".join(t):
                        return True
                    s[index] = replace
                    index = index+1
                    s_counter[replace]-=1
            else: # delete
                i= 0
                s = list(s)
                token = list(d_counter.keys())[0]
                index = 0
                while s_counter[token]>=1:
                    index = s.index(token,index)
                    s_left = s[:index]
                    s_right = s[index+1:]
                    if "".join(s_left)+"".join(s_right) == t:
                        return True
                    index = index+1
                    s_counter[token]-=1


if __name__ == "__main__":
    a = Solution()
    print(a.isOneEditDistance(s="ab",t="acb"))
    print(a.isOneEditDistance(s="cab",t="ad"))