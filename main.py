# def greet():
#   return "Hello Joel"
# print(greet)
#THIS CODE DID'NT RUN LIKE YOURS
# ==================================

# def greet(name):
#   return f"Good Morning Mr {name}"
# print(greet("Joel"))
  
# ============================
# def fruits(*names):
  
#     for i in names:
#       print((i))
  
# fruits("orange","apple","banana","cucumber")
#THIS CODE DID'NT RUN LIKE YOURS
# =============================================
# def fruits(*names):
#     '''
#     Accepts unknown number of fruit names and prints each of them
#     *name: list of fruits
#     '''
#     # names are tuples
#     for fruit in names:
#         print(fruit)

# fruits("Orange", "Banana", "Apple", "Grapes")
# =========================================================
# def greet(name):
#   '''
#   This fuction greets a person with a given messsage
#   name: person to greet
#   msg: message to greet the person with
#   '''
#   return f" Hello {name} Good morning i hope you are well."
# print(greet("Joel" ))
# =====================================================
# def person(**student):
#   # print(student)
#   # print(type(student))
#   for key in student:
#     print(student[key])
  
# # person(fname = "Joel", lname = "John",)
# person(fname = "Joel", lname = "John", subject = "python")
#======================================
#DEFULT KEY PARAMETER
# def greet(name= "david"):
#   return f"Hello, {name}"
# print(greet())
# ========================
#Recursion
def int(n):
  if n == 5:
    return True
  else:
    return n  * int(n -1)
print(int(4))


def greet():
    return "Hello Kingsley"

# ======================

'''
Functions with parameters
'''
def greet(name):
    '''
    Greets a person passed in as argument
    name: a name of a person to greet
    '''
    return f"Hello {name}, Good morning"

print(greet("Felix"))
print(greet("Kingsley"))
print(greet("Adriana"))

help(greet)

'''
Arbitrary parameters
'''

def fruits(*names):
    '''
    Accepts unknown number of fruit names and prints each of them
    *name: list of fruits
    '''
    # names are tuples
    for fruit in names:
        print(fruit)

fruits("Orange", "Banana", "Apple", "Grapes")

'''
Keyword parameters
'''

def greet(name, msg):
    '''
    This function greets a person with a given message
    name: person to greet
    msg: message to greet person with
    '''
    
    return f"Hello {name}, {msg}"

# print(greet("Kingsley", "Good morning!"))
# print(greet("Good morning", "Adriana!"))

print(greet(name="Kingsley", msg="Good morning!"))
print(greet(msg="Good morning", name="Adriana!"))

'''
Arbitrary Keyword parameters
'''

def person(**student):
    # print(type(student))
    # print(student)
    for key in student:
        print(student[key])

# person(fname="Kingsley", lname="Ijomah")
person(fname="Kingsley", lname="Ijomah", subject="Python")

'''
Default parameter values
'''

def greet(name='David'):
    return f"Hello, {name}"

print(greet())
print(greet("Dayana"))

'''
pass statement
'''

def greet():
    pass


'''
Recursion
'''

def factorial_recursive(n):
    '''
    Multiply a given number by every number less than it downt to 1 in a factorial way
    e.g if n is 5 then calculate 5*4*3*2*1 = 120
    n: is the highest starting number
    '''
    if n == 1:
        return True
    else:
        return n * factorial_recursive(n -1)

print(factorial_recursive(50))