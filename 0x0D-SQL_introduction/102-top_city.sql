-- list the 3 most hotests cities
SELECT `city`, AVG(`value`) AS `avg`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg` DESC
LIMIT 3;