# Program to find the sum and the sum of the cubes of the first n natural numbers respectively

def sumN(n):
    num = 0

    for x in range(1, n+1):
        num = num + x

    return num

def sumNcube(n):
    num = 0

    for x in range(1, n+1):
        num = num + (x**3)

    return num

def main():
    print("This program finds the sum of the first n natural numbers.")

    n = int(input("Enter the value of n: "))

    print("The sum of all the numbers upto {0}, is: {1}".format(n, sumN(n), sumNcube(n)))

    print("The sum of all the numbers upto {0} cubed, is: {2}".format(n, sumN(n), sumNcube(n)))
 
main()