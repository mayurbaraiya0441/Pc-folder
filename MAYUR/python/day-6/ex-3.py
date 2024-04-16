# Ex-6.3
# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
# 	Form the fullname by simply joining the first and last name together, separated by a space.
# 	Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.

# Examples:
# 	emp_1 = Employee("John", "Smith")
# 	emp_2 = Employee("Mary",  "Sue")
# 	emp_3 = Employee("Antony", "Walker")

# 	emp_1.fullname ➞ "John Smith"
# 	emp_2.email ➞ "mary.sue@company.com"
# 	emp_3.firstname ➞ "Antony"


class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = self.first_name + ' ' + self.last_name
        self.email = (self.first_name.lower() + '.' + self.last_name.lower() + '@company.com')



