import re
class Solution:
    def reorderLogFiles(self, logs: list):
        let_logs = [x for x in logs if len(re.findall("[0-9]",x.split()[1]))==0 ]
        sorted_list = sorted([(" ".join(x.split()[:1]),i) for i,x in enumerate(let_logs)])
        let_logs = [let_logs[x[1]]for x in sorted_list]
        sorted_list = sorted([(" ".join(x.split()[1:]),i) for i,x in enumerate(let_logs)])
        let_logs = [let_logs[x[1]]for x in sorted_list]
        let_logs.extend([x for x in logs if len(re.findall("[0-9]",x.split()[1]))>0])
        return let_logs

if __name__ == "__main__":
    a = Solution()
    logs = [["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
            ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"],
            ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]]
    for log in logs:
        print(a.reorderLogFiles(log))