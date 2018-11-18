import unittest

# tested with python 2.7.15

def largest_possible_loss(pricesLst):
    if len(pricesLst) == 0:
        return 0

    # Use a dynamic programming approach.
    #
    # This algorithm runs in O(n) time using O(1) space

    largestLoss = 0 # the largest possible loss so far
    sellPrice = pricesLst[0] # the sell price of the largest loss so far
    maxPrice = pricesLst[0] # the max price so far in the whole array

    for price in pricesLst[1:]:
        if price > maxPrice:
            maxPrice = price

        if maxPrice - price > largestLoss:
            largestLoss = (maxPrice - price)
            sellPrice = price

    return largestLoss


class TestPricesLst(unittest.TestCase):
    def test_largest_possible_loss(self):
        prices = [6, 12, 5, 3, 9, 6, 12, 3, 4, 10]
        self.assertEqual(largest_possible_loss(prices), 9)
        prices = [12, 6, 20, 19, 19]
        self.assertEqual(largest_possible_loss(prices), 6)
        prices = [10, 5, 15, 5, 9, 10]
        self.assertEqual(largest_possible_loss(prices), 10)
        prices = [7, 11, 11, 7, 11, 9, 11, 12, 3]
        self.assertEqual(largest_possible_loss(prices), 9)
        prices = [11, 6, 9, 4, 8, 5, 4, 5, 9, 10]
        self.assertEqual(largest_possible_loss(prices), 7)

    def test_lst_empty(self):
        self.assertEqual(largest_possible_loss([]), 0)

    def test_ascending(self):
        prices = [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(largest_possible_loss(prices), 0)

    def test_descending(self):
        prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(largest_possible_loss(prices), 10)

    def test_duplicate(self):
        prices = [10, 5, 10 ,5]
        self.assertEqual(largest_possible_loss(prices), 5)

if __name__ == '__main__':
    unittest.main()
