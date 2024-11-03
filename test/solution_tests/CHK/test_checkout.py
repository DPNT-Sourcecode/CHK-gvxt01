from solutions.CHK import 

class TestCheckout():
    def checkoutNormal(self):
        assert checkout_solution.checkout('BABDDCAC')== 215
        # assert True

    def checkoutOneWrongItem(self):
        assert checkout_solution.checkout('babD')== -1
        # assert True
    def checkoutDealPlusOne(self):
        assert checkout_solution.checkout('aaaaaaa') == -1

    def checkoutWithTwoMulti(self):
        assert checkout_solution.checkout('AAAAAAAA') == 330

    # def checkoutWithCombo(self):
    #     assert checkout_solution.checkout('ABEEAAAAAAA') == 410


