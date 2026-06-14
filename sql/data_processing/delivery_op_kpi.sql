WITH delivery_data AS (
SELECT 
    o.order_purchase_timestamp,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date,
    o.order_id,
    c.customer_state,
    r.review_score,
    julianday(o.order_delivered_customer_date)
    - julianday(o.order_estimated_delivery_date)
    AS delivery_delay_days,
    CASE 
        WHEN julianday(o.order_delivered_customer_date)
           > julianday(o.order_estimated_delivery_date)
        THEN 1 
        WHEN julianday(o.order_delivered_customer_date)
           = julianday(o.order_estimated_delivery_date)
        THEN 0
        WHEN julianday(o.order_delivered_customer_date)
           < julianday(o.order_estimated_delivery_date)
        THEN -1  
    END AS is_late
FROM olist_orders_dataset o
JOIN olist_customers_dataset c
    ON o.customer_id = c.customer_id
JOIN olist_order_reviews_dataset r
    ON o.order_id = r.order_id
)
SELECT *
FROM delivery_data
WHERE delivery_delay_days <=60;