'''
Flexible Discount Calculator

Problem:
Write a function apply_discount(price, *discounts, **options) that applies multiple discounts sequentially to a price.

Discounts in *discounts are percentages.

options may include tax (percentage to add) and round_to (decimal places).

Return final price after applying discounts and tax.

Sample Input:

apply_discount(1000, 10, 20, tax=5, round_to=1)


Expected Output:

684.0


(Explanation: 1000 -> 10% off = 900 -> 20% off = 720 -> +5% tax = 756 rounded to 1 decimal)
'''

def apply_discount(price, *discounts, **options):
  print(f'Price Before Discount: {price}')
  print('\t\t\t\tApplying Discounts!')
  for discount in discounts:
    price -= (price * (discount/100))
    print(f'\tPrice: {price} After {discount}% Discount!')
  if 'tax' in options:
    price += (price * options['tax']/100)
    print(f'\tPrice: {price} After {options['tax']}% Tax!')
  if 'round_to' in options:
    price = round(price, options['round_to'])
    print(f'\tPrice: {price} After Rounding Off By {options["round_to"]}')

apply_discount(1000, 10, 20, tax=5, round_to=1)