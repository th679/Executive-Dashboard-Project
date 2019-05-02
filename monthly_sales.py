# monthly_sales.py

import csv
import os
import itertools
from operator import itemgetter
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime


def to_usd(price):
    return "${0:,.2f}".format(price)


csv_filename = input("Please input a file name of the format sales-YYYYMM.csv:")

csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)   
#adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/d42b75d4f536ebeca5d6b1934926cdd95aeea714/notes/python/modules/os.md

exists = os.path.exists(csv_filepath)
#adapted from https://dbader.org/blog/python-check-if-file-exists

if exists == False:
    print("File does not exist")
    quit()


rows = []

with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        rows.append(dict(od))
        # adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution.py


sales_prices = []

for row in rows:
    sales_prices.append(float(row["sales price"]))

total_sales = sum(sales_prices)


product_sales = []

sorted_rows = sorted(rows, key=itemgetter("product"))
sort_by_product = itertools.groupby(sorted_rows, key=itemgetter("product"))
    #adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/e2d64e2d74621f3ff070175954878ba3f1562388/notes/python/modules/itertools.md

for product, rows in sort_by_product:
    sales = sum((float(row["sales price"]) for row in rows))
    product_sales.append({"name": product, "sales": sales})
    #adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py

sorted_product_sales = sorted(product_sales, key=itemgetter("sales"), reverse=True)
top_products = sorted_product_sales[0:3]
    #adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py


def period(month):
	months={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return months[month]
#adapted from https://github.com/hiepnguyen034/data_dashboard/blob/master/exec_dash.py

month_year = period(csv_filename[10:12])+' '+ str(csv_filename[6:10])


print("-----------------------")
print("MONTH: "+ month_year)
print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: " + to_usd(total_sales))

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for product in top_products:
    print(product["name"] + " " + to_usd(float(product["sales"])))

print("-----------------------")
print("VISUALIZING THE DATA...")


name_axis = []
sales_axis = []

for product in top_products:
    name_axis.append(product["name"])
    sales_axis.append(float(product["sales"]))

fig, ax = plt.subplots()

ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: to_usd(int(x))))
#adapted from https://preinventedwheel.com/matplotlib-thousands-separator-1-step-guide/

plt.barh(name_axis, sales_axis)
plt.ylabel('Product')
plt.xlabel('Sales (USD)')
plt.title('Top Selling Products: ' + month_year)
plt.tight_layout()
plt.show()
#adapted from dataviz-matplotlib slack channel