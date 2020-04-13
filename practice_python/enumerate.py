the_dict = {'google': 'green', 'yahoo': 'purple'}
index_checker = dict(enumerate(the_dict.items(), 1))
for k, v in index_checker.items():
    print(f'{k}: {v[0]}')
num = int(input("Type number here: "))
for k, v in index_checker.items():
    if num == k:
        print(f'Yes, {num} is {k}')
        break
    else:
        print('No such number. Try again.')
