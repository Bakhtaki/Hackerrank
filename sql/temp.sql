/*
Write a query to output the start and end dates of projects listed
by the number of days it took to complete the project in ascending
order. If there is more than one project that have the same number
of completion days, then order by the start date of the project.
*/

SELECT start_date, end_date,
       (end_date - start_date) AS days_to_complete
FROM project