import random

result = {}
names = []


def get_names(num_of_friends):
    for i in range(num_of_friends):
        name = input()
        names.append(name)


def lucky(bill, num_of_friends):
    lucky_one = random.choice(names)
    print(f'{lucky_one} is the lucky one!')
    split = round(bill / (num_of_friends - 1), 2)
    for name in names:
        if name == lucky_one:
            result[name] = 0
            continue
        result[name] = split


def not_lucky(bill, num_of_friends):
    print('No one is going to be lucky')
    split = round(bill / num_of_friends, 2)
    for name in names:
        result[name] = split


print('Enter the number of num_friends joining (including you):')
num_of_friends_ = int(input())
print()
if num_of_friends_ < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    get_names(num_of_friends_)
    print()
    print("Enter the total bill value:")
    bill_ = int(input())
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    print()
    if choice == 'Yes':
        lucky(bill_, num_of_friends_)
    else:
        not_lucky(bill_, num_of_friends_)
    print(result)
