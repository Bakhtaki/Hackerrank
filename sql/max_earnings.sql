
select max(months * salary),
       count(months * salary)
from employee
where employee_id in(
        select employee_id
        from employee
        where months * salary in (
                select max(months * salary)
                from employee
            )
    );