Number = input("Enter a number: ")
while True:
        if Number.isdigit():
                print("You entered a number")
                Number = int(Number)
                if Number % 2 == 0:
                        print(f"And {Number} is even")
                else:
                        print(f"And {Number} is odd")
        else:
                print("Please enter a valid number")
        Number = input("Enter a number: ")