def encrypt(num):
    def accepter(func):
        def decorated():
            encrypted_string = ""
            for ch in func():
                if ch != " ":
                    char = chr(ord(ch) + num)
                    encrypted_string += char
                else:
                    encrypted_string += ch                    
            return encrypted_string
        return decorated
    return accepter

@encrypt(2)
def get_low():
    return "Get get get low"

print(get_low())