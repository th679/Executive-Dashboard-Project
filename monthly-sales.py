# monthly_sales.py

# TODO: import some modules and/or packages here

import csv
import os

csv_filename = input("Please input a file name of the format sales-YYYYMM.csv:")

#if os.path.isfile(os.path.dirname(__file__), "data", csv_filename) == True:

csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

#else:
 #   print("No file at this location")
  #  breakpoint()

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