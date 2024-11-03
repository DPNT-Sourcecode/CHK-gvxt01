from solutions.CHK import checkout_solution


class TestCheckout():
    def checkoutNormal(self):
        assert checkout_solution.checkout('BABDDCAC')== 215
        # assert True

    def checkoutOneWrongItem(self):
        assert checkout_solution.checkout('babD')== -1
        # assert True
    def checkoutDealPlusOne(self):
        assert checkout_solution.checkout('aaaaaaa') == -1

    def checkoutWith

    def checkoutWithCombo(self):
        assert checkout_solution.checkout('ABEEAAAAAAA') == 410