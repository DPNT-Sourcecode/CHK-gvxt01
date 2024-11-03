"""
CHK_R1
ROUND 1 - Our supermarket
The purpose of this challenge is to implement a supermarket checkout that calculates the total price of a number of items.

In a normal supermarket, things are identified using Stock Keeping Units, or SKUs. 
In our store, we'll use individual letters of the alphabet (A, B, C, and so on). 
Our goods are priced individually. 
In addition, some items are multi-priced: buy n of them, and they'll cost you y pounds. 


For example, item A might cost 50 pounds individually, but this week we have a special offer: 
 buy three As and they'll cost you 130.

Our price table and offers: 
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+


Notes: 
 - For any illegal input return -1

In order to complete the round you need to implement the following method:
     checkout(String) -> Integer

Where:
 - param[0] = a String containing the SKUs of all the products in the basket
 - @return = an Integer representing the total checkout value of the items 

"""

# noinspection PyUnusedLocal
# skus = unicode string

"""
    so I can use a dictionary to store the prices next to the item names 

    then I can use a counter to store the values in the input string 

    before calculating check all the input values are in the price list
"""
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    
    # Not known whether the input is a list of capital letters, comma separated or just one word so separation will be needed to handle both

    priceDict = {
        'A' : 50,
        'B' : 30,
        'C' : 20,
        'D' : 15
    }

    # Special buys. dict val is a tuple with the number and the value

    specialDict = {
        'A' : (3, 130),
        'B' : (2, 45)
    }

    if ',' in skus:
        units = [unit.upper() for unit in skus.split(',')]
    else:
        # This is for the case where the input is a series of letters in a word
        units = list(skus.upper())

    if len(set(units).difference(set(priceDict.keys()))) > 0:
        return -1




test = checkout('AbCD')
print(test)
