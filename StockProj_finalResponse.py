"""
AFOREMENTIONED INSTRUCTIONS

Challenge: create a class structure to represent stocks and bonds
Requirements:
-- Both stocks and bonds have a price
-- Stocks have a company name and ticker
-- Bonds have a description, duration, and yield
-- You should not be able to instantiate the base class
-- Subclasses are required to override get_description()
-- get_description returns formats for stocks and bonds
For stocks: "Ticker: Company -- $Price"
For bonds: "description: duration'yr' : $price : yieldamt%"

ADDITIONAL INSTRUCTIONS

Challenge: use a magic method to make stocks and bonds sortable
Stocks should sort from low to high on price
Bonds should sort from low to high on yield

"""
#--------------------------------------------------------------

# import abstract base class library
from abc import ABC, abstractmethod
from dataclasses import dataclass
import doctest

# create Asset class that inherits from ABC
@dataclass
class Asset(ABC):
    """
    Base class for assets.

    >>> a = Asset(100)
    Traceback (most recent call last):
        ...
    TypeError: Can't instantiate abstract class Asset without an implementation for abstract method '__str__'

    """
    price: float = 0.0

    # define an abstract method that returns a string representation of the objects
    @abstractmethod
    def __str__(self):
        pass

class Sort(ABC):
    """
        This is to test the functuality of sorting mechanisms in this class for sorting

        >>> stocks = [Stock("AAPL", 150.0, "Apple Inc"), Stock("MSFT", 250.0, "Microsoft Corp"), Stock("GOOG", 100.0, "Google Inc")]
        >>> sorted_stocks = Sort().merge_sort(stocks)
        >>> [str(stock) for stock in sorted_stocks]
        ['GOOG: Google Inc -- $100.0', 'AAPL: Apple Inc -- $150.0', 'MSFT: Microsoft Corp -- $250.0']

        >>> bonds = [Bond(100.0, "5 Year Bond", 5, 2.0), Bond(200.0, "10 Year Bond", 10, 1.5), Bond(150.0, "7 Year Bond", 7, 2.5)]
        >>> sorted_bonds = Sort().merge_sort(bonds)
        >>> [str(bond) for bond in sorted_bonds]
        ['10 Year Bond: 10 : $200.0 : 1.5', '5 Year Bond: 5 : $100.0 : 2.0', '7 Year Bond: 7 : $150.0 : 2.5']
        """
    # Merge Sort Algorithm
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

# create Stock subclass that inherits price and include ticker, price, and company attributes
class Stock(Sort, Asset):
    """
    These tests ensure that the methods are reflectings stocks and their relationships to each other properly.

    >>> s = Stock("MSFT", 342.0, "Microsoft Corp")
    >>> print(s)
    MSFT: Microsoft Corp -- $342.0

    >>> goog = Stock("GOOG", 135.0, "Google Inc")
    >>> msft = Stock("MSFT", 342.0, "Microsoft Corp")
    >>> goog < msft
    True

    """
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company
        self.stockList = []

    # mandated string format class
    def __str__(self):
        strFormat = f"{self.ticker}: {self.company} -- ${self.price}"
        return strFormat

    # provide less than magic method for sorting function
    def __lt__(self, value):
        return self.price < value.price

    # iterate through the tuple appending stocks to make a stockList
    def compile_stockList(self, *stocks):
        for i in range(len(stocks)):
            self.stockList.append(stocks[i])
        return self.stockList

    # method to sort the stockList
    def sort_stockList(self):
        self.stockList = self.merge_sort(self.stockList)
        return self.stockList

# create Bond subclass that inherits price include price, description, duration, and yeildAmt attributes
class Bond(Sort, Asset):
    """
    These tests ensure that the methods are reflectings stocks and their relationships to each other properly.

    >>> b = Bond(95.31, "30 Year US Treasury", 30, 4.38)
    >>> print(b)
    30 Year US Treasury: 30 : $95.31 : 4.38

    >>> us30yr = Bond(95.31, "30 Year US Treasury", 30, 4.38)
    >>> us10yr = Bond(96.70, "10 Year US Treasury", 10, 4.28)
    >>> us30yr < us10yr
    False

    """
    def __init__(self, price, description, duration, yeildAmt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yeildAmt = yeildAmt
        self.bondList = []

    # mandated string format class
    def __str__(self):
        strFormat = f"{self.description}: {self.duration} : ${self.price} : {self.yeildAmt}"
        return strFormat

    # provide less than magic method for sorting function
    def __lt__(self, value):
        return self.yeildAmt < value.yeildAmt

    # iterate through the tuple appending bonds to make a bondList
    def compile_bondList(self, *bonds):
        for i in range(len(bonds)):
            self.bondList.append(bonds[i])
        return self.bondList

    # method to sort the bondList
    def sort_bondList(self):
        self.bondList = self.merge_sort(self.bondList)
        return self.bondList

# Run doctests
if __name__ == "__main__":
    doctest.testmod()

    # create stock objects
    msft = Stock("MSFT", 342.0, "Microsoft Corp")
    goog = Stock("GOOG", 135.0, "Google Inc")
    meta = Stock("META", 275.0, "Meta Platforms Inc")
    amzn = Stock("AMZN", 120.0, "Amazon Inc")

    # create bond objects
    us30yr = Bond(95.31, "30 Year US Treasury", 30, 4.38)
    us10yr = Bond(96.70, "10 Year US Treasury", 10, 4.28)
    us5yr = Bond(98.65, "5 Year US Treasury", 5, 4.43)
    us2yr = Bond(99.57, "2 Year US Treasury", 2, 4.98)

    # add stock and bond instances to unique tuples
    stockList = goog.compile_stockList(msft, goog, meta, amzn)
    sortedStocks = goog.sort_stockList()
    print("Sorted Stocks:")
    for stock in sortedStocks:
        print(stock)

    # add stock and bond instances to unique tuples
    bondList = us2yr.compile_bondList(us30yr, us10yr, us5yr, us2yr)
    sortedBonds = us2yr.sort_bondList()
    print("Sorted Bonds:")
    for bond in sortedBonds:
        print(bond)
