class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def func(self):
		print("My name is " + self.name)

p1 = person("Pesho", 32)

print(p1.name)
print(p1.age)

p1.func()

