--list all employees with their respective department

select e.employee_id, e.full_name, d.department_name 
from employee e
inner join department d on e.department_id = d.department_id 


-- list employees where the manager is John Smith

select e.employee_id, e.full_name, e.job_role 
from employee e
where e.manager_id = (select employee_id from employee where full_name = 'John Smith')

-- display each department with number of employees

select d.department_name, count(e.employee_id) as employee_count
from department d
left join employee e on d.department_id = e.department_id 
group by d.department_name 


--select departments without employees

select *
from department d
left join employee e on e.department_id = d.department_id 
where employee_id IS NULL


-- retrieve hierarchical employee reporting structure
select e1.full_name as employee_name, e2.full_name as manager_name
from employee e1
left join employee e2 on e1.manager_id = e2.employee_id 
order by e2.full_name desc

-- departments with more than 2 employees

--solution 1: having

select d.department_name, count(e.employee_id) as employee_count
from department d
left join employee e on d.department_id = e.department_id 
group by d.department_name 
HAVING count(e.employee_id) > 2


--solution 2: cte - common table expression

with department_employee_count as (
select d.department_name, count(e.employee_id) as employee_count
from department d
left join employee e on d.department_id = e.department_id 
group by d.department_name 
)
select * from department_employee_count
where employee_count > 2


select * from department

