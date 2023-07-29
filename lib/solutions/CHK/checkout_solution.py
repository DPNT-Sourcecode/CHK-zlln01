from dataclasses import dataclass
from typing import Dict, Union, Optional


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
    multi_buy_offers: Dict[int, Dict[str, Union[int, str]]]

    def calculate_price(self, sku_count: int, skus: str) -> int:
        total = 0
        total += sku_count * self.base_price

        for offer_sku_count, offer in self.multi_buy_offers.items():
            # Calculate free products
            number_of_possible_free_skus = sku_count // offer_sku_count

            number_of_target_sku = skus.count(offer["sku"])

            if number_of_possible_free_skus <= number_of_target_sku:
                total -= number_of_possible_free_skus * offer["base_price"]
            else:
                total -= number_of_target_sku * offer["base_price"]

        return total

def get_price(sku: str, sku_count: int, skus: str) -> int:
    price_table = {
        "A": {"price": 50, "special_offers": MultiPriceOffer(base_price=50, prices={3: 130, 5: 200})},
        "B": {"price": 30, "special_offers": MultiPriceOffer(base_price=30, prices={2: 45})},
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {"price": 40, "special_offers": MultiBuyOffer(base_price=40, multi_buy_offers={2: {"count": 1, "base_price": 30, "sku": "B"}})}
    }

    # Check if SKU in price table
    if price_table.get(sku, None) is None:
        raise ValueError

    total = 0
    # Check for special offers
    if price_table[sku].get("special_offers", None):
        return price_table[sku]["special_offers"].calculate_price(sku_count, skus)

    total = (price_table[sku]["price"] * sku_count)

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

