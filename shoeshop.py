"""Calculate shoe Shop Income."""

# A counter is a container that stores elements
# as dictionary keys,and their counts are
# stored as dictionary values.

# --------------------------------------------------------------
# The first line contains X, the number of shoes.
# The second line contains the space separated list
# of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the
# desired by the customer and , the price of the shoe
# --------------------------------------------------------------

# Imports
from collections import Counter

shoe_count = int(input())
shoe_sizes = Counter(map(int, input().split()))
customer_count = int(input())
total_price = 0


for _ in range(customer_count):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        shoe_sizes[size] -= 1
        total_price += price

# Print the total price of all the shoes sold
print(total_price)
