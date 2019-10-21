
import prompt
x = prompt.for_int('Enter a value in [0,5]', is_legal = (lambda x : 0<=x<=5))
print(x)

