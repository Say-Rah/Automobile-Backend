'''
  OOP - Object Oriented Programming.
'''

# class Person():
#     country = "Nigeria"
#     def __init__(self, name, age, complexion, gender):# A Constructor: Creates the attributes of a person
#      self.name = name #unique attributes
#      self.age = age
#      self.complexion = complexion
#      self.gender = gender

#     #Methods
#     def speak(self):
#       print(f"Hi i am {self.name} and  i am a {self.gender} and i am {self.complexion} in color.")
    

# me = Person("sarah", 17, "female", "dark skin")

# print(me.speak())



# class Automobile():
#     def __init__(self):
#         self.store = []

#     def add_a_car(self):
#         return "Audi"
    

# audi = Automobile()

# print(audi.add_a_car())


# class Automobile():
#     store = []
#     def __init__(self):
#         pass

#     def add_a_car(self, car_name, model, color, price=0):
#         self.store.append({"car_name":car_name, "model":model, "color":color, "price":price})

#         #View Cars

#         #update net_worth

#     def run_company(self): #methods or member functions
#         #while loop
#         return True
      
    

# audi = Automobile()

# print(audi.add_a_car("Lamborghini", "flexible", "red", 1000000))

# print(audi.store)


# print("Hello Welcome to Sarah's Cars Slot")
# print("Here at Sarah'Cars Slot! We sell all types of Cars.")


# class Animal():
#     def __init__(self, name, sound):
#       self.name = name
#       self.sound = sound

#     def add_an_animal(self):
#       return f"{self.name} is an animal and it's {self.sound}"

# Cat = Animal("cat", "meows")

# print(Cat.add_an_animal())

# print(audi.store)


class Automobile():
    store = []
    net_worth = 0
    def __init__(self, name, founded, ceo):
        self.name = name
        self.founded = founded
        self.ceo = ceo

    def add_a_car(self, car_name, model, color, price=0):
        self.store.append({"car_name":car_name, "model":model, "color":color, "price":price})

    # View Cars
    def view_cars(self):
        if len(self.store) == 0:
            print("No net worth")
        else:
            for car in self.store:
                print(
                    "==" * 8,
                    f"name: {car['car_name']}",
                    f"model: {car['model']}",
                    f"color: {car['color']}",
                    f"price: {car['price']}",
                    "==" * 8,
                    sep="\n"
                )

    # update net_worth
    def update_net_worth(self, price):
        self.net_worth += int(price)


    def run_company(self): # methods or member functions
        while True:
            command = input("Enter 'add' to add a car, 'view' to to see cars, 'quit', to exit: ")
            if command == "add":
                car_name = input("What is the name of the car: ")
                model = input("What is the model: ")
                color = input("What is the color the car: ")
                price = input("What is the price: ")

                self.add_a_car(car_name, model, color, price)
                self.update_net_worth(price)
                print(f"Car Added. Your net worth is {self.net_worth}")

            elif command == "view":
                self.view_cars()
            elif command == 'quit':
                print(f"Your net worth is {self.net_worth}. Thank you for your services")
                break
            else:
                print("Invalid command")


uni_global = Automobile("Uni Global", "2005", "Mr. Kayode")

print(uni_global.run_company())



# print("Welcome to your financial manager checker")

# income = 0
# expenses = {}

# salary = int(input("What is your total income for the month: "))

# income = salary

# while True:
#     user_input = input("Enter expense name (or type 'done' to finish): ")

#     if user_input != "done":
#         amount = int(input("Enter the amount of the expense: "))
#         expenses.update({user_input: amount})
#     else:
#         total_expense = 0
#         for key in expenses.values():
#             total_expense += key

#         result = income - total_expense

#         print("--- Summary ---")
#         print(f"Total income: ${income}")
#         print(f"Total expenses: ${total_expense}")
#         print(f"Remaining Balance: ${result}")
        
#         if result < 0:
#             print("You have exceeded your monthly expenses.")
#         else:
#             print("Congratulations. You managed you money well.")
#         break