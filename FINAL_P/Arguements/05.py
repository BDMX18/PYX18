'''
*Q4. Calculate Total Bill (Default + args)

Write a function total_bill(discount=0, *prices) that calculates the total bill after applying the discount.
Discount is a percentage value (e.g., 10 means 10% off).

Sample Data:

total_bill(10, 100, 200, 300)  # 10% discount on total
total_bill(0, 50, 75, 125)
'''

def total_bill(discount = 0, *prices):
  total = 0
  for price in prices:
    total += price
  discounted = total - (total*(discount/100))
  return discounted

print(total_bill(10, 100, 200, 300))
print(total_bill(0, 50, 75, 125))