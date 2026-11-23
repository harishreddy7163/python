from employee import Employee
from salary_calculator import SalaryCalculator
from report_generator import ReportGenerator

emp = Employee("kattapa", 1200000)

# Calculate Salary
salary = SalaryCalculator()
result = salary.calculate_salary(emp)

print("Calculated Salary:", result)

# Generate Employee Report
report = ReportGenerator()
report.generate_report(emp)