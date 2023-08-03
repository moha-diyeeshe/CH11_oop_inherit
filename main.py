class Employee:
    def __init__(self, name, emp_number):
        self.name = name
        self.emp_number = emp_number

class ProductionWorker(Employee):
    def __init__(self, name, emp_number, shift_number, hourly_pay_rate):
        super().__init__(name, emp_number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    # Accessor methods for ProductionWorker class
    def get_shift_number(self):
        return self.shift_number

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

    # Mutator methods for ProductionWorker class
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate

name = input("Enter employee name: ")
emp_number = input("Enter employee number: ")
shift_number = int(input("Enter shift number (1 for day shift, 2 for night shift): "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))

worker = ProductionWorker(name, emp_number, shift_number, hourly_pay_rate)

# Display the data for the ProductionWorker
print("\nProduction Worker Information:")
print("Name:", worker.name)
print("Employee Number:", worker.emp_number)
print("Shift Number:", worker.get_shift_number())
print("Hourly Pay Rate:", worker.get_hourly_pay_rate())


