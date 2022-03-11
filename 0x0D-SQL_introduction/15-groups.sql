-- Number by score
SELECT DISTINCT (score), COUNT(score)number FROM SECOND_TABLE
GROUP BY score
ORDER BY score DESC
