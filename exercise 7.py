def print_name(name, number):
    for person in range(0, number):
        print(name)


user = str(input("name to print: "))
user_num = int(input("How many times"))
print_name(user, user_num)
