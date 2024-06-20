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
    bottles = starting_number
    while True:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            if bottles - 1 > 1:
                print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
        elif bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
            break
        bottles -= 1

