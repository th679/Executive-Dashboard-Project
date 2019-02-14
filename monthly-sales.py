# monthly_sales.py

# TODO: import some modules and/or packages here

import csv
import os
import itertools
from operator import itemgetter

csv_filename = input("Please input a file name of the format sales-YYYYMM.csv:")

csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

rows =[]

with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        rows.append(dict(od))
        # adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution.py

sales_prices = []

for row in rows:
    sales_prices.append(float(row["sales price"]))

total_sales = sum(sales_prices)
usd = "${0:,.2f}"

product_sales = []

sorted_rows = sorted(rows, key=itemgetter("product"))
sort_by_product = itertools.groupby(sorted_rows, key=itemgetter("product"))
    #adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/e2d64e2d74621f3ff070175954878ba3f1562388/notes/python/modules/itertools.md

for product, rows in sort_by_product:
    sales = sum((float(row["sales price"]) for row in rows))
    product_sales.append({"name": product, "sales": sales})
    #adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py

print(product_sales)


print(usd.format(total_sales))

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")