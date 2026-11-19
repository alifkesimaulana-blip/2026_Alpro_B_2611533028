# code sebelum di perbaiki

# Canteen menu prices (rupiah)
# prices = [15000, 22000, 8000, 30000]
# # Make a discounted copy: 2000 off every item
# sale_prices = prices
# for i in range(len(sale_prices)):
#     sale_prices[i] = sale_prices[i] - 2000
# # Raise every normal price by 1000
# for price in prices:
#     price = price + 1000
# print("Normal:", prices)
# print("Sale:", sale_prices)

# code setelah di perbaiki 

prices = [15000, 22000, 8000, 30000]

sale_prices = prices.copy()

for i in range(len(sale_prices)):
    sale_prices[i] = sale_prices[i] - 2000

for i in range(len(prices)):
    prices[i] = prices[i] + 1000

print("Normal:", prices)
print("Sale:", sale_prices)