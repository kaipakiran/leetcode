class Solution:
    def isValid(self, s: str):
        open_c = ["(","[","{",]
        close_c = [")","]","}"]
        paranthesis = {}
        paranthesis['round']=0
        paranthesis['square']=0
        paranthesis['curly']=0
        last_open = []
        for c in s:
            if c in open_c:
                last_open.append(c)
                if c =="(":
                    paranthesis["round"]+=1
                elif c=="[":
                    paranthesis["square"]+=1
                else:
                    paranthesis["curly"]+=1
            elif c in close_c:
                if len(last_open)==0:
                    return False
                if c ==")":
                    if last_open.pop(-1) == "(":
                        if paranthesis['round']>0:
                            paranthesis["round"]-=1
                        else:
                            return False
                    else:
                        return False
                elif c == "]":
                    if last_open.pop(-1) == "[":
                        if paranthesis['square']>0:
                            paranthesis["square"]-=1
                        else:
                            return False
                    else:
                        return False
                else:
                    if last_open.pop(-1) == "{":
                        if paranthesis['curly']>0:
                            paranthesis["curly"]-=1
                        else:
                            return False
                    else:
                        return False
            else:
                pass
        return True if sum(paranthesis.values())==0 else False

if __name__ == "__main__":
    a = Solution()
    s = "([)]"
    print(a.isValid(s))
    s = "[()()]"
    print(a.isValid(s))