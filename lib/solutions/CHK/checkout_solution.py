

# noinspection PyUnusedLocal
# skus = unicode string
def get_price(sku: str, sku_count: int) -> int:
    price_table = {
        "A": {"price": 50, "special_offers": [{"count": 3, "price": 130}, {"count": 5, "price": 200}]},
        "B": {"price": 30, "special_offers": [{"count": 2, "price": 45}]},
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
        if price_table[sku]["special_offers"]["count"] <= sku_count:
            total += price_table[sku]["special_offers"]["price"] * (
                        sku_count // price_table[sku]["special_offers"]["count"])
            total += price_table[sku]["price"] * (sku_count % price_table[sku]["special_offers"]["count"])
            return total

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