def print_params(a = 99,b = 'Hello', c = True):
    print(a, b, c)



print_params()
print_params(100, 'Bay')
print_params(1, 25, [1, 2, 3])
values_list = [55,'You won', [1, 2]]
print_params(*values_list)
values_dict = {'a':11, 'b':'Go to party', 'c':[22,44]}
print_params(**values_dict)
values_list_2 = [[33, 55], 'We are happy']
print_params(*values_list_2,77)