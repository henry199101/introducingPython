class A():
	count = 0
	def __init__(self):
		A.count += 1
	def exclaim(self):
		print("i am an A")
	@classmethod
	def kids(cls):
		print("A has", cls.count, "little objects.")


easy_A = A()
breezy_a = A()
wheezy_a = A()
A.kids()