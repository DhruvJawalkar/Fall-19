num = int(input('Enter a Number '))
for n in range(1,num+1):
    if n%15 == 0:
        print(str(n)+' Fizz Buzz')
    elif n%3 == 0:
        print(str(n)+' Fizz')
    elif n%5 == 0:
        print(str(n)+' Buzz')    
    else:
        print(str(n))
print('Done!')
