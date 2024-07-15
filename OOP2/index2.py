#Base class or Super Class
# class father():
#     def __init__(self):
#         self.surname = "people"


#     def description(self):
#         return f"This is from the line of the {self.surname} family."
    

# #Derived Class or Sub Class
# class Daughter(father):
#     def __init__(self):
#         super().__init__()

#     def description(self):
#             return "I'm now part of the family of Ajegunle"

    
# excel = Daughter()

# print(excel.description())


# name = 'king'
# name = 'miracle'



#polymorphism


# def sum(a, b):
#     return a + b

# print(sum("Harry ", "Maguire"))
# print(sum([1,2,3,4,5], [6,7,8,9,0]))


def Sum(a , b):
    return a + b

class Merge:
    def sum(self,a,b):
        return a + b
    
addition = Merge()

# concat = Merge()

print(addition.sum(1, 2))
# print(concat.sum("Harry ", "Maguire"))