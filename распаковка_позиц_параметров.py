#1
def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

#2
values_list = [1, 'string' , 25.5]
print_params(*values_list)
values_dict = {'a':1, 'b':'string', 'c':25.5}
print_params(**values_dict)

#3
values_list_2 = [12, 'HELP']
print_params(*values_list_2, 42)