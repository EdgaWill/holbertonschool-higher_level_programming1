-- Temperatures
SELECT city, AVG(value)valueav FROM temperatures
GROUP BY city
ORDER BY valueav DESC
