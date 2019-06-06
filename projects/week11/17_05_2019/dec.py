class SomeDec:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(self.func)
        return self.func(*args, **kwargs)

def debugmethods(cls):
    for attr, value in vars(cls).items():
        if callable(value):
            setattr(cls, attr, "Pesho")
        
    return cls