def promo_price(total, payment):
    if total >= 500_000 and payment.lower() == "shopeepay":
        return total * 0.9
    return total

assert promo_price(500_000, "ShopeePay") == 450_000
assert promo_price(499_999, "ShopeePay") == 499_999
assert promo_price(550_000, "OVO") == 550_000

print("Semua kasus uji promo berhasil (PASSED)!")