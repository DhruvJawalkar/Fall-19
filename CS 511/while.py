num = int(input('Enter a Number '))
n = 1
while n<=num: 
    if n%15 == 0:
        print(str(n)+' Fizz Buzz')
    elif n%3 == 0:
        print(str(n)+' Fizz')
    elif n%5 == 0:
        print(str(n)+' Buzz')    
    else:
        print(str(n))
    n += 1    
print('Done!')
