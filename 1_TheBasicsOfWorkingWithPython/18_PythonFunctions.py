# A function lets us create a set of instructions that we can run when needed.

# Defining a function.
def print_user_name(name):
    return f"Welcome {name}" # 4 spaces tell the python interpreter it belongs to the function print_user_name.

# Calling a function.
print(print_user_name("tin"))

# A function can accept one or more parameters.
# Here in the below function multiple parameters such as name and age are passed.
# Positional arguments: name, age
def age_verifier(name,age):
    return f"Allowed: Hi {name} age criteria ia True as you age is {age}." if age >= 18 else f"Not Allowed: Hi {name} age criteria ia False as you age is {age}."

# Call with arguments, arguments are parameters defined in the function.
print(age_verifier('Siin',19))
print(age_verifier('Mia',12))
# print(age_verifier("Mia"))  TypeError: age_verifier() missing 1 required positional argument: 'age'
# A function can be called only when you mention all the positional arguments.

# Parameters vs Arguments
"""
We call parameters the values accepted by the function inside the
function definition, and arguments the values we pass to the function
when we call it. It's common to get confused about this distinction.
"""

# An argument can have a default value that's applied if the argument is not specified.
# Default parameter values : An argument can have a default value that's applied if the argument is not specified.
# Default arguments are not compulsory like positional arguments but can be overwritten by the user.

def university_admision_validator(name,gre_score,ielts_score,is_married= False):
    admission_granted = True if gre_score > 250 and ielts_score > 7 else False
    if admission_granted:
        if is_married:
            return f"You are admitted for {gre_score} and {ielts_score}, since you married there is a discount of 2000 dollars."
        else:
            return f"You are admitted for {gre_score} and {ielts_score}, since you married there is no discount."

    else:
        return f"You are not admitted for {gre_score} and {ielts_score}"
    
# name,age,gre_score,ielts_score are positional arguments, it needs to be specified in the same order. Default arguments need not be defined then default values will ne used.
print(university_admision_validator('Sri',267,8))
print(university_admision_validator('Sri',267,8,is_married=True))

# Important note: Parameters are passed by reference
# "Parameters are passed by reference" in Python is a common misconception. In reality, Python uses a mechanism called "pass by object reference" or "call by object reference." 

def square(number):
    return number * number

# For immutable objects - string, integer, flat, tuple.
number = 6
print(number) # 6
print(square(number)) # 36 # We are  passing only the reference of the number.
print(number) # 6

number = square(number)
print(number) # 36

# Contrast - for mutable. lists, sets, dictionaries.
# We are passing the object itself for mutable objects not the reference.
def add_2(array):
    array.append(2)

array = [1,3,5]
print(array) # [1,3,5]
print(add_2(array))
print(array) # [1,3,5,2] # It has modified the original array.

def even_array(array):
    even_array = []
    for number in array:
        if number % 2 == 0:
            even_array.append(number)
    return even_array

array = [1,2,3,4,5,6,7,8,9]
print(array) #  [1,2,3,4,5,6,7,8,9]
print(even_array(array))
print(array) #  [1,2,3,4,5,6,7,8,9]
array = even_array(array)
print(array)  # [2, 4, 6, 8]

"""
Conclusion:
Tkey distinction is not about passing by reference or value, but about mutability. 
Immutable objects (like integers) cannot be changed in place, so changes made inside a function won't affect the original object outside the function. 
Mutable objects (like lists) can be changed in place, so modifications inside a function will be visible outside.
"""

# A function can return a value, using the return statement.
def area_circle(radius):
    return 3.14 * (radius  ** 2) # pi * r * r
print(area_circle(9))

# When the function meets the return statement, the function ends.
# We can have the return statement inside a conditional, which is a common way to end a function if a starting condition is not met. 
# There can be on return statement for one condition but as soon as a particular return statement is reached a function ends.
def university_admision_validator(name,gre_score,ielts_score,is_married= False,is_disabled=False):
    admission_granted = True if gre_score > 250 and ielts_score > 7 else False
    if admission_granted:
        if is_married:
            return f"You are admitted for {gre_score} and {ielts_score}, since you married there is a discount of 2000 dollars."
        elif is_disabled:
            return f"You are admitted for {gre_score} and {ielts_score}, since you disabled there is a discount of 8000 dollars."
        else:
            return f"You are admitted for {gre_score} and {ielts_score}, since you married there is no discount."

    else:
        return f"You are not admitted for {gre_score} and {ielts_score}"
    
# Negative case
print(university_admision_validator('Sree',20,9))
# Positive case
print(university_admision_validator('Sree',290,9))
print(university_admision_validator('Sree',290,9,is_married=True))
print(university_admision_validator('Sree',290,9,is_disabled=True))

# Multiple values are returned as a tuple.
# We can return multiple values , default it will return as tuple.
def university_admision_validator(name,gre_score,ielts_score,is_married= False,is_disabled=False):
    admission_granted = True if gre_score > 250 and ielts_score > 7 else False
    if admission_granted:
        if is_married:
            return gre_score , ielts_score , {'is_admitted':True, "applicant_married": is_married, "applicant_disabled" : is_disabled} , {'admission_cost': 8000}
        elif is_disabled:
            return gre_score , ielts_score , {'is_admitted':True, "applicant_married": is_married, "applicant_disabled" : is_disabled} , {'admission_cost': 2000}
        else:
            return gre_score , ielts_score , {'is_admitted':True, "applicant_married": is_married, "applicant_disabled" : is_disabled} , {'admission_cost': 10000}

    else:
        return gre_score , ielts_score , {'is_admitted':True, "applicant_married": is_married, "applicant_disabled" : is_disabled} 

# Negative case
print(university_admision_validator('Sree',20,9))
# Positive case
print(university_admision_validator('Sree',290,9))
print(university_admision_validator('Sree',290,9,is_married=True))
print(university_admision_validator('Sree',290,9,is_disabled=True))

sree_admision_results = university_admision_validator('Sree',290,9,is_married=True)
print(sree_admision_results)
print(sree_admision_results[2]['is_admitted']) # True
print(sree_admision_results[3]['admission_cost']) #8000
