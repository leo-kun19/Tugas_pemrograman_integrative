def main():
    numbers = []  
    while True:
        num = int(input("Enter a number (or -1 to stop): "))
        if num == -1:
            break
        numbers.append(num)
    total_sum = sum(numbers)
    print("The sum of all numbers entered is:", total_sum)
main()
