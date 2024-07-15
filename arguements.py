# Arguments

# Positional Arguements.

def func(name, age):
    # logic
    return (name, age)

# print(func("Alice", 31))


# Keyword Arguements

def func_one(name="Alice", age=21, sex="Female"):
    return (name, age, sex)

# print(func_one())



# Default Arguements

def func_two(name, age, location="Lagos"):
    return (name, age, location)

# print(func_two("Alice", 22))

# print(func_two("Peter", 21, "Enugu"))



# Variable length Argument

def func_three(*names):
    print(names)
    return names


# print(func_three("Alice", "Sarah", "Kayode", "Mari"))



# Kwargs
def func_four(**person):
    return person

print(func_four(name="Alice", age=22, location="Lagos"))