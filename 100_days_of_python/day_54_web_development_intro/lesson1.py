import time
current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def speed_calc(): 
        time1 = time.time()
        function()
        time2= time.time()
        print(time2-time1)
    return speed_calc



@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    

fast_function()
slow_function()


##################################

def delay_decorator(function):
  def wrapper_function():
    time.sleep(2)
    function()
  return wrapper_function

@delay_decorator
def say_hello():
  print('Hello')

def say_bye():
  print("Bye")

def greeting():
  print('How are you?')
 