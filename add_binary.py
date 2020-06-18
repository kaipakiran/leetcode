class Solution:
    def __init__(self):
        self.output=""
        self.carry=0
    def _compute_sum(self,bit1:str,bit2:str) -> None:
        if bit1==bit2:
            if bit1=="1":
                if self.carry==1:
                    self.output = "1"+self.output
                    self.carry=1
                else:
                    self.output = "0"+self.output
                    self.carry=1
            else:
                if self.carry==1:
                    self.output = "1"+self.output
                    self.carry=0
                else:
                    self.output = "0"+self.output
                    self.carry=0
        else:
            if self.carry==1:
                self.output ="0"+self.output
                self.carry=1
            else:
                self.output="1"+self.output
                self.carry=0
            
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        alen = len(a)
        blen = len(b)
        while(alen>0 or blen>0):
            if alen>0 and blen>0:
                bit1 = a.pop()
                bit2 = b.pop()
                self._compute_sum(bit1,bit2)
            else: 
                if alen:
                    if self.carry:
                        while(alen>0 and self.carry==1):
                            bit1 = a.pop()
                            alen-=1
                            if bit1=="1":
                                self.output = "0"+self.output
                                self.carry=1
                            else:
                                self.output = "1" + self.output
                                self.carry=0    
                    self.output="".join(a)+self.output
                    break
                else:
                    if self.carry:
                        while(blen>0 and self.carry==1):
                            bit1 = b.pop()
                            blen-=1
                            if bit1=="1":
                                self.output = "0"+self.output
                                self.carry=1
                            else:
                                self.output = "1" + self.output
                                self.carry=0    
                    self.output="".join(b)+self.output
                    break
            alen-=1
            blen-=1
        if self.carry:
            self.output = "1"+self.output
        return self.output

if __name__ == "__main__":
    a = Solution()
    b1 = '1010'
    b2 = '11'
    print(a.addBinary(b1,b2))
