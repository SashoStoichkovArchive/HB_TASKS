# in terminal - pwd: print working directory
# in terminal - cat
# statement - част от езика/синтаксис

print("hello world")

# type
print(type(1))
print(type(1.1))
print(type("asd"))
print(type(True))

print(type([1, 2, 3]))

# dictionary
d = {
	"a": 1,
	"b": 2
}

print(d["a"])

# if/else
a = True

if a:
	if a:
		print("print")

	else:
		print("else")

else:
	print("asd")

# for
arr = [1, 2, 3]

for i in arr:
	print(i)

for key in d:
	print(key, d[key])

# dict
d1 = {
	"asd": 1,
	"jackpot": 100
}

def all_in(xs, ys):
	for x in xs:
		if x not in ys:
			return False

	return True

print(all_in([2, 3, 5], [1, 2, 3]))



