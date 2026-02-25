class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        min_price = prices[0]      # Minimum price so far
        max_profit = 0             # Maximum profit so far

        for price in prices:
            # Update min_price if current price is lower
            if price < min_price:
                min_price = price

            # Calculate profit if we sell at current price
            profit = price - min_price

            # Update max_profit if this profit is higher
            if profit > max_profit:
                max_profit = profit

        return max_profit