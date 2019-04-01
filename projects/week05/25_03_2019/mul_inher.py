class Soul:
    def __init__(self):
        print("Mentally")

class Body:
    def __init__(self):
        print("Physically")

class Person(Body, Soul):
    pass

Person()