def example_function():
    local_var = 20
    print(local_var)
    print(global_var)


example_function() #print(local_var) #it will raise an error because local_var is not defined. and because you cannot print a local variable out the function the local_var is in.


def whatever():
    another_global_var = 90

    whatever() #print(another_global_var) #it will raise an error because you cannot print a local variable outside the function.


    pi = 3.14
    if pi < 45:
        print(pi) #you cannot change the value of pi because pi is constant and it's a mathematical constant recognized by python.
















# global_var = 10
# print(global_var)


# def example_function():
#     local_var = 20
#     print(local_var)
#     print(global_var)


#     example_function()