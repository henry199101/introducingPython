class Person():
	def __init__(self, name):
		self.name = name

class EmailPerson(Person):
	def __init__(self, name, email):
		super().__init__(name)
		self.email = email

henry = EmailPerson('Henry he', 'mailhenry@foxmail.com')

print(henry.name)
print(henry.email)