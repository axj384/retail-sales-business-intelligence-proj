-- SQLite: run after loading sample_data.csv into table retail_orders
SELECT category, COUNT(*) AS orders, ROUND(SUM(revenue),2) AS revenue, ROUND(AVG(revenue),2) AS avg_order_value FROM retail_orders GROUP BY category ORDER BY revenue DESC;
SELECT substr(order_date,1,7) AS month, ROUND(SUM(revenue),2) AS monthly_revenue FROM retail_orders GROUP BY month ORDER BY month;
WITH ranked AS (SELECT customer_id, SUM(revenue) AS spend, DENSE_RANK() OVER(ORDER BY SUM(revenue) DESC) AS customer_rank FROM retail_orders GROUP BY customer_id) SELECT * FROM ranked WHERE customer_rank<=10;
