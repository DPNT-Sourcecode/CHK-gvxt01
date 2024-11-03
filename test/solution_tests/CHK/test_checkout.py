from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkoutReceiveList(self):
        assert checkout_solution.checkout('aBCE')== -1
        # assert True