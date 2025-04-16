select distinct user_id,order_date from table

select user_id,min(order_date) as first_order_date from first_table
group by user_id

select count(b.user_id) / count(a.user_id)
  from second_table a left join first_table b
 on a.user_id = b.user_id
and datediff(first_order_date,1) = b.order_date