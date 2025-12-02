-- Analysis Query for Performance Tuning
SELECT * FROM Users u
JOIN Orders o ON u.id = o.user_id
WHERE u.created_at > '2023-01-01'
AND o.total > 1000;