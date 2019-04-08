class Context:
    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

def generate():
    with Context as cm:
        res = 42
        print("CM prop: ", cm.prop)

        return res