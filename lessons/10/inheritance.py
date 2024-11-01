class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce_person(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}")


class Employee(Person):
    
    def __init__(self, first_name, last_name, job_type):
        super().__init__(first_name=first_name, last_name=last_name)
        self.job_type = job_type

    def work(self):
        print(f"{self.first_name} is working as a {self.job_type}")

    def introduce_person(self): #METHOD OVERRIDING
        print(f"Hello, my name is {self.first_name} {self.last_name} - {self.job_type}")

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.job_type}"
    
    def __eq__(self, other_object):
        if isinstance(other_object, Employee):
            return self.last_name == other_object.last_name and self.job_type == other_object.job_type
        return False


p1 = Person(first_name="John", last_name="Smith")
p1.introduce_person()
print("-------------")
e1 = Employee(first_name="Johnny", last_name="Smithy", job_type="developer")
e1.introduce_person()

e2 = Employee(first_name="Johnny", last_name="Smithy", job_type="developer")
print(e1 == e2)