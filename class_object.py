class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")

emp = Employee(121231, "siva")

emp.display()

del emp.id

try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp

try:
    emp.display()
except NameError:
    print('emp is not defined')