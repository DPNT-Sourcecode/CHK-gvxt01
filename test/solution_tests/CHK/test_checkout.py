from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkoutReceiveList(self):
        assert checkout_solution.checkout('ABC')== ['A', 'B', 'C']
        # assert True