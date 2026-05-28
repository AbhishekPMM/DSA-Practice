class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        left = 0
        right = 1
        maxprofit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left] 
                maxprofit = max(maxprofit,profit)
            else:
                left = right
            right +=1
        return maxprofit
obj = Solution()
prices = list(map(int, input("enter the input : ").split()))
result = obj.maxProfit(prices)
print(result)

