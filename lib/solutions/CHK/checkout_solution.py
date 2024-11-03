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
CHK_R3
ROUND 3 - More items and offers
A new item has arrived. Item F.
Our marketing team wants to try rewording the offer to see if it affects consumption
Instead of multi-pricing this item they want to say "buy 2Fs and get another F free"
The offer requires you to have 3 Fs in the basket.

Our price table and offers: 
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
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
        'E' : 40,
        'F' : 10
    }

    multiBuyDict = {
        'A' : [(5, 200), (3, 130)],
        'B' : [(2, 45)]
    }

    specialDict = {
        'B': {
            'amount': 1,
            'combo': Counter('EE')
        }
    }

    bogofDict = {
        'F': {
            'amount': 1,
            'combo': Counter('FFF')
        }
    }


    # Need another dict for the Buy x get one free deals or BOGOF. it can work like the specialbuys too



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


        bogofExists = bogofDict.get(item, None) != None
        if bogofExists:
            bogofDeal = bogofDict[item]
            bogofComboNeeded = bogofDeal['combo']
            bogofComboExists = basket >= bogofComboNeeded

            testBasket = deepcopy(basket)

            while bogofComboExists:
                basket.subtract({item: bogofDeal['amount']})
                testBasket.subtract(bogofComboNeeded)
                bogofComboExists = testBasket >= bogofComboNeeded

        specialBuyExists = specialDict.get(item, None) != None
        if specialBuyExists:
            specialDeal = specialDict[item]
            comboNeeded = specialDeal['combo']
            comboExists = basket >= comboNeeded

            testBasket = deepcopy(basket)

            while comboExists:
                basket.subtract({item: specialDeal['amount']})
                testBasket.subtract(comboNeeded)
                comboExists = testBasket >= comboNeeded

        


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






