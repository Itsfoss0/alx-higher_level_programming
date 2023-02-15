-- maximum temperature of each state
SELECT `state`, max(value) as `maximum_temperature`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;