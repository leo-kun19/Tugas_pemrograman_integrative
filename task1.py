import math

def main():
    salary = int(input("Enter your annual salary: "))
    monthly_salary = math.ceil(salary / 12)
    print("Your monthly salary is:", monthly_salary)
main()
