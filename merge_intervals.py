class Solution:
    def merge(self, intervals:list):
        new_intervals = []
        intervals = sorted(intervals)
        for i,interval in enumerate(intervals):
            temp = interval
            for j, interval2 in enumerate(intervals[i+1:],1):
                if temp[-1] >= interval2[0] and temp[-1]<=interval2[-1]:
                    temp[-1] = interval2[-1]
                    intervals.pop(intervals.index(interval2))
                elif temp[0] <=interval2[-1] and temp[-1]>=interval2[0]:
                    if temp[0]>=interval2[0]:
                        temp[0] = interval2[0]
                    intervals.pop(intervals.index(interval2))
            new_intervals.append(temp)
        return new_intervals

if __name__ == "__main__":
    a = Solution()
    intervals = [[10,15],[2,3],[1,8],[8,10],[15,18]]
    print(a.merge(intervals))
    intervals = [[1,4],[4,5]]
    print(a.merge(intervals))