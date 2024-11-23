# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        print("You called " + function.__name__ + str(args))
        print("It returned: " + str(function(*args)))
    return wrapper    

# TODO: Use the decorator 👇

@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)