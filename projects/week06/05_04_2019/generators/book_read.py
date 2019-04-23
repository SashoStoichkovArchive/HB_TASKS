import keyboard, os

first_part = open("../book/001.txt", "r")
second_part = open("../book/002.txt", "r")

for line in first_part:
    if line.startswith("#"):
        input("Next chapter ->")
        os.system('cls' if os.name == "nt" else "clear")
        print(line[1:])
    else:
        print(line)

for line in second_part:
    if line.startswith("#"):
        input("Next chapter ->")
        os.system('cls' if os.name == "nt" else "clear")
        print(line[1:])
    else:
        print(line)

first_part.close()
second_part.close()
