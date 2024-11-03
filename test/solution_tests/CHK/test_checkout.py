from solutions.CHK import checkout_solution


class TestCheckout():
    def checkoutOneWrongItem(self):
        assert checkout_solution.checkout('BABDDCAC')== 215
        # assert True

    def checkoutDealPlusOne(self):
        assert checkout_solution.checkout('aaaaaaa') == 310
