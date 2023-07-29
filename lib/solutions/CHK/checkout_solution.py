from dataclasses import dataclass
from typing import Dict, Union, Optional, Any


# noinspection PyUnusedLocal
# skus = unicode string


@dataclass
class MultiPriceOffer:
    base_price: int
    prices: Dict[int, int]

    def calculate_price(self, sku_count: int, skus: Optional[str] = None) -> int:
        total = 0
        offer_count_ordered_by_count = sorted(self.prices.keys(), reverse=True)

        for offer_sku_count in offer_count_ordered_by_count:
            total += self.prices[offer_sku_count] * (sku_count // offer_sku_count)
            sku_count = sku_count % offer_sku_count
            if sku_count == 0:
                return total

        total += sku_count * self.base_price
        return total


@dataclass
class MultiBuyOffer:
    base_price: int
    multi_buy_offers: Dict[int, Dict[str, Union[int, str, MultiPriceOffer]]]

    def calculate_price(self, sku_count: int, skus: str) -> int:
        total = 0
        total += sku_count * self.base_price

        for offer_sku_count, offer in self.multi_buy_offers.items():
            # Calculate free products
            number_of_possible_free_skus = sku_count // offer_sku_count

            if number_of_possible_free_skus == 0:
                continue

            number_of_target_sku = skus.count(offer["sku"])
            original_offer_price = offer["special_offer"].calculate_price(
                number_of_target_sku
            )

            if number_of_possible_free_skus <= number_of_target_sku:
                calculated_price = offer["special_offer"].calculate_price(
                    number_of_target_sku - number_of_possible_free_skus
                )
                if original_offer_price > calculated_price:
                    total -= original_offer_price - calculated_price
                else:
                    total -= calculated_price
            else:
                calculated_price = offer["special_offer"].calculate_price(
                    number_of_target_sku
                )
                if original_offer_price > calculated_price:
                    total -= original_offer_price - calculated_price
                else:
                    total -= calculated_price

        return total


def get_price_table() -> Dict[str, Any]:
    price_table = {
        "A": {
            "price": 50,
            "special_offers": MultiPriceOffer(base_price=50, prices={3: 130, 5: 200}),
        },
        "B": {
            "price": 30,
            "special_offers": MultiPriceOffer(base_price=30, prices={2: 45}),
        },
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {
            "price": 40,
            "special_offers": MultiBuyOffer(
                base_price=40,
                multi_buy_offers={
                    2: {
                        "count": 1,
                        "base_price": 30,
                        "sku": "B",
                        "special_offer": MultiPriceOffer(base_price=30, prices={2: 45}),
                    }
                },
            ),
        },
        "F": {
            "price": 10,
            "special_offers": MultiBuyOffer(
                base_price=10,
                multi_buy_offers={
                    3: {
                        "count": 1,
                        "base_price": 10,
                        "sku": "F",
                        "special_offer": MultiPriceOffer(base_price=10, prices={}),
                    }
                },
            ),
        },
        "G": {"price": 20},
        "H": {
            "price": 10,
            "special_offers": MultiPriceOffer(base_price=10, prices={5: 45, 10: 80}),
        },
        "I": {"price": 35},
        "J": {"price": 60},
        "K": {
            "price": 80,
            "special_offers": MultiPriceOffer(base_price=80, prices={2: 150}),
        },
        "L": {"price": 90},
        "M": {"price": 15},
        "N": {
            "price": 40,
            "special_offers": MultiBuyOffer(
                base_price=40,
                multi_buy_offers={
                    3: {
                        "count": 1,
                        "base_price": 15,
                        "sku": "M",
                        "special_offer": MultiPriceOffer(base_price=15, prices={}),
                    }
                },
            ),
        },
        "O": {"price": 10},
        "P": {
            "price": 50,
            "special_offers": MultiPriceOffer(base_price=50, prices={5: 200}),
        },
        "Q": {
            "price": 30,
            "special_offers": MultiPriceOffer(base_price=30, prices={3: 80}),
        },
        "R": {
            "price": 50,
            "special_offers": MultiBuyOffer(
                base_price=50,
                multi_buy_offers={
                    3: {
                        "count": 1,
                        "base_price": 30,
                        "sku": "Q",
                        "special_offer": MultiPriceOffer(base_price=30, prices={}),
                    }
                },
            ),
        },
        "S": {"price": 30},
        "T": {"price": 20},
        "U": {
            "price": 40,
            "special_offers": MultiBuyOffer(
                base_price=40,
                multi_buy_offers={
                    4: {
                        "count": 1,
                        "base_price": 40,
                        "sku": "U",
                        "special_offer": MultiPriceOffer(base_price=40, prices={}),
                    }
                },
            ),
        },
        "V": {
            "price": 50,
            "special_offers": MultiPriceOffer(base_price=50, prices={2: 90, 3: 130}),
        },
        "W": {"price": 20},
        "X": {"price": 90},
        "Y": {"price": 10},
        "Z": {"price": 50},
    }

    return price_table


def get_price(sku: str, sku_count: int, skus: str) -> int:
    price_table = get_price_table()

    # Check if SKU in price table
    if price_table.get(sku, None) is None:
        raise ValueError

    total = 0
    # Check for special offers
    if price_table[sku].get("special_offers", None):
        return price_table[sku]["special_offers"].calculate_price(sku_count, skus)

    total = price_table[sku]["price"] * sku_count

    return total


def checkout(skus):
    sku_count = {}

    for sku in skus:
        sku_count[sku] = sku_count.get(sku, 0) + 1

    total = 0

    for sku, sku_count in sku_count.items():
        try:
            total += get_price(sku, sku_count, skus)
        except ValueError:
            return -1

    return total
