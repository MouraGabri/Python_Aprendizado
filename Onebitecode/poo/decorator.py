def meu_decorate(func):
    def wrapper():
        print('Antes de chamar a função')
        func()
        print('Depois de chamar a função')
    return wrapper


#Decorator para deixar texto em maiusculo
def upper_case(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper    