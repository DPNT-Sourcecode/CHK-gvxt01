from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkoutReceiveList(self):
        assert checkout_solution.checkout('A,B,c')== ['A', 'B', 'C']
        # assert True