print("Welcome! print the largest numbers")

result = 0
numbers = [20, 30, 40, 50, 60, 70, 80, 90, 100]

firstnumber = int(input("Enter your Number"))

result = numbers

while True:
    user_input = input("Enter the largest number (or type 'done' to finish): ")

    if user_input != "done":

        numbers = int(input("Enter the firstnumber"))
    else:
        largest_numbers = 0

        result = numbers - largest_numbers

        print(f"Total result: [result]")
        print(f"Total numbers: [numbers]")
        print(f"Remaining numbers: [result]")
        
        if result < 100:
            print("Nice Try.")
        else:
            print("Wow!!!!! You got the largest number.")
            print(f"Largest number: result]")

        break



