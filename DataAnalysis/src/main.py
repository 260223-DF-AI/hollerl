import pandas as pd
import datetime

import analysis
import visualizations


df = pd.DataFrame({
        'order_id': [1, 2, 3],
        'customer_id': ['C001', 'C002', 'C001'],
        'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-02']),
        'product_name': ['Widget', 'Gadget', 'Widget'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'quantity': [2, 1, 3],
        'unit_price': [10.00, 25.00, 10.00],
        'region': ['North', 'South', 'North']
    })

df_test = pd.DataFrame({
        'order_id': [1, 2, 3],
        'customer_id': ['C001', 'C002', 'C001'],
        'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-02']),
        'product_name': ['Widget', 'Gadget', 'Widget'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'quantity': [2, 1, 3],
        'unit_price': [10.00, 25.00, 10.00],
        'region': ['North', 'South', 'North']
    })

pd.set_option('display.max_columns', None)
print(df)
print(df_test)