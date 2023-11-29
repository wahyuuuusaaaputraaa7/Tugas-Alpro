import random
import os

def main():
    outfile = open("random_nums.txt", "w")
    for i in range (100):
        outfile.write(str(random.randint(0,399)) + " ")
    outfile.close()

    infile = open("random_nums.txt", "r")
    nums = infile.read()
    print(nums, "\n")

    os.system("cls")
    numbers = [int(x) for x in nums.split()]
    num_printed = 0

    print(f"{'Bilangan Random':^20}")
    odd_count = 0
    even_count = 0

    numbers = [int(x) for x in nums.split()]
    num_printed = 0
    for x in numbers:
        num_printed += 1
        print (format(x, "3d"), end= " ")
        if x % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if num_printed == 10:
            print()
            num_printed = 0
        else:
            print(" ", end= " ")
    print("\n")

    even_numbers = [x for x in numbers if x% 2== 0]
    odd_numbers = [x for x in numbers if x% 2!= 0]

    even_numbers = sorted(even_numbers)
    odd_numbers = sorted(odd_numbers)

    print("Bilangan Genap:")
    print_numbers(even_numbers)
    print("\n")

    print("Bilangan Ganjil:")
    print_numbers(odd_numbers)
    print("\n")
    
    print("Odd numbers:", odd_count)
    print("Even numbers:", even_count)
    
def print_numbers(numbers):
    num_printed = 0
    for x in numbers:
        num_printed += 1
        print(format(x, "3d"), end=" ")
        if num_printed == 10:
            print()
            num_printed = 0
        else:
            print(" ", end= " ")
main()