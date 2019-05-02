import pytest
import csv
import os
import itertools
from operator import itemgetter
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime


from monthly_sales import to_usd, get_top_products

def test_to_usd():
    assert to_usd(5) == "$5.00"
    assert to_usd(5.777) == "$5.78"
    assert to_usd(12345) == "$12,345.00"

def test_get_top_products():
    csv_filename = "sales-201710.csv"
    csv_filepath = os.path.join(os.path.dirname(__file__), "mock_data", csv_filename)
    rows = []
    with open(csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for od in reader:
            rows.append(dict(od))
    results = get_top_products(rows)
    assert results == [
        {'name': 'Button-Down Shirt', 'sales': 5464.200000000001},
        {'name': 'Super Soft Sweater', 'sales': 2249.8500000000004},
        {'name': 'Super Soft Hoodie', 'sales': 1800.0}
    ]