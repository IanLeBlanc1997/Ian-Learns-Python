# #FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# #KeyError
# a_dictionary= {'key':'value'}
# value = a_dictionary['non-existant-key']

# #IndexError
# fruit_list = ["tomato",'pineapple','cherry']
# fruit = fruit_list['orange']

# #TypeError
# text = "abc"
# print(text + 5)

#handing exceptions

# try: something that might cause an exception
# except: do this if there was an Exception
# else: do this if there was not an Exception
# finally: do this no matter what 

# try:
#     file = open("a_file.txt")
#     a_dictionary = {'key':'value'}
#     print(a_dictionary['asdf'])
# except FileNotFoundError: 
#     file = open("a_file.txt",'w')
#     file.write("something")
# except KeyError as e:
#     print(f"There key {e} does not exist")
# else: 
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("I will always do this")
#     raise KeyError("This is an error I made up")

height = float(input('What is your height in meters?\n'))
weight = float(input("What is your weight in kilograms?\n"))
if height > 3:
    raise ValueError("Human height should not be over 3 meters") 
bmi = weight / height **2
print(bmi)
