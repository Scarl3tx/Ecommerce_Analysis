SELECT 
    oi.price,
    o.order_purchase_timestamp,
    c.customer_state,
    t.product_category_name_english,
    oi.product_id,
    o.order_id
FROM olist_orders_dataset o
JOIN olist_order_items_dataset oi
    ON o.order_id = oi.order_id
JOIN olist_customers_dataset c
    ON o.customer_id = c.customer_id 
JOIN olist_products_dataset p
    ON oi.product_id = p.product_id
JOIN product_category_name_translation t
    ON p.product_category_name = t.product_category_name;