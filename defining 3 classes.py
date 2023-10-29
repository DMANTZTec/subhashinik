'''1)Write a program with defining 3 classes like 
Person contains person_details method which display person name, address, mobile number, email.
Department contains department_details method which display department name 
Marks contains marks_details which display subject1, subject2, subject3 marks. 
Now use inheritance to achive the below requirement 
Staff class which needs to display department and person details. 
Student needs to display marks and person details.'''
class Person:
    def __init__(self,person_name,address,mobile_number,email):
        self.person_name=person_name
        self.address=address
        self.mobile_number=mobile_number
        self.email=email
    def display(self):
        print("person_name :" ,self.person_name)
        print("address :",self.address)
        print("mobile_number : ",self.mobile_number)
        print("email : ",self.email)
p1=Person("subhashini","madugula",7671970611,"subhashinikolluri124@gmail.com")

class department():
    def __init__(self,department_name):
        self.department_name=department_name
    def display(self):
        print("department :",self.department_name)
dept=department("IT")

class staff(Person):
    print("person_details")
person_details=staff("subhashini","madugula","7671970611","subhashinikolluri124@gmail.com")
person_details.display()
class staff(department):
    print("department_details")
person_department=staff("IT")
person_department.display()
class marks():
    def __init__(self,subject1, subject2, subject3):
        self.subject1=subject1
        self.subject2=subject2
        self.subject3=subject3
    def display(self):
        print("python : " ,self.subject1)
        print("java :",self.subject2)
        print("c++ ",self.subject3)
mark=marks(90,100,95)
class student(marks):
    print("student marks")
student_marks=student(90,100,95)
student_marks.display()
class student(Person):
    print("person details")
person=student("lali","eluru","8978229943","ramakrishnakilari27@gmail.com")
person.display()