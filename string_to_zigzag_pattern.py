class Solution:
    def convert(self, s: str, numRows: int):
        """
           #Convert string to zigzag pattern 
           #https://stackoverflow.com/questions/6473679/transpose-list-of-lists
           input = PAYPALISHIRING
           output with numRows = 5
           P     H 
           A   S I
           Y  I  R
           P L   I G
           A     N 
           output with numRows = 3
           P   A   H   N
           A P L S I I G
           Y   I   R 
           output with numRows = 4
           P     I      N 
           A   L S    I G
           Y A   H  R
           P     I        
        """
        num_rows = numRows
        string = s
        overall_cols = []
        i = 0
        c = 0
        out = []
        while(i < len(string)):
            if c!=0:
                if c <= (num_rows-2):
                    temp = [" "]*num_rows
                    temp[num_rows-c-1] = string[i]
                    c+=1
                    overall_cols.append(temp)
                    i+=1
                else:
                    c = 0
            if c == 0:
                temp = list(string[i:(i+(num_rows))])
                tlen = len(temp)
                if tlen<num_rows:
                    temp.extend([" "]*(num_rows-tlen))
                overall_cols.append(temp)
                i+=num_rows
                c+= 1
        for l in list(map(list, zip(*overall_cols))):
            out.append("".join([x for x in l if x !=' ']))
        return("".join(out))

if __name__ == "__main__":
    a = Solution()
    print(a.convert("paypalishiring",3))
    print(a.convert("paypalishiring",2))
    print(a.convert("paypalishiring",4))