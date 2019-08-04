SELECT emp.emp_no, 
	   emp.last_name, 
	   emp.first_name,
	   emp.gender,
	   sal.salary 
FROM employees AS emp, 
	 salaries AS sal
WHERE emp.emp_no = sal.emp_no;

SELECT emp.emp_no, 
	   emp.first_name,
	   emp.last_name, 
	   emp.hire_date
FROM employees AS emp
WHERE emp.hire_date LIKE '1986%';

SELECT dpm.dept_no,
	   dpm.emp_no,
	   dept.dept_name,
	   emp.last_name,
	   emp.first_name,
	   dpm.from_date,
	   dpm.to_date
FROM dept_manager AS dpm
JOIN departments AS dept ON dpm.dept_no = dept.dept_no 
JOIN employees AS emp ON dpm.emp_no = emp.emp_no;

SELECT emp.emp_no,
	   emp.last_name,
	   emp.first_name,
	   dept.dept_name
FROM employees AS emp
JOIN dept_emp ON emp.emp_no = dept_emp.emp_no
JOIN departments AS dept ON dept_emp.dept_no = dept.dept_no;

SELECT emp.emp_no,
	   emp.last_name,
	   emp.first_name
FROM employees AS emp
WHERE emp.last_name LIKE 'B%'
AND emp.first_name = 'Hercules';

SELECT emp.emp_no,
	   emp.last_name,
	   emp.first_name,
	   dept.dept_name
FROM employees AS emp
JOIN dept_emp ON emp.emp_no = dept_emp.emp_no
JOIN departments AS dept ON dept_emp.dept_no = dept.dept_no
WHERE dept.dept_name = 'Sales';

SELECT emp.emp_no,
	   emp.last_name,
	   emp.first_name,
	   dept.dept_name
FROM employees AS emp
JOIN dept_emp ON emp.emp_no = dept_emp.emp_no
JOIN departments AS dept ON dept_emp.dept_no = dept.dept_no
WHERE dept.dept_name = 'Sales'
OR dept.dept_name = 'Development';

SELECT last_name, COUNT(last_name) AS frequency_count
FROM employees
GROUP BY last_name 
ORDER BY COUNT(last_name) DESC;
