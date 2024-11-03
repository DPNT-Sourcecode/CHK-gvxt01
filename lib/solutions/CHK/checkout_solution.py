from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

"""
    so I can use a dictionary to store the prices next to the item names 

    then I can use a counter to store the values in the input string 

    before calculating check all the input values are in the price list
"""


"""
CHK_R2
ROUND 2 - More offers
The checkout feature is great and our supermarket is doing fine. Is time to think about growth.
Our marketing teams wants to experiment with new offer types and we should do our best to support them.

We are going to sell a new item E.
Normally E costs 40, but if you buy 2 of Es you will get B free. 
How cool is that ? Multi-priced items also seemed to work well so we should have more of these.

Our price table and offers: 
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+


Notes: 
 - The policy of the supermarket is to always favor the customer when applying special offers.
 - All the offers are well balanced so that they can be safely combined.
 - For any illegal input return -1

In order to complete the round you need to implement the following method:
     checkout(String) -> Integer

Where:
 - param[0] = a String containing the SKUs of all the products in the basket
 - @return = an Integer representing the total checkout value of the items 
"""



def checkout(skus):
    if not isinstance(skus, str):
        return -1
    
    priceDict = {
        'A' : 50,
        'B' : 30,
        'C' : 20,
        'D' : 15,
        'E' : 40
    }

    specialDict = {
        'A' : (3, 130),
        'B' : (2, 45)
    }

    if ',' in skus:
        units = skus.split(',')
    else:
        # This is for the case where the input is a series of letters in a word
        units = list(skus)

    if len(set(units).difference(set(priceDict.keys()))) > 0:
        return -1
    
    resultsFreqs = Counter(units)
    total = 0

    # So no there are combo offers 
    for item in resultsFreqs.keys():
        specialExists =  specialDict.get(item, None) != None
        if not specialExists:
            total += resultsFreqs[item] * priceDict[item]
        else:
            inDeal = resultsFreqs[item] // specialDict[item][0]
            extra = resultsFreqs[item] % specialDict[item][0]

            total += inDeal * specialDict[item][1] + extra * priceDict[item]

    return total





test = checkout('AbC')
print(test)




