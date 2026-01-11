-- SQLite CSV import script
.mode csv

.import 'data/raw/olist_customers_dataset.csv' olist_customers_dataset
.import 'data/raw/olist_geolocation_dataset.csv' olist_geolocation_dataset
.import 'data/raw/olist_orders_dataset.csv' olist_orders_dataset
.import 'data/raw/olist_order_items_dataset.csv' olist_order_items_dataset
.import 'data/raw/olist_order_payments_dataset.csv' olist_order_payments_dataset
.import 'data/raw/olist_order_reviews_dataset.csv' olist_order_reviews_dataset
.import 'data/raw/olist_products_dataset.csv' olist_products_dataset
.import 'data/raw/olist_sellers_dataset.csv' olist_sellers_dataset
.import 'data/raw/product_category_name_translation.csv' product_category_name_translation