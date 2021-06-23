class Solution(object):
    @staticmethod
    def _get_minimum_discount_price(current_index, prices_indexes, prices):
        discounted_price = None

        for index in range(current_index + 1, prices_indexes):
            if prices[current_index] >= prices[index]:
                discounted_price = prices[current_index] - prices[index]
                break

        if discounted_price is None:
            discounted_price = prices[current_index]

        return discounted_price

    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        discounted_prices = []
        prices_indexes = len(prices)

        for index in range(prices_indexes):
            discounted_price = self._get_minimum_discount_price(index, prices_indexes, prices)
            discounted_prices.append(discounted_price)

        return discounted_prices
