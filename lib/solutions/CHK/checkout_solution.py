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
CHK_R5
ROUND 5 - A new offer type + price updates
All the other major supermarket have adopted a new offer type: group discount offer.
The offer could be presented like: buy any 3 of a group of items for 45
To keep up with the market, we need to make some price adjustments.
Please use the new and updated price table.

Our price table and offers: 
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+


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

def applyOffer(offerDict: dict, shopping: Counter, item: str)->Counter:
    # THis is a function to update the counter based on special deals and bogofs
    deal = offerDict[item]
    comboNeeded = deal['combo']
    comboExists = shopping >= comboNeeded

    copyShopping = deepcopy(shopping)

    while comboExists:
        shopping.subtract({item: deal['amount']})
        copyShopping.subtract(comboNeeded)
        comboExists = copyShopping >= comboNeeded


    return shopping

def checkout(skus):
    if not isinstance(skus, str):
        return -1
    
    priceDict = {
        'A' : 50,
        'B' : 30,
        'C' : 20,
        'D' : 15,
        'E' : 40,
        'F' : 10,
        'G' : 20,
        'H' : 10,
        'I' : 35,
        'J' : 60,
        'K' : 70,
        'L' : 90,
        'M' : 15,
        'N' : 40,
        'O' : 10,
        'P' : 50,
        'Q' : 30,
        'R' : 50,
        'S' : 20,
        'T' : 20,
        'U' : 40,
        'V' : 50,
        'W' : 20,
        'X' : 17,
        'Y' : 20,
        'Z' : 21,
    }

    multiBuyDict = {
        'A' : [(5, 200), (3, 130)],
        'B' : [(2, 45)],
        'H' : [(10, 80), (5, 45)],
        'K' : [(2, 120)],
        'P' : [(5, 200)],
        'Q' : [(3, 80)],
        'V' : [(3, 130), (2, 90)]
    }

    specialDict = {
        'B': {
            'amount': 1,
            'combo': Counter('EE')
        },
        'M': {
            'amount': 1,
            'combo': Counter('NNN')
        },
        'Q': {
            'amount': 1,
            'combo': Counter('RRR')
        },
    }

    bogofDict = {
        'F': {
            'amount': 1,
            'combo': Counter('FFF')
        },
        'U': {
            'amount': 1,
            'combo': Counter('UUUU')
        }
    }


    # Need another dict for the Buy x get one free deals or BOGOF. it can work like the specialbuys too

    # Need a groupby dict to handle the group and the amount you need
    # THis dit needs to store the items in descending order because you want to apply the deal in such a way to get the min price

    groupBuyDict = {
        'STXYZ' : {
            'combo': Counter('STXYZ'),
            'amount': 3,
            'price' : 45,
            'order' : ['Z', 'S', 'T', 'Y', 'X']
        }
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




    for item in basket.keys():
        
        groupBuyDeal = [groupBuyDict[group] for group in groupBuyDict.keys() if item in group]
        if len(groupBuyDeal) > 0:
            # assume no conflicting group buys
            print('Group deal identified')
            groupDeal = groupBuyDeal[0]
            print(groupDeal)
            groupDealCombo = groupDeal['combo']
            groupDealComboExists = sum(basket[item] for item in groupDealCombo.keys()) > groupDeal['amount']

            while groupDealComboExists:
                print(f'Applying deal {groupDealCombo}')
                total += groupDeal['price']
                deductedItems
                # basket.subtract(groupDealCombo)
                # total += groupDeal['amount']
                # diff = deepcopy(groupDealCombo)
                # diff.subtract(basket)
                # print(f'Diff is {diff.total()}')
                # groupDealComboExists = diff.total() <= groupDealCombo.total() - groupDeal['amount']


        bogofExists = bogofDict.get(item, None) != None
        if bogofExists:
            basket = applyOffer(offerDict=bogofDict, shopping=basket, item=item)

        specialBuyExists = specialDict.get(item, None) != None
        if specialBuyExists:
            basket = applyOffer(offerDict=specialDict, shopping=basket, item=item)

        


        multiBuyExists =  multiBuyDict.get(item, None) != None
        if not multiBuyExists:
            total += basket[item] * priceDict[item]
        else:
            deal_counter = 0
            while basket[item] > 0 and deal_counter < len(multiBuyDict[item]):
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

                deal_counter += 1
            if basket[item] > 0:
                    rest = basket[item] * priceDict[item]
                    total += rest
                    basket.subtract(Counter({item: basket[item]}))
        print(f'Current total for item :{item} is {total}')

            # total += inDeal * multiBuyDict[item][1] + extra * priceDict[item]

    return total











