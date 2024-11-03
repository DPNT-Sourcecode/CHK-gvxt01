from solutions.HLO import hello_solution

class TestHello():
    def test_hello(self):
        assert hello_solution.hello('John')== "Hello, John!"

from solutions.CHK import checkout_solution


