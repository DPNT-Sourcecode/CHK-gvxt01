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

    def test_checkoutWithCombo(self):
        assert checkout_solution.checkout('ABEEAAAAAAA') == 410

    def test_checkoutInA(self):
        




