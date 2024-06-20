def get_starting_number():
    number = input("How many bottles of beer on the wall?")
    while not number.isnumeric() or int(number) < 1:
        if not number.isnumeric():
            print("Please input a valid integer.")
        else:
            print("Please input an integer greater than 0.")
        number = input("How many bottles of beer on the wall?")
    return int(number)

def sing(starting_number):
    for i in range(starting_number, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i - 1 > 1:
                print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")

