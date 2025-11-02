class Person:

  name = ''
  age = ''
  gender = ''

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  
  def show_personal_details(self):
    print('Employee Name:', self.name)
    print('Employee Age:', self.age)
    print('Employee Gender:', self.gender)
  
  @classmethod
  def species(cls):
    return "Human"
  
  @staticmethod
  def is_adult(age):
    if age >= 18:
      return True
    else:
      return False
    
class WorkInfo:

  def __init__(self, eid, dept, sal):
    self.emp_id = eid
    self.dept = dept
    self.sal = sal

  def show_work_info(self):
    print('Employee ID:', self.emp_id)
    print('Employee Department:', self.dept)
    print('Employee Salary:', self.sal)

  @classmethod
  def organization_name(cls):
    return "TechCorp Pvt. Ltd."
  
  @staticmethod
  def is_high_earner(sal):
    if sal > 100000:
      return True
    
class Employee(Person, WorkInfo):

  def __init__(self, name, age, gender, eid, dept, sal, pos):
    Person.__init__(self, name, age, gender)
    WorkInfo.__init__(self, eid, dept, sal)
    self.position = pos

  def show_full_profile(self):
    Person.show_personal_details(self)
    WorkInfo.show_work_info(self)
    print('Postion:', self.position)


  
  
