class Employee:
    def __init__(self, first_name, race, salary):
        self.first_name = name
        self.last_name = race
        self.age = age
        self.salary = salary
        
    def introduce_self(self):
        return f'My name is {self.first_name} {self.last_name} and I am {self.age} years old'
    
    def raise_salary(self, ratio):
        self.salary = self.salary * ratio
        
    def check_age(self):
        if self.age < 18:
            return 'Underage employee'
        else:
            return 'Adult employee'
        
    def get_email(self):
        return f'{self.first_name}{self.last_name}@company.com'
