def uppercase(f):
    "Dada una función f que devuelve un string lo pasa todo a mayúsculas"
    def wrap():
        return f().upper()
    return wrap

def make_bold(f):
    "Dada una función f que devuelve un string le añade los tags de bold"
    def wrap():
        return "%s" % f()
    return wrap

@make_bold
@uppercase
def say_hello():
    return "Hello world"

print(say_hello())