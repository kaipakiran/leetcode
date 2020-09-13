class Solution:
    def maxProfit(self, prices: list):
        profit = 0
        while(1):
            if len(prices)==0:
                return profit
            buy = min(prices)
            buy_index = prices.index(buy)
            #print(buy_index)
            if (buy_index+1) == len(prices):
                prices.pop(buy_index)
            else:
                sell = max(prices[buy_index+1:])
                temp = sell - buy
                if temp> profit:
                    profit = temp
                prices.pop(buy_index)
                prices.pop(prices.index(sell))
        return profit

if __name__ == "__main__":
    a = Solution()
    prices = [7,2,4,1]
    print(a.maxProfit(prices))