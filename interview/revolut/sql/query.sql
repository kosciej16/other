SELECT user_id, sum(coalesce(amount*rate, amount)) paid from transactions t
LEFT JOIN exchange_rates e
ON e.from_currency = t.currency
AND e.ts = (
    SELECT max(e2.ts)
    FROM exchange_rates e2
    WHERE e2.from_currency = e.from_currency
    AND e2.to_currency = 'GBP'
    -- Uncomment to get solution for task 2
    AND e2.ts <= t.ts
)
WHERE e.to_currency = 'GBP'
group by user_id
order by user_id
