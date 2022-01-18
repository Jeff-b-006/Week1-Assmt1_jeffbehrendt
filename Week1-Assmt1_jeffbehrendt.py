def front_two_back_two(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]
print(front_two_back_two('hello'))
print(front_two_back_two('h'))

Kelvin = float(input('Enter Kelvin temperature: '))
Celsius = Kelvin - 273.15
Fahrenheit = Celsius*(9/5) + 32
print('Temperature in Celsius is:',Celsius)
print('Temperature in Fahrenheit is:',Fahrenheit)

n = int(input('Enter 4 digit number: '))
def first(n):
    n = int(n / 1000)
    print("The first number is",n)
def last(n):
    n = int(n % 10)
    print('The last number is',n)
if n > 999 and n < 10000:
    first(n)
    last(n)
else:
    print('Not a 4 digit  number')

list = [int(number) for number in input('Enter list numbers with a space between each: ').split()]
min_max_sum = [min(list),max(list),sum(list)]
print(min_max_sum)

def print_square():
    dictionary = {}
    for i in range(1,16):
        dictionary[i] = i*i
    print(dictionary)
print_square()