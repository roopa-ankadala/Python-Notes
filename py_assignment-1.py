Topics: Constructors, Class Attributes, and Instance Attributes

1. Core Concepts
Constructor (__init__)
A constructor is a special method in a class that executes automatically whenever a new object (instance) of that class is created. In Python, the constructor is always named __init__().
•	Purpose: Initializes the newly created object by assigning starting values to its attributes.
•	The self Parameter: Always the first parameter of __init__. It acts as a reference to the specific object being created, allowing attributes to be bound directly to that individual instance.
Class Attributes
A class attribute is a variable defined directly inside the class body, outside of any methods.
•	Shared State: Shared across all instances of the class. Every object reads the same value unless overridden on a specific instance.
•	Common Uses: Constants, shared configuration settings, or tracking values across all objects.
•	Access Syntax: Accessed via the class name (ClassName.attribute) or through an instance (object.attribute).
Instance Attributes
An instance attribute is a variable defined inside the constructor (__init__) or other instance methods using self (e.g., self.name = name).
•	Unique State: Belongs exclusively to the individual object. Modifying an instance attribute on one object does not affect any other object.
•	Common Uses: Object-specific data such as a student's name, an account balance, or a car's model.
•	Access Syntax: Accessed only via the specific instance (object.attribute).

2. Quick Comparison
Feature	Class Attributes	Instance Attributes
Definition Location	Inside the class body, outside all methods	Inside __init__ (or methods) using self
Data Sharing	Shared across all instances of the class	Unique to each individual instance
Effect of Modification	Updating via the class updates it for all instances	Updating affects only that specific instance
Access Syntax	ClassName.attr or instance.attr	instance.attr only

3. Practical Examples: 3 Classes with Constructors
Python
# ==========================================
# Class 1: Student
# ==========================================
class Student:
    # Class Attributes (shared by all students)
    institute_name = "10000 Coders"
    batch = "D27R"

    # Constructor
    def __init__(self, name, roll_no, course):
        # Instance Attributes (unique to each student)
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display_info(self):
        print(f"Student: {self.name} (Roll: {self.roll_no}) | Course: {self.course} | Institute: {Student.institute_name} ({Student.batch})")


# ==========================================
# Class 2: BankAccount
# ==========================================
class BankAccount:
    # Class Attributes (shared across all accounts)
    bank_name = "State Bank of Python"
    interest_rate = 0.04  # 4%

    # Constructor
    def __init__(self, account_holder, account_number, balance=0):
        # Instance Attributes (unique to each account)
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_account(self):
        print(f"{BankAccount.bank_name} | Holder: {self.account_holder} | A/C: {self.account_number} | Balance: ₹{self.balance}")


# ==========================================
# Class 3: Car
# ==========================================
class Car:
    # Class Attributes (shared by all cars)
    wheels = 4
    vehicle_type = "Four-Wheeler"

    # Constructor
    def __init__(self, brand, model, year, color):
        # Instance Attributes (unique to each car)
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_specs(self):
        print(f"{self.year} {self.brand} {self.model} ({self.color}) - {Car.wheels} wheels")


# ==========================================
# Creating Instances & Running Output
# ==========================================
if __name__ == "__main__":
    # 1. Student Instances
    student1 = Student("Roopa Ankadala", 101, "Python Full Stack")
    student2 = Student("Aarav Sharma", 102, "Data Science")
    student1.display_info()
    student2.display_info()

    print("-" * 60)

    # 2. BankAccount Instances
    acc1 = BankAccount("Roopa", "SB1001", 15000)
    acc2 = BankAccount("Vikram", "SB1002", 8500)
    acc1.display_account()
    acc2.display_account()

    print("-" * 60)

    # 3. Car Instances
    car1 = Car("Hyundai", "Creta", 2025, "White")
    car2 = Car("Tata", "Nexon", 2026, "Blue")
    car1.display_specs()
    car2.display_specs()
4. Program Output
Plaintext
Student: Roopa Ankadala (Roll: 101) | Course: Python Full Stack | Institute: 10000 Coders (D27R)
Student: Aarav Sharma (Roll: 102) | Course: Data Science | Institute: 10000 Coders (D27R)
------------------------------------------------------------
State Bank of Python | Holder: Roopa | A/C: SB1001 | Balance: ₹15000
State Bank of Python | Holder: Vikram | A/C: SB1002 | Balance: ₹8500
------------------------------------------------------------
2025 Hyundai Creta (White) - 4 wheels
2026 Tata Nexon (Blue) - 4 wheels