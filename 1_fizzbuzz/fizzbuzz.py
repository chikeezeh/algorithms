def fizzbuzz():
    x = int(input("Please enter an Integer: "))
    for i in range(1,x+1):
        if i % 15 == 0: #modulus operator(%) to check remainder.
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print ('Fizz')
        else:
            print(i)

if __name__ == '__main__': # allows the program to be run by calling the file name
    fizzbuzz()
