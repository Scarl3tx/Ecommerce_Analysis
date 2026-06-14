SELECT
    c.customer_id,
    c.customer_unique_id,
    c.customer_state,
    o.order_id,
    o.order_purchase_timestamp 
FROM olist_customers_dataset c
JOIN olist_orders_dataset o
    ON  c.customer_id = o.customer_id;
