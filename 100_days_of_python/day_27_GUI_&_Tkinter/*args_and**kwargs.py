# def add(*args):
#    total = sum(args)
#    print(total)
# add(1,3,3)


# def calculate(n,**kwargs):
#     n += kwargs["add"]
#     n*= kwargs["multiply"]
#     print(n)

# calculate(2,add=3,multiply = 5)

class Car:
    def __init__(self,**kwarg):
        """model= , make ="""
        self.make = kwarg.get["make"]
        self.model = kwarg.get['model']
        self.color = kwarg.get["color"]
        self.seats = kwarg.get['seats']


car = Car()