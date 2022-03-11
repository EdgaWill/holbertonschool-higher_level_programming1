-- Say my name
SELECT score, name FROM second_table
WHERE IS NOT NULL
ORDER BY score DESC;

INSERT INTO second_table (id,name,score)VALUES(5,'Aria',18);
INSERT INTO second_table (id,name,score)VALUES(5,'Aria',12);
