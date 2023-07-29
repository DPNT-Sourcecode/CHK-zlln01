

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

    for sku, sku_count in 
