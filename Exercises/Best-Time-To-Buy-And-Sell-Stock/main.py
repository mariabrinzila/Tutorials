class Solution(object):
    def max_profit(self, prices):
        """
        :param prices: the array of stock prices (the price on position i represents the price to sell or
            buy stock on day i)
        :return: the maximum profit we can achieve from a buy - sell transaction, if it's possible
            (we must sell on a day after buying stock) and 0, otherwise
        """
        # Data structure <=> Array
        # Algorithm <=> Greedy

        # We must have a maximum profit
        # Which may not necessarily come from choosing a minimum buying price and maximum selling price
        # So we need to find 2 values that maximize the profit (sell - buy is maximal)
        # Which will lead to an optimal solution <=> Greedy

        # Time complexity <=> O(n), where n is the size of the array
        # Space complexity <=> O(1)

        # For each element in the array of prices:
        # If the current element is < the minimum price to buy stock:
        # Change the buying price since we found a new minimum to buy stock
        # If the position of the new minimum is > the current day to sell stock:
        # Reinitialize the selling price since we need to find another after the buying day
        # If the selling price has been established and the profit of the current transaction is maximal:
        # Update the profit
        # Otherwise (if the current element is >= the minium price to buy stock):
        # If the current element is > the maximum price to sell stock:
        # Change the selling price since we found a new maximum to sell stock
        # If the profit of the current transaction is maximal:
        # Update the profit
        # If by the time we finished the array of prices, the profit's value hasn't changed from -1:
        # No transactions can be made
        buy = 100000
        sell = -1
        n = len(prices)
        day_sell = n + 1
        profit = -1

        for i in range(n):
            price = prices[i]

            if price < buy:
                buy = price

                if i > day_sell:
                    sell = -1

                if sell != -1 and sell - buy > profit:
                    profit = sell - buy
            else:
                if price > sell:
                    sell = price
                    day_sell = i

                    if sell - buy > profit:
                        profit = sell - buy

        if profit == -1:
            return 0

        return profit


# Example 1
prices1 = [7, 1, 5, 3, 6, 4]

print(Solution().max_profit(prices1))
print("-------------------------------------")

# Example 2
prices1 = [7, 6, 4, 3, 1]

print(Solution().max_profit(prices1))
print("-------------------------------------")

# Example 3
prices1 = [3, 2, 6, 5, 0, 3]

print(Solution().max_profit(prices1))
