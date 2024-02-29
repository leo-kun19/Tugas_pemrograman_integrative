import math

def main():
    number = int(input("Enter a whole number: "))
    result = number / 3
    if result % 1 == 0:
        print("Result:", int(result))
    else:
        print("Result:", round(result, 3))
main()
