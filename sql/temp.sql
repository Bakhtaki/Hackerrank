/*
Query an alphabetically ordered list of all names in OCCUPATIONS,
immediately followed by the first letter of each profession as
a parenthetical (i.e.: enclosed inparentheses). For example:
AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).

*/
select (name || '(' || UPPER(substr(occupation, 1, 1)) || ')')
from occupations
order by name;
/*
Query the number of ocurrences of each occupation in OCCUPATIONS.
Sort the occurrences in ascending order, and output them in the following format:
*/
select (
        'There are a total of' || count(name) || ' ' || lower(occupation) || 's.'
    )
from occupations
group by occupation
order by count(name),
    occupation;