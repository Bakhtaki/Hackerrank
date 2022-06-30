"""Script for Ordered Dict solution.
"""

# -----------------------------------------------------------------------------
# Task
# You have a list of N products with their prices that consumers bought on a
# particular day.
# Your task is to print each product's name and price in order of its first
# occurrence.
#
# item_name:name of the item
# net_price:price of the item
#
# Input Format
# The first line contains N, the number of items.
# The next N lines contains the item's name and price, separated by a space.
#
# Constraints
# 1 <= N <= 100
# Output Format
# Print the product's name and price in order of its first occurrence.
# Sample Input
# 5
# Bajaj Pulsar 200
# Samsung Galaxy 10 300
# Apple iPhone 6 150
# Samsung Galaxy 10 300
# Bajaj Pulsar 200
#
# Sample Output
# Bajaj Pulsar 400
# Samsung Galaxy 10 600
# Apple iPhone 6 150
# -----------------------------------------------------------------------------
# Solution

# Import libraries
from collections import OrderedDict

# Initialize OrderedDict
products = OrderedDict()

# Read N integers from input
n = int(input())

# Read N lines from input and repartition them in OrderedDict
for i in range(n):
    item_name, space,  net_price = input().rpartition(' ')
    products[item_name] = products.get(item_name, 0) + int(net_price)

# Print OrderedDict
for item_name, net_price in products.items():
    print(item_name, net_price)
