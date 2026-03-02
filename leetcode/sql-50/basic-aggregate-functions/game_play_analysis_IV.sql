-- SELECT 
--     ROUND(
--         COUNT(DISTINCT a.player_id) * 1.0 /
--         (SELECT COUNT(DISTINCT player_id) FROM Activity),
--         2
--     ) AS fraction
-- FROM Activity a
-- WHERE (a.player_id, a.event_date) IN (
--     SELECT player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
--     FROM Activity
--     GROUP BY player_id
-- );


SELECT
    ROUND(
        COUNT(DISTINCT f.player_id) * 1.0 / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2
    ) as fraction
FROM Activity a
JOIN (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) f
ON a.player_id = f.player_id
AND a.event_date = f.first_login + INTERVAL 1 DAY;
