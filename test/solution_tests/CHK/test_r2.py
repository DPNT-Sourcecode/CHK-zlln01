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
            ("BEBEEE", 160),
            ("ABCDEABCDE", 280),
            ("AAAAAEEB", 280),
            ("ABCDE", 155),
            ("AAAAAEEBAAABB", 455),
            ("ABCDECBAABCABBAAAEEAA", 665)
        ])
    def test_checkout(self, skus, expected_value):
        assert checkout(skus) == expected_value