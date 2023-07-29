import pytest

from solutions.CHK.checkout_solution import checkout


class TestCheckout():

    @pytest.mark.parametrize(
        "skus, expected_value",
        [
            ("A", 50),
            ("AAABCD", 195),
            ("AAABCDE", -1),
            ("AAAABCD", 245),
            ("AAAA", 180),
            ("AAAAA", 230),
            ("AAAAAA", 260),
        ])
    def test_checkout(self, skus, expected_value):
        assert checkout(skus) == expected_value