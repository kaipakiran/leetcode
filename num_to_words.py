class Solution:
    def numberToWords(self, num: int):
        if num == 0:
            return "Zero"
        unit = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        eleven_teen = ['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen'\
                        ,'Eighteen','Nineteen']
        ten_tys = ['Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        place = ['unit','Thousand','Million','Billion']
        num_string = {}
        
        prev = -1
        j = 1
        while(1):
            val = num%1000
            inter = []
            zero = 0
            for i in range(1,4):
                v = val%(10**i)
                #print(val,v,i)
                if i>=2:
                    #print(str(v/(10**(i-1))))
                    v = int(str(v/(10**(i-1))).split('.')[0])
                #print(v)
                if v == 0:
                    zero = 1
                else:
                    if i==1:
                        inter.append(unit[v-1])
                        prev = v
                    elif i == 2:
                        if v ==1:
                            if zero:
                                inter.append(ten_tys[v-1])
                                zero = 0
                            else:
                                inter.pop(i-2)
                                inter.append(eleven_teen[prev-1])
                        else:
                            inter.append(ten_tys[v-1])
                    else:
                        inter.append('Hundred')
                        inter.append(unit[v-1])
            #print(inter)
            num_string[place[j-1]]=" ".join(inter[::-1])
            #print(num/1000)
            num = int(str(num/1000).split(".")[0])
            #print(num)
            if num==0:
                break
            j+=1
        #print(num_string)
        res = []
        for key in num_string.keys():
            if len(num_string[key])>0:
                if key!='unit':
                    res.append(num_string[key]+" "+key)
                else:
                    res.append(num_string[key])
        return(" ".join(res[::-1]).strip())
    
if __name__ == "__main__":
    a = Solution()
    num = 1002112001
    print(a.numberToWords(num))
    num = 123456
    print(a.numberToWords(num))