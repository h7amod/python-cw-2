my_name = input("whats your name: ")
my_age = input("whats your age: ")


print(f"my name is {my_name} and my age is {my_age}")


first_number = int(input("first number: "))
second_number = int(input("second number: "))
operator = input("operator(+-/*): ")

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)



bus_capacity = 30
peoples_input = int(input("how many people are in the bus"))
empty_seats = bus_capacity - peoples_input

if empty_seats > peoples_input:
    print("there is empty seats")
elif empty_seats <= peoples_input:
    print("there is no empty seats")