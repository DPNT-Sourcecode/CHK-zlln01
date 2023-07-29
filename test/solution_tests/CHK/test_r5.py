import pytest

from solutions.CHK.checkout_solution import checkout


class TestCheckout():

    @pytest.mark.parametrize(
        "skus, expected_value",
        [
            ("AAAAA", 200),
            ("AAAAAAAA", 330),
            ("EEB", 80),
            ("EEBB", 110),
            ("EEEEBB", 160),
            ("BEBEEE", 160),
            ("ABCDEABCDE", 280),
            ("AAAAAEEB", 280),
            ("ABCDE", 155),
            ("AAAAAEEBAAABB", 455),
            ("ABCDECBAABCABBAAAEEAA", 665),
            ("FF", 20),
            ("FFF", 20),
            ("FFFFF", 40),
            ("FFFFFF", 40),
            ("ABCDEF", 165),
            ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 837),
            ("HHHHH", 45),
            ("HHHHHHHHHH", 80),
            ("KK", 120),
            ("NNNM", 120),
            ("NNN", 120),
            ("PPPPP", 200),
            ("QQQ", 80),
            ("RRRQ", 150),
            ("RRR", 150),
            ("UUU", 120),
            ("UUUU", 120),
            ("VV", 90),
            ("VVV", 130),
            ("PPPPQRUVPQRUVPQRUVSU", 730),
            ("SSS", 45),
            ("TTT", 45),
            ("XXX", 45),
            ("YYY", 45),
            ("ZZZ", 45),
            ("STX", 45),
            ("XYZ", 45),
            ("XXY", 45),
            ("XXXZ", 62),
            ("ZZXZ", 62),
            ("ZZZZZZXX", 124)
        ])
    def test_checkout(self, skus, expected_value):
        assert checkout(skus) == expected_value
