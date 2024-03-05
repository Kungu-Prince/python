#code for payroll
# Define a base class for Employee
class Employee:
    def __init__(self, employee_id, full_name, base_salary):
        self.employee_id = employee_id
        self.full_name = full_name
        self.base_salary = base_salary

    def calculate_salary(self):
        pass

# A subclass for HourlyEmployee inheriting from Employee
class HourlyEmployee(Employee):
    HOURLY_RATE = 2000

    def __init__(self, employee_id, full_name, base_salary, hours_worked):
        # Call the parent class constructor
        super().__init__(employee_id, full_name, base_salary)
        # Initializing additional attributes
        self.hours_worked = hours_worked

    def calculate_salary(self):
        # Calculate salary based on hours worked and hourly rate
        return self.hours_worked * HourlyEmployee.HOURLY_RATE

# Create a subclass for SalaryEmployee inheriting from Employee
class SalaryEmployee(Employee):
    def __init__(self, employee_id, full_name, monthly_salary):
        # Call the parent class constructor
        super().__init__(employee_id, full_name, monthly_salary)
        # Use the same attribute name for clarity
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        # Salary for SalaryEmployee is just the monthly salary
        return self.monthly_salary

# Create a subclass for CommissionEmployee inheriting from SalaryEmployee
class CommissionEmployee(SalaryEmployee):
    def __init__(self, employee_id, full_name, monthly_salary, commission_percentage):
        # Call the parent class constructor
        super().__init__(employee_id, full_name, monthly_salary)
        # Initialize additional attribute specific to CommissionEmployee
        self.commission_percentage = commission_percentage

    def calculate_salary(self):
        # Calculate salary with an additional commission based on a percentage
        return self.monthly_salary + (self.monthly_salary * self.commission_percentage / 100)

# Set a constant monthly salary for SalaryEmployee
BASE_SALARY_AMOUNT = 50000

# Prompt the user to enter employee details
employee_name = input("Enter your full name: ")
employee_id = input("Enter employee ID: ")
employee_type = input("Enter type of employee (Hourly/Salary/Commission): ")

# Determine the type of employee and calculate salary accordingly
if employee_type.lower() == "hourly":
    hours_worked = float(input("Enter hours worked: "))
    employee = HourlyEmployee(employee_id, employee_name, 0, hours_worked)
elif employee_type.lower() == "salary":
    employee = SalaryEmployee(employee_id, employee_name, BASE_SALARY_AMOUNT)
elif employee_type.lower() == "commission":
    commission_percentage = float(input("Enter commission percentage: "))
    employee = CommissionEmployee(employee_id, employee_name, BASE_SALARY_AMOUNT, commission_percentage)

# Display the calculated total salary for the employee
print(f"The total salary for {employee.full_name} with ID {employee.employee_id}  is: {employee.calculate_salary()}")
