SELECT DISTINCT city
FROM station
WHERE city REGEXP "[^a,e,u,i,o]$";