import numpy as np
import pandas as pd

# Loading all data sets
customer = pd.read_csv('../olist_customers_dataset.csv')
geolocation = pd.read_csv('../olist_geolocation_dataset.csv')
order_items = pd.read_csv('../olist_order_items_dataset.csv')
order_pay = pd.read_csv('../olist_order_payments_dataset.csv')
order_review = pd.read_csv('../olist_order_reviews_dataset.csv')
orders = pd.read_csv('../olist_orders_dataset.csv')
products = pd.read_csv('../olist_products_dataset.csv')
sellers = pd.read_csv('../olist_sellers_dataset.csv')

# Applying product category translation
products = pd.merge(products, pd.read_csv('../product_category_name_translation.csv'), how='left',
                    left_on='product_category_name',
                    right_on='product_category_name')

# Show all columns
pd.set_option('display.max_columns', None)
# Show all lines
pd.set_option('display.max_rows', None)
# value display length is 100, the default is 50
pd.set_option('max_colwidth', 100)


