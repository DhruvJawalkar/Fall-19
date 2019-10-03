import platform

print('You are running Python version '+platform.python_version())
name = input('What is your name? ')
age = int(input('How old are you now? '))
retirement_age = int(input('How old will you be when you retire? '))
current_savings = float(input('How much have you saved for retirement? '))
annual_saving = float(input('How much are you saving per year? '))
final_savings = current_savings+(annual_saving*(retirement_age-age))
print('{}, you will have ${} if you continue to save at the current rate.'.format(name, final_savings))

