from dataclasses import dataclass
from typing import Dict


# noinspection PyUnusedLocal
# skus = unicode string

@dataclass
class MultiPriceOffer:
    base_price: int
    prices: Dict[int, int]

    def calculate_price(self, sku_count: int) -> int:
        total = 0
        offer_count_ordered_by_count = sorted(self.prices.keys(), reverse=True)

        for offer_sku_count in offer_count_ordered_by_count:
            total += self.prices[offer_sku_count] * (sku_count // offer_sku_count)
            sku_count = sku_count % offer_sku_count
            if sku_count == 0:
                return total

        total += sku_count * self.base_price
        return total



def get_price(sku: str, sku_count: int) -> int:
    price_table = {
        "A": {"price": 50, "special_offers": MultiPriceOffer(base_price=50, prices={3: 130, 5: 200})},
        "B": {"price": 30, "special_offers": MultiPriceOffer(base_price=30, prices={2: 45})},
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {"price": 40, "special_offers": []}
    }

    # Check if SKU in price table
    if price_table.get(sku, None) is None:
        raise ValueError

    total = 0
    # Check for special offers
    if price_table[sku].get("special_offers", None):
        # if price_table[sku]["special_offers"]["count"] <= sku_count:
        #     total += price_table[sku]["special_offers"]["price"] * (
        #                 sku_count // price_table[sku]["special_offers"]["count"])
        #     total += price_table[sku]["price"] * (sku_count % price_table[sku]["special_offers"]["count"])
        #     return total
        return price_table[sku]["special_offers"].calculate_price(sku_count)


    total = (price_table[sku]["price"] * sku_count)

    return total


def checkout(skus):
    sku_count = {}

    for sku in skus:
        sku_count[sku] = sku_count.get(sku, 0) + 1

    total = 0

    for sku, sku_count in sku_count.items():
        try:
            total += get_price(sku, sku_count)
        except ValueError:
            return -1

    return total
