import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Added the assertion below ------------ """
    for quote in quotes:
      #from the getDataPoint() function in client3.py,
      #each line should match each record I have
      self.assertEqual(getDataPoint(quote),(
        quote['stock'],
        float(quote['top_bid']['price']),
        float(quote['top_ask']['price']),
        (float(quote['top_bid']['price']) + float(quote['top_ask']['price']))/2)
        )

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Added the assertion below ------------ """
    for quote in quotes:
      #from the getDataPoint() function in client3.py,
      #each line should match each record I have
      self.assertEqual(getDataPoint(quote),(
        quote['stock'],
        float(quote['top_bid']['price']),
        float(quote['top_ask']['price']),
        (float(quote['top_bid']['price']) + float(quote['top_ask']['price']))/2)
        )

  """ ------------ Added more unit tests ------------ """
  def test_getDataPoint_calculatePriceBidSameAsAsk(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      #from the getDataPoint() function in client3.py,
      #each line should match each record I have
      self.assertEqual(getDataPoint(quote),(
        quote['stock'],
        float(quote['top_bid']['price']),
        float(quote['top_ask']['price']),
        (float(quote['top_bid']['price']) + float(quote['top_ask']['price']))/2)
        )

  def test_getRatio_calculate(self):
    tuples_of_prices = [
      #'a' greater than 'b'
      {'price_a': 121.2, 'price_b': 120.48},
      #'a' equal to 'b'
      {'price_a': 121.2, 'price_b': 121.2},
      #'a' less than 'b'
      {'price_a': 120.48, 'price_b': 121.2}
    ]
    for set_of_two_prices in tuples_of_prices:
      #from the getRatio() function in client3.py,
      self.assertEqual(
        getRatio(float(set_of_two_prices['price_a']), float(set_of_two_prices['price_b'])),
        (float(set_of_two_prices['price_a'])/float(set_of_two_prices['price_b']))
        )


if __name__ == '__main__':
  try:
    unittest.main()
  except AttributeError:
    #This error was here from the begining
    pass
