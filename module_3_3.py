def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(a='hello', b= 'world')


values_list = [2, 'Hi', 1.5]

values_dict = {'a':'Welcome','b':True, 'c': 3.5 }

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)