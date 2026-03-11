class Person:
    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name

class Employee:
    def __init__(self,emp_id):
        self.emp_id=emp_id

class Manager(Person,Employee):
    def __init__(self,emp_id,name):
        Person.__init__(self,emp_id)
        Employee.__init__(self,emp_id)
        self.name=name
        