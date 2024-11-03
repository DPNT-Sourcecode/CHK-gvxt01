from collections import Counter
from copy import deepcopy
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

    multiBuyDict = {
        'A' : [(5, 200), (3, 130)],
        'B' : [(2, 45)]
    }

    if ',' in skus:
        units = skus.split(',')
    else:
        # This is for the case where the input is a series of letters in a word
        units = list(skus)

    if len(set(units).difference(set(priceDict.keys()))) > 0:
        return -1
    
    basket = Counter(units)
    total = 0
    basketToEdit = deepcopy(basket)
    # So no there are combo offers and multiple offers
    # To support this I'll make a combo structure and put the multi buys as a list of tuples
    for item in basket.keys():
        multiBuyExists =  multiBuyDict.get(item, None) != None
        if not multiBuyExists:
            total += basket[item] * priceDict[item]
        else:
            deal_counter = 0
            while basket[item] > 0:
                print(f'Deal counter: {deal_counter} and item: {item}')
                print(f'basket has {basket[item]} left of {item}')
                print(basket)
                deal = multiBuyDict[item][deal_counter]
                inDeal = basket[item] // deal[0]
                if inDeal > 0:
                    print('in deal')
                    print(f'subtracting: {inDeal * deal[0]}')
                    basket.subtract(Counter({item: inDeal * deal[0]}))
                    total += inDeal * deal[1]
                    print(basket)
                else:
                    rest = basket[item] * priceDict[item]
                    total += rest

                deal_counter += 1

            # total += inDeal * multiBuyDict[item][1] + extra * priceDict[item]

    return total








