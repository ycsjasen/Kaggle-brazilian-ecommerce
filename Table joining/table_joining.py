import sys
sys.path.insert(1, 'C:\\Users\\ycsja\\Desktop\\github\\Kaggle brazilian ecommerce')

import numpy as np
import pandas as pd
from Data_loading.data_loading import orders


def table_join(left, right_file, join_key):
    right = pd.read_csv('../' + right_file + '.csv')
    joined = pd.merge(left, right, how='left', on=join_key)
    return joined


joined_table = orders
joined_table = table_join(left=joined_table, right_file='olist_customers_dataset', join_key='customer_id')
joined_table = table_join(joined_table, 'olist_order_payments_dataset', join_key='order_id')
joined_table = table_join(joined_table, 'olist_order_reviews_dataset', join_key='order_id')
joined_table = table_join(joined_table, 'olist_order_items_dataset', join_key='order_id')
joined_table = table_join(joined_table, 'olist_products_dataset', join_key='product_id')
joined_table = table_join(joined_table, 'olist_sellers_dataset', join_key='seller_id')


joined_table.to_csv('megatable.csv', index=False)
