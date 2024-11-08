from collections import Counter

from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkoutNormal(self):
        assert checkout_solution.checkout('BABDDCAC')== 215
        # assert True

    def test_checkoutOneWrongItem(self):
        assert checkout_solution.checkout('babD')== -1
        # assert True

    def test_checkoutDealPlusOne(self):
        assert checkout_solution.checkout('aaaaaaa') == -1

    def test_checkoutWithTwoMulti(self):
        assert checkout_solution.checkout('AAAAAAAAA') == 380
        assert checkout_solution.checkout('AAAA') == 180

    def test_checkoutWithCombo(self):
        assert checkout_solution.checkout('ABEEAAAAAAA') == 410
        assert checkout_solution.checkout('ABEEAAAAAAAEEB') == 490
        assert checkout_solution.checkout('EEBEEB') == 160

    def test_checkoutWithBogof(self):
        assert checkout_solution.checkout('FFFABCDE') == 175
        assert checkout_solution.checkout('FFFABCDEFFF') == 195
        assert checkout_solution.checkout('EEBEEBAAAAFFF') == 360

    def test_checkoutLargeStore(self):
        assert checkout_solution.checkout('RRRQQQQHHHHHKVV') == 435

    def test_checoutGroupBuy(self):
        assert checkout_solution.checkout('STXYZSTXYZY') == 169
        assert checkout_solution.checkout('NNNMMFFFBEESTXYZ') == 317
        assert checkout_solution.checkout('STZ') == 45
        assert checkout_solution.checkout('STXSTX') == 90
        assert checkout_solution.checkout('SSS') == 45
        


    def test_applyOffer(self):
        assert checkout_solution.applyOffer(
            offerDict={
                'F': {
                    'amount': 1,
                    'combo': Counter('FFF')
                },
                'U': {
                    'amount': 1,
                    'combo': Counter('UUUU')
                },
            },
            shopping=Counter('FFFD'),
            item='F'
        ) == Counter('FFD')
        assert checkout_solution.applyOffer(
            offerDict={
                'G': {
                    'amount': 2,
                    'combo': Counter('FFF')
                },
                'T': {
                    'amount': 1,
                    'combo': Counter('UUUU')
                },
            },
            shopping=Counter('FFFDGG'),
            item='G'
        ) == Counter('FFFD')


