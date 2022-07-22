/*
Pivot the Occupation column in OCCUPATIONS so that each Name
is sorted alphabetically and displayed underneath its corresponding
Occupation. The output column headers should be Doctor, Professor,
 Singer, and Actor, respectively.

*/
SELECT
    [Doctor], [Professor], [Singer], [Actor]
FROM
(
    SELECT ROW_NUMBER() OVER (PARTITION BY OCCUPATION ORDER BY NAME)
     [RowNumber], * FROM OCCUPATIONS
) AS tempTable
PIVOT
(
    MAX(NAME) FOR OCCUPATION IN ([Doctor], [Professor], [Singer], [Actor])
) AS pivotTable