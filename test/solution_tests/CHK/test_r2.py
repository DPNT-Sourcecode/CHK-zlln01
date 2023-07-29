import pytest

from solutions.CHK.checkout_solution import checkout


class TestCheckout():

    @pytest.mark.parametrize(
        "skus, expected_value",
        [
            ("AAAAA", 200),
            ("AAAAAAAA", 330),
            ("AAABCDF", -1),
            ("EEB", 80),
            ("EEBB", 110),
            ("EEEEBB", 160),
            ("AAAAAEEB", 280),
        ])
    def test_checkout(self, skus, expected_value):
        assert checkout(skus) == expected_value
