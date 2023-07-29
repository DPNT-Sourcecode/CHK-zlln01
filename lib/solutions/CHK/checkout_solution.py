

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        "A": {"price": 50, "special_offers": {"count": 3, "price": 130}},
        "B": {"price": 30, "special_offers": {"count": 2, "price": 45}},
        "C": {"price": 20},
        "D": {"price": 15},
    }

    sku_count = {}

    for sku in skus:
        sku_count[sku] = sku_count.get(sku, 0) + 1

    total = 0

    for sku, sku_count in sku_count.items():
        # Check if SKU in price table
        if price_table.get(sku, None) is None:
            return -1

        # Check for special offers
        if price_table[sku].get("special_offers", None):
            if price_table[sku]["special_offers"]["count"] == sku_count:
                total += price_table[sku]["special_offers"]["price"]
                continue

        total += (sku * sku_count)

    return total
