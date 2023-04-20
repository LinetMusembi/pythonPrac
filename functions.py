# Write a python function to find the maximum of three numbers
def numbers(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=b and c>=a:
        return c
print (numbers(4,7,9))
# Write a function that sums all the numbers in a list
def sum(nums):
    output=0
    for num in nums:
        output +=num
    return output
print(sum((23,42,78,90,30)))
# Write a python function to multiply all the numbers in a list
def multiply(numbs):
    total=1
    for numb in numbs:
        total *=numb
    return total
print(multiply((7,8,9)))
# Write a python function to reverse a string
def name(word):
    new=word[::-1]
    return new
print(name(("Lynet")))
# Write a python function that prints even numbers from a given list
# even numbers are numbers when divided by two they dont have a remainder so..
def evenNumbers(numbers):
    emptyArray=[]
    for number in numbers:
        if number %2==0:
            emptyArray.append(number)
    return emptyArray
print(evenNumbers([21,51,78,47,69,92]))
     