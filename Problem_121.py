#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if  not prices:
            return 0
        max_profile = 0
        small_price = prices[0]
        for i in prices[1:]:
            small_price = min(small_price, i)
            if i - small_price > max_profile:
                max_profile = i - small_price
        return max_profile