class Solution(object):
    def max_profit(self, prices):
        """
        :param prices: the array of stock prices (the price on position i represents the price to sell or
            buy stock on day i)
        :return: the maximum profit we can achieve from a buy - sell transaction, if it's possible
            (we must first sell on a day after buying stock) and 0, otherwise
        """
        # Data structure <=> Array
        # Algorithm <=> Greedy

        # We must have a maximum profit
        # So we need to buy stock on a day when the price is the smallest possible (so we need to pick
        # The minimum price in the array)
        # And sell the stock on a day after the day we bought it at the greatest possible price (so we
        # Need to pick the maximum price in the array after the position when we bought the stock)
        # So we need to first pick the global minimum and then the local maximum
        # Which will lead to an optimal solution <=> Greedy

        # Time complexity <=> O(n), where n is the size of the array
        # Space complexity <=> O(1)

        # For each element in the array of prices:
        # If the current element is < the minimum price to buy stock, the day for buying stock isn't
        # The end of the array and there are prices higher than it after it:
        # Change the minimum's value
        # Since we found a new minimum to buy stock
        # If the current element is >= the minium price to buy stock:
        # If the current element is > the maximum price to sell stock or the previous price's day is <
        # The day the stock was bought, change the maximum's value
        # Since we found a new maximum to sell stock
        # If by the time we finished the array of prices we didn't find a price to sell stock:
        # No transactions can be made
        buy = 100000
        sell = -1
        n = len(prices)
        day_sell = n + 1
        day_buy = -1

        for i in range(n):
            price = prices[i]

            if price < buy:
                if i != n - 1 and prices[i + 1] > price and sell - buy < sell - price:
                    buy = price
                    day_buy = i
            else:
                if (price > sell and sell - buy < price - buy) or day_sell < day_buy:
                    sell = price
                    day_sell = i

        if sell == -1:
            return 0

        return sell - buy


# Example 1
"""prices1 = [7, 1, 5, 3, 6, 4]

print(Solution().max_profit(prices1))
print("-------------------------------------")

# Example 2
prices1 = [7, 6, 4, 3, 1]

print(Solution().max_profit(prices1))
print("-------------------------------------")"""

# Example 3
prices1 = [3, 2, 6, 5, 0, 3]

print(Solution().max_profit(prices1))
print("-------------------------------------")
